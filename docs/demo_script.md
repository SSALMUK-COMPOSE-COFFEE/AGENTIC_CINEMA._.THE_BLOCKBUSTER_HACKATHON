# 데모 영상 대본 (3분, 영어 내레이션 또는 영어 자막)

녹화 전 준비
- `docker compose up -d` 상태에서 https://shotmemory.hajin.xyz (또는 http://localhost:5175) 열기
- 브라우저 창 1440×900, 다크 테마 그대로
- 에이전트 응답은 검색 25~45초, 러프컷 60~130초. 녹화 후 대기 구간은 편집으로 잘라낸다
- 인제스트가 돌고 있으면 임베딩 429 재시도로 느려진다. 녹화 중에는 인제스트를 멈춘다
- 시작 전 서버를 한 번 재시작해 워밍업이 끝난 상태로 녹화한다 (첫 요청은 20초 느림)

| 시간 | 화면 | 영어 내레이션 |
| --- | --- | --- |
| 0:00–0:20 | 스프레드시트 로그 시트에 타임코드를 손으로 적는 장면 (직접 촬영 또는 화면 녹화) | A documentary assistant editor logs a hundred hours of footage by hand. Who is in the shot, where, what time of day, what size. It takes weeks. Then the editor asks for "a rainy night close-up of two people", and half a day disappears into the log sheet. |
| 0:20–0:45 | Shot Memory 첫 화면. 상단 카운터 "4 films · N shots · N h" 강조. 필름 드롭다운에서 His Girl Friday 선택해 샷 그리드 스크롤 | Shot Memory watches every shot for you. Gemini writes the log: caption, people, time of day, interior or exterior, shot size, camera move, tension. Gemini Embedding turns a frame into a vector. ClickHouse remembers all of it, one row per shot. |
| 0:45–1:25 | 예시 버튼 "rainy night, two people, close-up" 클릭. 에이전트 패널에 EditorAssistant → Librarian → embed_query → run_query 순서로 뜨는 것 보여주기. 결과 그리드. SQL 패널 열어 "ClickHouse 50 ms" 강조. 카드 호버로 프록시 재생. "Similar" 클릭 | Ask in plain language. The Librarian agent embeds the request, writes one hybrid SQL query, and runs it through the official ClickHouse MCP server. Hard filters and vector distance in the same query. ClickHouse answers in tens of milliseconds. Hover to play the shot. Click Similar for a vector neighbour search. |
| 1:25–2:20 | 입력창에 "build a 45-second teaser: tension rising to a climax, then release" 입력. 에이전트 패널에서 CutAssembler가 Librarian을 비트별로 4번 병렬 호출하는 것, 이어서 ContinuityChecker → check_metadata → compare_frames 뜨는 것. 타임라인 생성, 경고 목록. 경고 하나에 마우스 올려 설명. 샷 하나 ×로 빼고 순서 이동. "Export EDL" 클릭 → 다운로드된 .edl을 텍스트 편집기 또는 Resolve에서 열기 | Now an editing brief. The CutAssembler splits it into beats and sends the Librarian out for each one, in parallel. The ContinuityChecker pulls adjacent-shot metadata from ClickHouse, applies the rules, and asks Gemini to look at the frames when the rules fire. The editor approves, swaps, reorders, and exports a CMX3600 EDL for Resolve, Premiere, or Final Cut. |
| 2:20–2:50 | README 아키텍처 다이어그램 (Google ADK · Gemini 3.8 Flash · Gemini Embedding 2 · mcp-clickhouse · ClickHouse 박스). `backend/app/agent/tools/clickhouse_mcp.py` 코드 잠깐 | Under the hood: Google ADK runs the agent team, Gemini does every model call, and ClickHouse is not a chatbot backend but the agents' long-term memory, joined at runtime through mcp-clickhouse. Remove ClickHouse and nothing works. |
| 2:50–3:00 | 포지셔닝 문장 + 저장소 URL + 라이브 URL | Shot Memory. Search hundreds of thousands of shots in plain language, and let the agents assemble the first cut. |

주의
- 배경 음악은 무음 또는 퍼블릭 도메인
- 화면에 타사 로고가 보이지 않게 (브라우저 북마크 바 숨기기, 파일 관리자 대신 텍스트 편집기)
- 자막을 쓸 경우 영어 자막 필수
- YouTube 공개(public) 업로드 후 URL을 Devpost에 입력
