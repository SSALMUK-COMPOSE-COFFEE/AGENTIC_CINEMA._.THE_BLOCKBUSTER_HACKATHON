# Shot Memory

Natural-language shot search and rough-cut assembly for film editors, built on Google ADK, Gemini, and ClickHouse.

Submission for **Agentic Cinema: The Blockbuster Hackathon** — ClickHouse track.

## What it does

1. Ingest a film: detect shots, have Gemini write a structured log for each one (caption, people, time of day, weather, shot size, camera move, emotion), and embed a representative frame.
2. Store everything in ClickHouse: metadata columns plus a vector column for hybrid search.
3. An ADK agent team (Librarian, CutAssembler, ContinuityChecker, Narrator) talks to ClickHouse through the official `mcp-clickhouse` MCP server to search shots, assemble sequences, and flag continuity problems.
4. Export the result as an EDL for Premiere, Resolve, or FCP.

## Stack

| Layer | Choice |
| --- | --- |
| Agents | Google ADK (`google-adk`) + Gemini (`google-genai`) |
| Data | ClickHouse via `mcp-clickhouse` at runtime, `clickhouse-connect` for ingest |
| API | FastAPI |
| UI | React + Vite |

## Run locally

```bash
cp .env.example .env                    # set GEMINI_API_KEY
docker compose up -d clickhouse         # schema is applied on first start
uv tool install mcp-clickhouse          # the MCP server the agents talk to
cd backend && uv sync && uv run uvicorn app.main:app --reload --port 8010
cd web && npm install && npm run dev    # http://localhost:5173
```

Ingest a film:

```bash
cd backend && uv run python -m app.ingest.pipeline ../data/films/charade.mp4 --title "Charade" --year 1963
```

Only three settings are required: `GEMINI_API_KEY`, optional `GEMINI_BASE_URL`, and `GEMINI_MODEL`.

## Demo data

Public-domain films only. Sources are listed in `docs/` alongside each title.

## License

Apache-2.0
