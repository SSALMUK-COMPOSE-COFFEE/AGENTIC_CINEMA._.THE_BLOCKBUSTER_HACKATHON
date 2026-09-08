# Shot Memory

Natural-language shot search and rough-cut assembly for film editors, built on Google ADK, Gemini, and ClickHouse.

Submission for **Agentic Cinema: The Blockbuster Hackathon**, ClickHouse track.

Live: https://shotmemory.hajin.xyz

## The problem

A documentary assistant editor logs 100 to 500 hours of footage by hand: who is in the shot, where, what time of day, what shot size, what mood. That takes weeks. When the editor asks for "a rainy night close-up of two people", the assistant spends half a day going back through the log sheet. Trailer and teaser assembly repeats that search dozens of times.

| Task | Today | Shot Memory |
| --- | --- | --- |
| Log 100 hours of footage | 2 to 3 weeks of assistant time | A few hours of unattended batch ingest |
| One conditional search | 30 minutes to half a day | Tens of milliseconds in ClickHouse, under a minute end to end |
| First 60-second teaser draft | A day | About a minute of agent work, then editor review |

## What it does

1. **Ingest** a film: detect shots, have Gemini watch each one and write a structured log entry (caption, people, time of day, interior/exterior, weather, shot size, camera move, emotion, tension), and embed a representative frame with Gemini Embedding.
2. **Store** every shot as one row in ClickHouse: typed metadata columns plus an `Array(Float32)` embedding column, so one SQL query combines hard filters with vector distance.
3. **Search and assemble** through a Google ADK agent team. The agents reach ClickHouse only through the official `mcp-clickhouse` MCP server at runtime.
4. **Export** the result as a CMX3600 EDL for Premiere, Resolve, or Final Cut.

## Architecture

```
                          ┌──────────────────────────────────────────────────┐
                          │  Google ADK agent team  (google-adk)             │
  Editor ──► React UI ───►│  EditorAssistant                                 │
             (SSE trace)  │    ├─ Librarian ────── embed_query               │
                          │    ├─ CutAssembler ─── Librarian ×N (parallel)   │
                          │    │                   ContinuityChecker         │
                          │    │                     ├─ check_metadata       │
                          │    │                     └─ compare_frames       │
                          │    │                   build_edl · save_sequence │
                          │    └─ Narrator                                   │
                          │  every model call: Gemini 3.8 Flash (google-genai)│
                          └──────────────────────┬───────────────────────────┘
                                                 │  MCP over stdio: run_query
                                                 ▼
                          ┌──────────────────────────────────────────────────┐
                          │  mcp-clickhouse  (official ClickHouse MCP server)│
                          └──────────────────────┬───────────────────────────┘
                                                 ▼
                          ┌──────────────────────────────────────────────────┐
                          │  ClickHouse                                      │
                          │   shots  (metadata columns + 3072-d embedding)   │
                          │   query_vectors · sequences · search_log         │
                          └──────────────────────▲───────────────────────────┘
                                                 │  clickhouse-connect batch INSERT
  Film file ──► Ingest: PySceneDetect ─► ffmpeg proxy + thumbnails
                ─► Gemini 3.8 Flash  (structured shot log, response_schema)
                ─► Gemini Embedding 2 (image mode, 3072 dimensions)
```

Google products in the runtime path:

| Product | Package | Used for |
| --- | --- | --- |
| Google ADK (Agent Builder family) | `google-adk` | Multi-agent orchestration, `AgentTool`, `McpToolset`, callbacks that stream every tool call to the UI |
| Gemini 3.8 Flash | `google-genai` | Shot logging at ingest, routing, SQL generation, cut assembly, visual continuity comparison, narration |
| Gemini Embedding 2 | `google-genai` | Shot embeddings (image mode) and query embeddings (text mode) |

### Why ClickHouse is not optional

Remove ClickHouse and nothing works. Search is one hybrid SQL statement the Librarian writes and runs through `mcp-clickhouse`:

```sql
WITH (SELECT embedding FROM query_vectors WHERE query_id = '…') AS q
SELECT shot_id, film_title, t_in, t_out, caption, people_count, time_of_day, interior, shot_size, tension,
       thumbnail_uri, proxy_uri, round(cosineDistance(embedding, q), 4) AS dist
FROM shots
WHERE time_of_day = 'night' AND people_count = 2 AND shot_size IN ('cu', 'mcu')
ORDER BY dist ASC
LIMIT 12
```

The query vector is staged in `query_vectors` by the `embed_query` tool so the agent's SQL stays short. The CutAssembler runs that search once per beat, the ContinuityChecker reads adjacent-shot metadata from the same table, and assembled sequences and search history are written back. The only direct driver access is the ingest job and the row hydration that fills the UI after an agent returns shot ids; every agent read goes through MCP.

## Agent team

| Agent | Role | Tools |
| --- | --- | --- |
| EditorAssistant | Routes the editor's message and hands the result to the Narrator | Librarian, CutAssembler, Narrator |
| Librarian | Turns a description into one hybrid SQL query, with a strict query budget | `embed_query`, `mcp-clickhouse` |
| CutAssembler | Splits a brief into beats, searches each beat in parallel, orders shots, exports the EDL | Librarian, ContinuityChecker, `build_edl`, `save_sequence` |
| ContinuityChecker | Applies time-of-day, interior/exterior, and wardrobe-palette rules, then asks Gemini to compare frames | `check_metadata`, `compare_frames`, `mcp-clickhouse` |
| Narrator | One short explanation of the picks and warnings | none |

Agents return shot ids only. The backend hydrates rows from ClickHouse and streams them to the UI, so the models never spend tokens re-emitting result tables.

## Stack

| Layer | Choice |
| --- | --- |
| Agents | Google ADK + Gemini 3.8 Flash + Gemini Embedding 2 |
| Data | ClickHouse; `mcp-clickhouse` at runtime, `clickhouse-connect` for ingest and hydration |
| Shot detection | PySceneDetect + ffmpeg |
| API | FastAPI, server-sent events for the agent trace |
| UI | React + Vite |
| Deploy | Docker Compose (ClickHouse, API, nginx-served UI) |

## Run locally

```bash
cp .env.example .env                    # set GEMINI_API_KEY
docker compose up -d clickhouse         # schema is applied on first start
uv tool install mcp-clickhouse          # the MCP server the agents talk to
cd backend && uv sync && uv run uvicorn app.main:app --reload --port 8010
cd web && npm install && npm run dev    # http://localhost:5173
```

Or run the whole stack in containers:

```bash
cp .env.example .env
docker compose up -d --build            # UI on http://127.0.0.1:18091
```

Ingest a film (resumable; already-loaded shots are skipped):

```bash
cd backend && uv run python -m app.ingest.pipeline ../data/films/his_girl_friday.mp4 --title "His Girl Friday" --year 1940
```

`--threshold` sets the PySceneDetect content threshold (default 15, which suits flat-lit black-and-white footage). `--limit N` processes only the first N shots for a smoke test.

Only `GEMINI_API_KEY` is required. `GEMINI_MODEL` defaults to `gemini-3.8-flash` and `EMBEDDING_MODEL` to `gemini-embedding-2`. The schema is in `backend/sql/001_schema.sql`.

## Repository layout

```
backend/app/agent/           ADK agents, tools, and the SSE trace callbacks
backend/app/agent/tools/clickhouse_mcp.py   McpToolset for mcp-clickhouse
backend/app/ingest/          shot detection, proxies, Gemini logging, embeddings, batch load
backend/app/api/             FastAPI routes (films, shots, sequences, agent chat)
backend/sql/                 ClickHouse schema
web/                         React UI
deploy/                      host nginx site and setup script
```

## Demo data

Public-domain films only, downloaded from the Internet Archive.

| Film | Year | Public-domain basis | Source |
| --- | --- | --- | --- |
| His Girl Friday | 1940 | Copyright not renewed | https://archive.org/details/his_girl_friday |
| Night of the Living Dead | 1968 | Released without a copyright notice | https://archive.org/details/night_of_the_living_dead_dvd |
| Nosferatu | 1922 | Published before 1929 | https://archive.org/details/Nosferatu1922 |
| The Last Man on Earth | 1964 | Copyright not renewed | https://archive.org/details/TheLastManOnEarth_72 |

## License

Apache-2.0
