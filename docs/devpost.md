# Devpost 제출 폼 초안

트랙: ClickHouse

## Project name

Shot Memory

## Tagline

Natural-language shot search and agent-assembled rough cuts for film editors, with ClickHouse as the agents' long-term memory.

## About the project (영어, 4요소 포함)

### Inspiration

A documentary assistant editor logs 100 to 500 hours of footage by hand: who is in the shot, where, what time of day, what shot size, what mood. It takes weeks. When the editor asks for "a rainy night close-up of two people", the assistant spends half a day going back through the log sheet, and a trailer repeats that search dozens of times. We wanted the log sheet to write itself and the search to take a second.

### What it does

Shot Memory ingests a film, detects every shot, has Gemini write a structured log entry for each one, embeds a representative frame, and stores it all in ClickHouse. An editor then types a description ("lonely man walking through an empty street, wide shot") or an editing brief ("build a 60-second teaser: tension rising to a climax, then release"). A Google ADK agent team searches the archive with hybrid SQL, assembles an ordered sequence, checks continuity between adjacent shots, and exports a CMX3600 EDL that opens in Resolve, Premiere, or Final Cut.

### How we built it

- **Ingest**: PySceneDetect finds shot boundaries, ffmpeg cuts a 320p proxy and three thumbnails per shot, Gemini 3.8 Flash watches the proxy and returns a structured log (response_schema enforced), Gemini Embedding 2 embeds the middle frame in image mode (3072 dimensions). Rows go into ClickHouse in batches with clickhouse-connect.
- **Storage**: one ClickHouse table, `shots`, with typed metadata columns and an `Array(Float32)` embedding column, so one SQL statement combines hard filters (`time_of_day = 'night' AND people_count = 2`) with `cosineDistance` ordering. Query vectors are staged in a `query_vectors` table so the agent's SQL stays short. Assembled sequences and search history are written back.
- **Agents (Google ADK)**: EditorAssistant routes the request. Librarian embeds the query and writes one hybrid SQL query. CutAssembler splits a brief into beats and calls the Librarian per beat in parallel. ContinuityChecker applies metadata rules, then asks Gemini to compare frames visually. Narrator explains the result. Every agent runs on Gemini 3.8 Flash through `google-genai`.
- **ClickHouse at runtime**: the agents reach ClickHouse only through the official `mcp-clickhouse` MCP server, loaded as an ADK `McpToolset`. The only direct driver access is the ingest job.
- **UI**: React + Vite. The agent panel streams every tool call from every agent over SSE, the SQL panel shows the query the Librarian ran and the ClickHouse latency, and the timeline supports reorder, remove, and EDL export.

### Google Cloud usage

Google ADK (Agent Builder family) for multi-agent orchestration and MCP tool loading; Gemini 3.8 Flash via `google-genai` for shot logging, routing, cut assembly, continuity vision checks, and narration; Gemini Embedding 2 for shot and query embeddings.

### Partner usage (ClickHouse)

ClickHouse stores every shot with its embedding and metadata and answers the hybrid search that the whole product depends on. The agents query it at runtime through the official ClickHouse MCP server (`mcp-clickhouse`, `run_query`). Search, similar-shot lookup, cut assembly, and continuity checks all read from ClickHouse; sequences and search logs are written back.

### Data sources

Public-domain films from the Internet Archive: His Girl Friday (1940), Night of the Living Dead (1968), Nosferatu (1922), The Last Man on Earth (1964). Sources and the public-domain basis for each are listed in the README.

### Challenges we ran into

- A scene-detection threshold that works for modern footage found almost no cuts in flat-lit 1940s dialogue scenes; we tuned it per film and made the ingest resumable.
- The Librarian initially explored the schema with dozens of queries per request. Giving it a strict query budget and moving row hydration out of the LLM (the agent returns shot ids, the backend fetches rows from ClickHouse) cut a rough-cut request from over eight minutes to about a minute.
- The ContinuityChecker skipped its own rules when left to the model, so the metadata rules became a deterministic Python tool and the model only handles the visual comparison.
- Gemini rate limits during ingest slowed the agents; retries with exponential backoff and async embedding calls fixed it.

### What we learned

ClickHouse is a good fit for agent memory: one table, one query language, hybrid filter plus vector ordering in tens of milliseconds, and the MCP server means the agent writes SQL the editor can read. The biggest wins came from deciding what the model should not do.

### What's next

Per-beat emotion curves on the timeline, FCPXML export, cloud ingest jobs for multi-hundred-hour archives, and a "why this shot" explanation per card.

## Built with

google-adk, google-genai, gemini, clickhouse, mcp-clickhouse, fastapi, react, vite, pyscenedetect, ffmpeg, docker

## Links

- Repository: https://github.com/SSALMUK-COMPOSE-COFFEE/AGENTIC_CINEMA._.THE_BLOCKBUSTER_HACKATHON
- Live: https://shotmemory.hajin.xyz
- Video: (YouTube URL)

## 체크리스트

- [ ] 저장소 public 전환
- [ ] LICENSE 루트에 존재
- [ ] 라이브 URL 시크릿 창에서 접속 확인
- [ ] 영상 3분 이내, YouTube 공개, 영어
- [ ] 팀원 전원 Devpost 등록
