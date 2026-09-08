# Agentic Cinema: The Blockbuster Hackathon — 개요 및 트랙 정리

출처: https://agentic-cinema.devpost.com/ (Overview / Resources / Dates / Rules / 각 파트너 리소스 페이지)
정리 기준일: 2026-09-08

---

## 1. 대회 개요

| 항목 | 내용 |
| --- | --- |
| 대회명 | **Agentic Cinema: The Blockbuster Hackathon** |
| 태그라인 | **"Lights. Camera. Code."** |
| 주최 | **Google Cloud** (Devpost 호스팅) |
| 파트너 (트랙 스폰서) | **IBM · Grafana Labs · Parallel · ClickHouse · Replit** (5개) |
| 총 상금 | **$75,000** (현금) |
| 트랙 수 | 5개 (파트너별 1개), 트랙당 3개 시상 |
| 제출 마감 | **September 9, 2026 @ 2:00pm PDT** |
| 참가자 수 | 약 9,904명 등록 (조회 시점 기준) |
| 플랫폼 요건 | Web, Android, iOS 중 하나에서 동작 |
| 핵심 스택 | **Gemini / Gemini Enterprise Agent Platform + Google Cloud Agent Builder** + 선택한 파트너 제품/MCP |

### 참가 자격 (Eligibility)

> "Participants must be above the legal age of majority in their country of residence. Certain countries and territories are excluded from participation."

- 거주 국가의 성년 연령 이상이어야 함.
- **제외 국가/지역** (Official Rules 기준 원문):
  > "Afghanistan, Antarctica, China, Djibouti, Iraq, Kazakhstan, Somalia, Venezuela, Western Sahara, Italy, Brazil, Quebec, Cuba, Iran, Syria, North Korea, Sudan, Belarus, Russia, Vietnam, and the Crimea, Donetsk, and Luhansk regions of Ukraine."
- **대한민국은 제외 목록에 없음 → 참가 가능.**

### 상금 구조 (Prizes)

5개 트랙 모두 동일한 상금 구조:

| 순위 | 상금 | 비고 |
| --- | --- | --- |
| 1st Place | **$7,500** | + 소셜 미디어 홍보 (social media promotion) |
| 2nd Place | **$4,500** | |
| 3rd Place | **$3,000** | |

트랙당 $15,000 × 5개 트랙 = **$75,000**

---

## 2. 챌린지 설명

### 2-1. 원문 요지 (English, verbatim 인용 포함)

핵심 미션 문장:

> **"Build a functional agent—powered by Gemini and Google Cloud Agent Builder—that integrates a Partner Entity's product or MCP to power a real media & entertainment workflow."**

Official Rules 쪽의 더 강한 표현:

> "a functional, **production-ready** AI agent or multi-agent network—powered by Gemini and Google Cloud Agent Builder"

참가자 역할(role) 컨셉 — 영화 제작 스태프에 빗댄 3가지 페르소나:

- **Director**: "building production-ready autonomous agent networks"
- **Technical Producer**: "connecting secure data pipelines via **managed MCP servers**"
- **Studio Head**: "enforcing **Cloud IAM** security and governance across multi-agent workflows"

전체 톤을 요약하는 문장:

> "Vibe code with **Gemini Enterprise** and our leading partner technologies to cast the perfect enterprise tech stack and build the next generation of AI applications fit for the big screen."

### 2-2. 한글 번역/해설

이 해커톤은 **엔터프라이즈 워크플로우를 자율 에이전트 기반의 "프로덕션 시스템"으로 바꾸는 것**을 주제로 한다. 테마는 영화 제작(Cinema)이며, 실제로 만들어야 하는 것은 **미디어 & 엔터테인먼트 업계의 실제 워크플로우를 처리하는 동작하는 AI 에이전트(또는 멀티 에이전트 네트워크)** 이다.

세 가지 참가 페르소나는 곧 세 가지 기술 축을 의미한다.

1. **Director (감독)** — 프로덕션 수준의 자율 에이전트 네트워크 설계. 멀티 에이전트 오케스트레이션, ADK/Agent Engine 활용.
2. **Technical Producer (테크니컬 프로듀서)** — **managed MCP server**를 통해 안전한 데이터 파이프라인 연결. 파트너 MCP(Grafana MCP, ClickHouse MCP 등) 연동이 여기에 해당.
3. **Studio Head (스튜디오 대표)** — **Cloud IAM** 기반 보안/거버넌스를 멀티 에이전트 워크플로우 전반에 적용. 권한 분리, Secret Manager, 감사 로깅 등.

즉 심사에서 좋은 점수를 받으려면 "데모용 프로토타입"이 아니라 **실제 운영 가능한(production-ready) 아키텍처**여야 하며, Google Cloud 스택 + 파트너 제품이 **코드 안에서 실제로 호출**되어야 한다.

### 2-3. Why Join?

- Gemini Enterprise Agent Platform과 파트너 도구를 직접 다뤄보며, 로컬 아이디어를 **프로덕션 아키텍처**로 전환하는 실전 경험을 얻는다.
  > "Get hands-on experience with Gemini Enterprise Agent Platform and partner tools to transition local ideas into production architectures"
- 자동화된 프로덕션 워크플로우를 **임원급 심사위원, 엔터프라이즈 전문가, 엔지니어링 리더**에게 직접 피치할 수 있다.
  > "Pitch automated production workflows directly to executive judges, enterprise experts, and engineering leaders"

---

## 3. 트랙별 상세

> **공통 전제**: 어떤 트랙을 고르든 **Gemini + Google Cloud Agent Builder** 기반 에이전트여야 하며, 그 위에 해당 파트너의 제품/MCP를 **런타임에 실제로 사용**해야 한다. README에 이름만 적는 것은 인정되지 않는다.
>
> 또한 Official Rules 상 **Google Cloud AI 도구만 사용 가능** — "Use only Google Cloud AI tools (no AWS, Microsoft, OpenAI, or Anthropic models)". 즉 GPT/Claude 등 타사 LLM을 모델로 쓰면 실격 요소가 된다.

트랙별 필수 파트너 제품 요약:

| 트랙 | 필수 제품 (Mandatory) | 선택/권장 |
| --- | --- | --- |
| IBM | **IBM Bob** (개발 과정에서 사용 필수) | **Confluent** (실시간/이벤트 기반 데이터, 강력 권장) |
| Grafana Labs | **Grafana Cloud MCP server** (런타임 사용 필수) | Grafana Cloud AI Observability |
| Parallel | **Parallel Search API** (런타임 통합 필수) | Extract API, Task API, Monitor API, MCP Server |
| ClickHouse | **공식 ClickHouse MCP server (`mcp-clickhouse`)** + ClickHouse Cloud/셀프호스팅 클러스터 | ClickHouse Agent Skills |
| Replit | **Replit Agent** (개발 과정) + **Replit 배포** (`replit.app` / `replit.dev` 도메인) | — |

---

### 3-1. IBM 트랙

**필수 요구사항 (verbatim)**

> "Your project must be built using **IBM Bob** as part of the development process. Use of **Confluent** is optional but strongly encouraged to power real-time data and event-driven workflows."

- **IBM Bob 사용 증빙이 없으면, 구현 방식과 무관하게 IBM 트랙 심사 대상에서 제외된다.**
  ("Projects failing to demonstrate IBM Bob usage will not qualify for the IBM track, regardless of implementation approach.")

**평가 관점 (Success Criteria)**

> Strong submissions should show how AI meaningfully improves workflows, enhances decision-making, elevates customer experience, or drives measurable operational outcomes.

한글 요지: AI가 **워크플로우 개선 / 의사결정 향상 / 고객 경험 개선 / 측정 가능한 운영 성과**로 이어진다는 것을 보여야 한다. "측정 가능한(measurable)"이라는 단어가 핵심 — 정량 지표를 데모에 넣을 것.

**제공 리소스**

- IBM–Google 파트너십 소개 페이지
- "Welcome to IBM Bob" 비디오 튜토리얼
- IBM Bob Quick Start Tutorial
- IBM Bob Best Practices 가이드
- IBM Bob Trial 접근 링크
- IBM Confluent Trial 접근 링크

**힌트 / 전략**

- IBM Bob은 "개발 과정에서 사용(as part of the development process)"이 요건 → 데모 영상에 Bob으로 개발/생성하는 장면을 넣어 증빙하는 것이 안전하다.
- Confluent를 붙이면 "이벤트 드리븐 실시간 파이프라인"이라는 스토리가 생겨 **Technical Producer 축**과 잘 맞는다. 예: 라이브 방송 이벤트 스트림 → Confluent → Gemini 에이전트 → 실시간 자막/하이라이트 생성.
- 5개 트랙 중 유일하게 "런타임 사용"이 아니라 "개발 과정 사용"이 필수라는 점에서 요건 해석이 느슨한 편이나, 반대로 증빙 방법을 스스로 만들어야 한다.

---

### 3-2. Grafana Labs 트랙

**트랙 성격**

관측성(observability) 데이터를 활용하는 AI 에이전트. **라이브 프로덕션 컨텍스트를 조회하고 그에 기반해 행동(action)** 하는 에이전트를 만드는 것이 핵심.

**무엇을 만드는가 (What to Build)**

- "Query metrics (**PromQL**-compatible) and logs (**LogQL**) for live system context"
- 대시보드 검색 및 Grafana로 돌아가는 링크 생성
- **Grafana IRM** 워크플로우를 이용한 인시던트/알럿 조사
- 근본 원인 분석(root-cause analysis) 시 metrics · logs · traces 상관 분석

**예시 미션 (Example missions)**

- 발생 중인(firing) 알럿 조사
- **Loki** 로그와 **Tempo** 트레이스 상관 분석
- 근본 원인 요약(summarizing root causes)
- 대시보드에 어노테이션 추가(annotating dashboards)

**필수 기술 (Required)**

> Projects must actively use the **Grafana Cloud MCP server** at runtime, which "exposes **60+ tools** for querying metrics, logs, and traces, searching dashboards, and managing alerts."

- 선택 사항: **Grafana Cloud AI Observability** — 에이전트의 LLM 호출, 토큰 비용, 지연시간, MCP 툴 활동을 모니터링.

**기술 요구사항 (Technical Requirements)**

1. `grafana.com/products/cloud/` 에서 무료 Grafana Cloud 계정 생성
2. MCP 서버 사용 전, **Stack administrator가 Grafana Assistant 약관에 동의**해야 함
3. **Agent Development Kit (ADK)** 를 통해 연결 (Python, TypeScript 지원)
4. 제출물: 오픈소스 라이선스가 포함된 공개 저장소 + 약 3분 데모 영상

**중요 주의사항 (Unattended deployments)**

> The hosted MCP server requires **interactive browser authorization**. For fully unattended agents, use the **open-source Grafana MCP server with service-account tokens** instead.

한글: 호스팅형 MCP 서버(`https://mcp.grafana.com/mcp`)는 브라우저 대화형 인증이 필요하다. **완전 무인(unattended) 에이전트**를 만들려면 오픈소스 Grafana MCP 서버 + 서비스 계정 토큰을 사용해야 한다. → 데모에서 자동 실행 에이전트를 보여줄 계획이라면 처음부터 OSS MCP 서버 경로를 택하는 것이 안전하다.

**주요 링크**

- Grafana Cloud 가입: https://grafana.com/products/cloud/
- Hosted MCP 엔드포인트: https://mcp.grafana.com/mcp
- ADK Grafana 통합 문서: https://github.com/google/adk-docs/blob/main/docs/integrations/grafana-cloud.md
- MCP 문서: https://grafana.com/docs/grafana/latest/developer-resources/mcp/
- 커뮤니티: community.grafana.com, Grafana community Slack

---

### 3-3. Parallel 트랙

**파트너 소개 (verbatim)**

> "Parallel develops web infrastructure for AI agents. We provide a vertically integrated stack — from proprietary crawling and indexing to search, extraction, reasoning, and monitoring — purpose-built for AI systems that need accurate, fresh, traceable information from the open web."

한글: Parallel은 AI 에이전트를 위한 **웹 인프라**다. 자체 크롤링·인덱싱부터 검색·추출·추론·모니터링까지 수직 통합 스택을 제공하며, **정확하고 최신이며 추적 가능한(traceable)** 오픈 웹 정보를 필요로 하는 AI 시스템을 위해 설계되었다.

**필수 통합 (Required Integration)**

프로젝트는 런타임에 **Parallel Search API**를 실제로 통합해야 한다. 허용되는 방식:

- 공식 **`parallel-web` SDK** (Python 또는 TypeScript)
- 지원 통합: **Vercel AI SDK**의 `@parallel-web/ai-sdk-tools`
- **LangChain**의 `ParallelWebSearchTool`
- Parallel Web Search를 사용한 **Grounding configuration**

> Simply mentioning Parallel in documentation does not satisfy requirements—functional code integration is mandatory.

**사용 가능한 API/리소스**

- **Search API** — quickstart 제공 (필수 대상)
- **Extract API** — URL 콘텐츠 추출
- **Task API** — 대규모 웹 리서치 및 엔리치먼트
- **Monitor API** — 웹 변화 감시 및 알림
- **Parallel CLI**
- **Parallel Playground** — 테스트용
- 통합 가이드: **Gemini Enterprise integration** 문서, **Grounding Gemini Models** 가이드, **MCP Server for Search & Extract**

**크레딧 & 지원**

- 가입 시 자동으로 **$20–$80 Parallel 크레딧** 지급
- 결제 정보 추가 시 매월 **$5** 추가 크레딧
- 지원 문의: support@parallel.ai

**힌트 / 전략**

- Gemini의 **Grounding** 설정에 Parallel Web Search를 연결하는 경로가 공식적으로 지원되므로, "Gemini + Google Cloud Agent Builder" 필수 요건과 가장 자연스럽게 결합된다.
- 미디어/엔터테인먼트 워크플로우와의 접점: 실시간 트렌드·리뷰·소셜 반응 수집, 캐스팅/IP 리서치, 경쟁 작품 모니터링(Monitor API), 배급 시장 조사 등.

---

### 3-4. ClickHouse 트랙

**트랙 성격 (verbatim)**

> "one of the fastest and most resource-efficient real-time databases and data warehouses, optimized for diverse data-intensive and large-scale workloads."

**필수 기술 (verbatim)**

> Projects must "actively use ClickHouse at runtime via the official **ClickHouse MCP server (`mcp-clickhouse`)**, connecting to a **ClickHouse Cloud or self-hosted cluster**."

- **ClickHouse Agent Skills** 를 개발 중 사용하는 것은 권장되나 **선택 사항**.

**Day One 셋업**

1. **크레딧**: 신규 계정에 **$400 크레딧** 제공 (리딤 필요)
2. **인프라**: ClickHouse Cloud에서 service 생성 → quickstart 문서를 따라 수 분 내 쿼리 가능
3. **Skills 설치**: `npx skills add clickhouse/agent-skills`

**리소스**

- AI/MCP 통합 가이드 (에이전트를 ClickHouse에 연결)
- 공식 `mcp-clickhouse` 서버 문서
- **SQL Playground** — 공개 데이터셋으로 프로토타이핑
- ClickHouse examples 저장소, 공식 문서 홈

**예시 구현 (Example Implementations)**

- 프레임워크 통합 예시: **LangChain, LlamaIndex, DSPy**
- **AgentHouse** 데모 — 라이브 chat-with-data 경험, `llm.clickhouse.com` 에서 접근 가능

**힌트 / 전략**

- 요건이 "런타임에 MCP 서버를 통해 실제 사용"이므로, 에이전트가 자연어 → SQL → ClickHouse 조회를 수행하는 흐름을 데모에 명확히 보여야 한다.
- 미디어/엔터테인먼트 접점: 스트리밍 시청 로그 분석, 박스오피스/시청률 실시간 대시보드, 광고 성과 분석, 대용량 이벤트 로그 기반 콘텐츠 추천.
- $400 크레딧은 5개 트랙 중 가장 큰 인프라 크레딧.

---

### 3-5. Replit 트랙

**파트너 소개 (verbatim)**

> Replit enables users to "turn an idea into working software using natural language." The platform integrates "code, AI, database, authentication, security, testing, and publishing into one platform."

**필수 요구사항 (verbatim)**

> "your project must be built using **Replit Agent** as part of the development process, and the finished project must be **hosted and deployed directly on Replit** (a project URL on a **`replit.app` or `replit.dev`** domain)."

- 이 호스팅 요건을 충족하지 못하면 **자격 미달(ineligible)**.

**Replit 크레딧 코드**

- 구글 폼으로 신청: https://forms.gle/pwwvgDvbkgiRpADm6
- **신규 Replit 사용자 전용**. 기존 계정 보유자는 리딤 불가 → 다른 이메일로 신규 가입 필요.
- 신규 사용자에게 **Core tier 구독용 $20 크레딧** 제공. 첫 달 전액 커버되며, 카드 정보는 필요하지만 청구되지 않음. 다음 결제 주기 전에 취소해야 과금 방지.
- > "Using up your credits does not unpublish your app. Your project's published URL remains viewable to judges."
  (크레딧을 소진해도 앱이 내려가지 않으며, 게시된 URL은 심사위원이 계속 볼 수 있다.)

**리소스**

- Replit 리소스 문서 (Google Drive 링크로 제공)

**힌트 / 전략**

- 유일하게 **호스팅 위치까지 강제**하는 트랙이다. "Hosted project URL" 제출 요건과 결합해, 반드시 `replit.app`/`replit.dev` URL을 제출해야 한다.
- Replit Agent로 개발했다는 증빙(세션 스크린샷/영상)을 데모에 포함하는 것이 안전하다.
- 동시에 Gemini + Google Cloud Agent Builder 요건도 만족해야 하므로, Replit에 배포된 앱이 Google Cloud의 에이전트를 호출하는 구조가 된다.

---

## 4. 제출 요구사항 (Requirements)

### 4-1. 무엇을 만들어야 하나

> **"Build a functional agent—powered by Gemini and Google Cloud Agent Builder—that integrates a Partner Entity's product or MCP to power a real media & entertainment workflow."**

Official Rules의 프로젝트 요건:

- **Gemini + Google Cloud Agent Builder** 기반의 functional, **production-ready** AI 에이전트 또는 **멀티 에이전트 네트워크**
- **엔터테인먼트/미디어 워크플로우**를 다룰 것
- **Google Cloud AI 도구만 사용** — "no AWS, Microsoft, OpenAI, or Anthropic models"
- **Web, Android, iOS** 중 하나에서 동작할 것
- **대회 기간 중 새로 만든 프로젝트**여야 함 (newly created during the contest period)
- 선택한 트랙의 **파트너 제품 필수 통합** (IBM Bob / Grafana MCP / Parallel Search API / ClickHouse MCP / Replit Agent)

### 4-2. 제출 산출물 (Deliverables)

| # | 산출물 | 상세 |
| --- | --- | --- |
| 1 | **Hosted project URL** | 심사위원이 직접 테스트할 수 있는 배포 URL (Replit 트랙은 반드시 `replit.app`/`replit.dev`) |
| 2 | **3-Minute Trailer (Demo Video)** | 최대 3분. YouTube 또는 Vimeo 업로드, **공개(publicly visible)** 설정. **영어이거나 영어 자막 포함** |
| 3 | **Public code repository** | GitHub / GitLab / Bitbucket. **공개 저장소 + 오픈소스 라이선스 파일 명시** |
| 4 | **Text description** | 기능, 사용 기술, 배운 점(features, technologies, learnings) 서술 |
| 5 | **Partner track 선택** | 5개 중 하나 선택 |
| 6 | **Devpost 제출 폼 완료** | |

**데모 영상 관련 verbatim (매우 중요)**

> "**3-Minute Trailer (Demo Video)**: a demo video showing your project/agent **functioning as built — not a cinematic trailer**. Upload to YouTube or Vimeo, make it publicly visible, and make sure it's in English or includes English subtitles."

→ 대회 이름과 "Trailer"라는 표현 때문에 오해하기 쉬우나, **영화 예고편 스타일의 연출 영상이 아니라 실제 동작 데모 영상**이어야 한다.

**저장소 관련 verbatim (매우 중요)**

> "Include a URL to your open-source code repository for judging and testing on either GitHub, GitLab or Bitbucket. It must contain all source code, assets, and instructions needed to run, and must demonstrate **actual runtime use of Google Cloud and your chosen Partner's service (imported and called in code, not just named in the README)**"

→ Google Cloud와 파트너 서비스 모두 **코드 내에서 import 되고 호출**되어야 한다. README 언급만으로는 실격.

### 4-3. 심사 기준 (Judging Criteria)

4개 항목, **각 25% 동일 가중치**.

| 기준 | 원문 설명 | 한글 해설 |
| --- | --- | --- |
| **Technological Implementation** | How well the project uses Google Cloud and Partner services | Google Cloud와 파트너 서비스를 얼마나 잘 활용했는가 |
| **Design** | Whether it delivers a complete product experience, not just a proof of concept | PoC가 아닌 **완결된 제품 경험**을 제공하는가 |
| **Potential Impact** | Credible case for solving a real problem for a real audience | 실제 사용자의 실제 문제를 푼다는 설득력 있는 근거가 있는가 |
| **Quality of the Idea** | Creative, non-obvious use of services with genuine problem-space understanding | 창의적이고 뻔하지 않은 서비스 활용 + 문제 영역에 대한 진짜 이해 |

---

## 5. 일정 / 타임라인

KST = PDT + 16시간.

| 이벤트 | PDT | KST |
| --- | --- | --- |
| **Submissions Period 시작** | July 27, 1:45pm PDT | 2026-07-28 (화) 05:45 KST |
| **Submissions Period 종료 (제출 마감)** | **September 9, 2:00pm PDT** | **2026-09-10 (목) 06:00 KST** |
| **Judging Period 시작** | September 10, 12:00pm PDT | 2026-09-11 (금) 04:00 KST |
| **Judging Period 종료** | October 8, 12:00pm PDT | 2026-10-09 (금) 04:00 KST |
| **Winners Announcement** | October 13, 12:00pm PDT | 2026-10-14 (수) 04:00 KST |

> All times are listed in PDT (Pacific Daylight Time).

**현재 시점(2026-09-08) 기준 남은 시간: 제출 마감까지 약 2일.**

캘린더 추가 링크:
- Apple: https://agentic-cinema.devpost.com/calendar
- Google: https://agentic-cinema.devpost.com/calendar/google
- Outlook: https://agentic-cinema.devpost.com/calendar/outlook

---

## 6. 참고 링크 목록

### 6-1. 대회 공식

| 항목 | URL |
| --- | --- |
| 메인 페이지 | https://agentic-cinema.devpost.com/ |
| 참가 등록 | https://agentic-cinema.devpost.com/register?flow%5Bdata%5D%5Bchallenge_id%5D=30721&flow%5Bname%5D=register_for_challenge |
| 리소스 허브 | https://agentic-cinema.devpost.com/resources |
| Official Rules | https://agentic-cinema.devpost.com/rules |
| 일정 | https://agentic-cinema.devpost.com/details/dates |
| 프로젝트 갤러리 | https://agentic-cinema.devpost.com/project-gallery |
| 업데이트 | https://agentic-cinema.devpost.com/updates |
| 토론 포럼 | https://agentic-cinema.devpost.com/forum_topics |
| 제출 관리 | https://devpost.com/submit-to/30721-agentic-cinema-the-blockbuster-hackathon/manage/submissions |
| 운영 담당 이메일 | janet@devpost.com |
| Discord (리소스 페이지 기재) | https://discord.gg/7Dqk5ebCD4 |

### 6-2. 파트너 트랙 리소스 페이지

| 트랙 | URL |
| --- | --- |
| IBM | https://agentic-cinema.devpost.com/details/ibm-resources |
| Grafana Labs | https://agentic-cinema.devpost.com/details/grafana-resources |
| Parallel | https://agentic-cinema.devpost.com/details/parallel-resources |
| ClickHouse | https://agentic-cinema.devpost.com/details/clickhouse-resources |
| Replit | https://agentic-cinema.devpost.com/details/replit-resources |

### 6-3. 크레딧 신청

| 항목 | URL | 내용 |
| --- | --- | --- |
| Google Cloud 무료 체험 | https://cloud.google.com/free | no-cost trial |
| 해커톤 GCP 크레딧 폼 | https://forms.gle/XPe837tzogh8L5sX6 | **$100 크레딧**, 처리 1–5 영업일 |
| Replit 크레딧 코드 폼 | https://forms.gle/pwwvgDvbkgiRpADm6 | **$20**, 신규 사용자 한정 |
| ClickHouse | ClickHouse Cloud 신규 가입 | **$400 크레딧** |
| Parallel | 가입 시 자동 지급 | **$20–$80** (+ 결제수단 등록 시 월 $5) |

### 6-4. Google Cloud 필수 도구 문서 (Resources 페이지 Phase별 정리)

**Phase 1 — Core Frameworks**

| 항목 | URL | 관련성 |
| --- | --- | --- |
| Gemini Enterprise Agent Platform API Setup | https://cloud.google.com/vertex-ai/docs | Vertex AI 기반 에이전트 플랫폼 셋업. 모든 트랙의 출발점 |
| Agent Builder Guide (Low-Code) | https://cloud.google.com/dialogflow/cx/docs/concept/agent | **Google Cloud Agent Builder** — 대회 필수 컴포넌트. 로우코드 에이전트 정의 |
| Gemini SDK for Python | https://github.com/googleapis/python-genai | `google-genai` 파이썬 SDK. 코드 기반 개발 시 핵심 |
| Agent Engine Getting Started | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/intro_agent_engine.ipynb | 에이전트 배포 런타임 입문 노트북 |

**Phase 2 — Action & Data Connectivity**

| 항목 | URL |
| --- | --- |
| Document Processing Guide | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/document_processing.ipynb |
| RAG Q&A with BigQuery & PDFs | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/retrieval-augmented-generation/rag_qna_with_bq_and_featurestore.ipynb |
| Agent Builder Data Stores / Grounding Overview | https://cloud.google.com/vertex-ai/docs/generative-ai/grounding/overview |
| Gemini Multimodal Use Cases | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/intro_multimodal_use_cases.ipynb |
| Video Transcription Notebook | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/multimodal_video_transcription.ipynb |
| Video Captioning Notebook | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/multimodal-data-curation/captioning.ipynb |
| Imagen 3 Image Generation Guide | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb |
| Lyria 3 Music Generation | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/music/getting-started/lyria3_music_generation.ipynb |
| Gemini 3.1 Flash TTS Tutorial | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/getting-started/gemini_3_1_flash_tts.ipynb |
| Multi-Speaker Podcast Notebook | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/use-cases/podcast/multi-speaker-podcast.ipynb |
| Multimodal Sentiment Analysis | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/multimodal-sentiment-analysis/intro_to_multimodal_sentiment_analysis.ipynb |

> 관련성: 미디어 & 엔터테인먼트 워크플로우라는 주제 특성상 **영상 전사·캡셔닝, 이미지 생성(Imagen 3), 음악 생성(Lyria 3), TTS, 멀티스피커 팟캐스트, 감정 분석**이 곧바로 제품 기능이 된다. 대본(script) 처리에는 Document Processing + RAG 조합이 대응된다.

**Phase 4 — Reasoning & Logic (ADK)**

ADK 설치:

```
pip install "google-cloud-aiplatform[agent_engines,adk]>=1.101.0"
```

| 항목 | URL |
| --- | --- |
| Introduction to Agent Engine | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/intro_agent_engine.ipynb |
| Deploying ADK Agents to Agent Engine | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_deploy_your_first_adk_agent_on_agent_engine.ipynb |
| Live API on Agent Engine (Bidirectional Audio) | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_live_api_on_agent_engine.ipynb |
| Google Maps Agent Tutorial | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/tutorial_google_maps_agent.ipynb |
| **MCP Database Toolbox** | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/tutorial_mcp_toolbox_for_databases.ipynb |
| Introduction to Function Calling | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb |
| Forced Function Calling Guide | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/forced_function_calling.ipynb |
| Multimodal Function Calling | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/multimodal_function_calling.ipynb |

> 관련성: **ADK(Agent Development Kit)** 는 Grafana 트랙에서 명시적으로 연결 수단으로 지정되어 있고, MCP Database Toolbox는 ClickHouse 트랙과 직결된다. Function Calling은 파트너 API(Parallel Search API 등)를 툴로 노출하는 표준 방식이다.

**Phase 5 — Deployment & Safety**

| 항목 | URL | 관련성 |
| --- | --- | --- |
| Agent Builder Deployment / Versioning | https://cloud.google.com/dialogflow/cx/docs/concept/version | 배포 버전 관리 |
| Cloud Run Quickstart | https://cloud.google.com/run/docs/quickstarts | Hosted project URL 확보 경로 (Replit 트랙 제외) |
| Secret Manager Guide | https://cloud.google.com/secret-manager/docs | 파트너 API 키 보관 — **Studio Head(IAM/거버넌스) 축**에 직결 |
| Gemini Safety Settings | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb#Safety-Settings | 안전 설정 |

### 6-5. 파트너 기술 문서

| 항목 | URL |
| --- | --- |
| Grafana Cloud 가입 | https://grafana.com/products/cloud/ |
| Grafana Hosted MCP 엔드포인트 | https://mcp.grafana.com/mcp |
| ADK ↔ Grafana Cloud 통합 문서 | https://github.com/google/adk-docs/blob/main/docs/integrations/grafana-cloud.md |
| Grafana MCP 문서 | https://grafana.com/docs/grafana/latest/developer-resources/mcp/ |
| ClickHouse Agent Skills 설치 | `npx skills add clickhouse/agent-skills` |
| ClickHouse AgentHouse 데모 | https://llm.clickhouse.com |
| Parallel 지원 | support@parallel.ai |

---

## 7. 체크리스트 (실격 방지)

- [ ] Gemini + Google Cloud Agent Builder를 **코드에서 실제 호출**
- [ ] 선택한 파트너 제품/MCP를 **런타임에 실제 호출** (README 언급만 ❌)
- [ ] OpenAI / Anthropic / AWS / Microsoft 모델 **미사용**
- [ ] Web / Android / iOS 중 하나에서 동작
- [ ] 대회 기간 중 **신규 제작** 프로젝트
- [ ] 공개 저장소 + **오픈소스 라이선스 파일** 포함
- [ ] 실행 방법(instructions)과 모든 소스·에셋 포함
- [ ] **3분 이하** 데모 영상, YouTube/Vimeo **공개**, 영어 또는 영어 자막
- [ ] 영상은 **실제 동작 데모** (시네마틱 예고편 ❌)
- [ ] Hosted project URL 제출 (Replit 트랙이면 `replit.app` / `replit.dev`)
- [ ] Text description (features / technologies / learnings) 작성
- [ ] 트랙 선택 + Devpost 제출 폼 완료
- [ ] **마감: 2026-09-09 14:00 PDT = 2026-09-10 06:00 KST**
