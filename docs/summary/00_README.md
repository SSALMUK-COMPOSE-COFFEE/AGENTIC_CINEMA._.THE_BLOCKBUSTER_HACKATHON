# Agentic Cinema: The Blockbuster Hackathon — 분석 문서 인덱스

조사 기준일: 2026-09-08 (KST) · 출처: https://agentic-cinema.devpost.com/

| 파일 | 내용 |
| --- | --- |
| [01_overview_tracks.md](01_overview_tracks.md) | 대회 개요, 챌린지 설명, 5개 파트너 트랙별 필수 기술·요구사항, 제출물, 일정, 참고 링크 |
| [02_rules_judging_prizes.md](02_rules_judging_prizes.md) | 공식 규정 전문 정리: 참가 자격, 제출 체크리스트, 심사 기준, 상금표, IP, 실격 사유 |
| [03_resources_tooling.md](03_resources_tooling.md) | Google Cloud·파트너별 리소스, 크레딧 수령 방법, 스타터 키트, 커뮤니티, 트랙별 추천 스택 |
| [04_updates_discussions.md](04_updates_discussions.md) | 주최측 업데이트 10건, 포럼 공식 Q&A 모음, 미답변 리스크, 참가자 현황 |
| [05_project_gallery_competition.md](05_project_gallery_competition.md) | 갤러리 현황(마감 전 비공개), 직전 ADK 해커톤 프록시 분석, 트랙별 빈틈·우승 전략 |
| [06_project_ideas.md](06_project_ideas.md) | 아이디어 결정 기록: Shot Memory 선정 근거와 탈락 후보 7개 |
| [07_shot_memory_spec.md](07_shot_memory_spec.md) | Shot Memory 상세 설계: 아키텍처, 스키마, ADK 에이전트, 인제스트, UI, 데모 스크립트, 체크리스트 |

## 한눈에 보는 핵심

- 마감: 2026-09-09 14:00 PDT = KST 2026-09-10 06:00. 수상 발표 2026-10-13.
- 상금 $75,000. 5개 트랙(IBM / Grafana Labs / Parallel / ClickHouse / Replit) 각 1위 $7,500 · 2위 $4,500 · 3위 $3,000. 그랜드 프라이즈 없음.
- 심사: Stage 1 pass/fail 스크리닝 → Stage 2 4개 기준 동일 가중치(Technological Implementation / Design / Potential Impact / Quality of the Idea).
- 최대 실격 리스크
  - Google Cloud 외 AI 전면 금지 (OpenAI·Anthropic·AWS·MS). 개발 워크플로까지 적용, 기획 용도도 불가.
  - 2026-07-27 이후 신규 제작 프로젝트만 허용.
  - 리포에서 Google Cloud SDK와 파트너 제품의 실제 런타임 호출이 확인돼야 함 (README 언급만으로는 불가).
  - 3분 데모 영상은 실제 작동 시연이어야 하며 시네마틱 트레일러 불가.
- 트랙별 필수 기술: IBM → IBM Bob 사용 / Grafana → Grafana Cloud MCP 런타임 호출 / Parallel → Search API / ClickHouse → mcp-clickhouse 런타임 호출 / Replit → Replit Agent 사용 + replit.app 배포.
- 크레딧: GCP $100(폼 신청, 8/31 마감), ClickHouse $400, Parallel $20~80 자동, Replit $20(신규 계정만).
- 갤러리는 마감 전 비공개. 05 문서의 경쟁 분석은 직전 Google Cloud ADK Hackathon 데이터 기반 프록시.
