# 06. 프로젝트 아이디어 결정 기록

결정일: 2026-09-08 (KST)
**선정: Shot Memory (ClickHouse 트랙)** → 상세 설계는 [07_shot_memory_spec.md](07_shot_memory_spec.md)

---

## 1. 선정 근거

| 심사 기준 | Shot Memory가 상위권 조건을 충족하는 방식 |
| --- | --- |
| Technological Implementation | ADK 멀티에이전트 + Gemini 비디오 이해 + Vertex Embeddings + Cloud Run/Jobs + Storage. ClickHouse는 mcp-clickhouse로 런타임 결합. 제거 시 검색 자체가 사라짐 |
| Design | 채팅이 아닌 편집자 워크플로 화면(검색 그리드 · 타임라인 · 연속성 경고 · EDL 내보내기) |
| Potential Impact | 퍼블릭 도메인 영화로 **실제 푸티지** 데모. "로그 시트 수작업 하루 → 수 초"를 숫자로 증명 |
| Quality of the Idea | ClickHouse를 박스오피스 SQL 챗봇이 아니라 **영상의 장기 기억·검색 인덱스**로 재해석 |

트랙 경쟁은 많지만 경쟁작 대부분이 text-to-SQL 챗봇 구간이라 직접 경쟁하지 않는다.

---

## 2. 검토 후 탈락한 후보

| 후보 | 트랙 | 요지 | 탈락 사유 |
| --- | --- | --- | --- |
| Clearance Desk | Parallel | 각본 엔티티 → Parallel 병렬 리서치 → 클리어런스·고증 리스크 리포트 | 경쟁률은 최저지만 공개 영상에 가상 브랜드를 써야 해 실데이터 설득력이 떨어짐. **차순위 백업안** |
| Greenlight Memo | Parallel | 피칭 덱 → 비교작·캐스팅 리서치 → 투자 메모 | 흥행 데이터 인용 신뢰성 검증이 어려움 |
| Production Control Room | Grafana | 촬영 일정·예산을 시계열화, 알람 → 에이전트 조사 → 일정 재편 | 발상은 최상이나 데이터가 합성일 수밖에 없고 MCP 무인 인증 구성이 까다로움 |
| Stream Doctor | Grafana | 라이브 스트리밍 QoE 이상 진단 | 렌더팜 대시보드류와 같은 구간으로 묶일 위험 |
| Pipeline TD Agent | IBM | Blender/Nuke 파이프라인 스크립트 생성·샌드박스 검증 | IBM Bob은 개발 도구라 런타임 파트너 결합이 없음. 증빙 형식도 미확정 |
| Previz Forge | Replit | 각본 씬 → 프리비즈 웹앱 생성 → Replit 배포 | 물량 최다 트랙 + 에이전트의 Replit 배포 API 경로가 매끄럽지 않음 |
| Audience Pulse | ClickHouse | 시청 이탈 초단위 적재 → 편집 제안 | 실제 유지율 데이터 확보 불가, 합성 의존 |
