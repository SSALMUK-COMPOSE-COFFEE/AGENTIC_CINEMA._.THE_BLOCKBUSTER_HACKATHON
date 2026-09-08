# 03. 리소스 & 툴링 총정리

> 출처: https://agentic-cinema.devpost.com/resources 및 각 파트너 상세 페이지, 외부 공식 문서
> 조사 기준일: 2026-09-08 (제출 마감 2026-09-09 14:00 PDT)

## 0. 한눈에 보기

| 항목 | 내용 |
| --- | --- |
| 주최 | Google Cloud |
| 파트너 트랙 | IBM / Grafana Labs / Parallel / ClickHouse / Replit (5개, 택 1) |
| 총상금 | $75,000 (트랙당 $15,000 — 1위 $7,500 · 2위 $4,500 · 3위 $3,000) |
| 필수 조건 | Gemini + Google Cloud Agent Builder 기반 에이전트 + 선택한 파트너 서비스를 **런타임에 실제 호출** |
| 제출물 | 호스팅된 프로젝트 URL, 3분 데모 영상, 오픈소스 라이선스 포함 public 레포, 트랙 선택 |
| 심사 기준 | Technological Implementation / Design / Potential Impact / Quality of the Idea |
| 커뮤니티 | Discord https://discord.gg/7Dqk5ebCD4 |

리소스 페이지는 **Phase 1~5** 구조로 되어 있다.
Phase 1 코어 프레임워크 → Phase 2 액션·데이터 연결 → Phase 3 파트너 통합 →
Phase 4 추론·상태·로직 호스팅 → Phase 5 배포·안전성.

---

## 1. Google Cloud 리소스

### 1-1. Phase 1 — Core Frameworks & Environment

| 리소스 | 설명 | 링크 |
| --- | --- | --- |
| Gemini Enterprise Agent Platform API Setup | Vertex AI 계열의 매니지드 에이전트 플랫폼. API 활성화·프로젝트 세팅의 출발점 | https://cloud.google.com/vertex-ai/docs |
| Agent Builder Guide (Low-Code) | Dialogflow CX 기반 Agent Builder. 코드 없이 대화형 에이전트 골격을 잡는 경로 | https://cloud.google.com/dialogflow/cx/docs/concept/agent |
| Gemini Enterprise Agent Platform SDK for Python | `google-genai` 파이썬 SDK 저장소. Gemini 호출·툴 정의의 표준 진입점 | https://github.com/googleapis/python-genai |
| Agent Starter Pack / Agent Engine 입문 노트북 | Agent Engine에 에이전트를 올리는 최소 예제 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/intro_agent_engine.ipynb |

**설치 커맨드 (공식 안내)**

```bash
pip install "google-cloud-aiplatform[agent_engines,adk]>=1.101.0"
```

### 1-2. Phase 2 — Action Mechanisms & Data Connectivity

**스크립트 처리 & 문서 그라운딩**

| 리소스 | 미디어/엔터 활용 아이디어 | 링크 |
| --- | --- | --- |
| Document Processing Guide | 각본(PDF/Final Draft), 계약서, 콜시트 파싱 → 구조화 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/document_processing.ipynb |
| RAG with BigQuery + Feature Store | 대본 아카이브·IP 라이브러리 위에 RAG 구축 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/retrieval-augmented-generation/rag_qna_with_bq_and_featurestore.ipynb |
| Agent Builder Data Stores / Grounding Overview | 그라운딩 개념·데이터스토어 구성 | https://cloud.google.com/vertex-ai/docs/generative-ai/grounding/overview |

**비디오 분석 & VFX**

| 리소스 | 활용 아이디어 | 링크 |
| --- | --- | --- |
| Multimodal Use Cases | 러시 푸티지 분석, 샷 분류 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/intro_multimodal_use_cases.ipynb |
| Multimodal Video Transcription | 촬영본 자동 전사, 대사/씬 로그 생성 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/multimodal_video_transcription.ipynb |
| Video Captioning (data curation) | 자막·메타데이터 자동 생성, 아카이브 검색용 캡션 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/multimodal-data-curation/captioning.ipynb |
| Imagen 3 Image Generation | "VFX 무드보드, 콘셉트 아트, 스토리보드 패널을 텍스트 프롬프트로 생성" (공식 문구) | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb |

> 참고: 리소스 페이지에 **Veo는 명시적으로 등장하지 않는다.** 이미지 생성은 Imagen 3,
> 음악은 Lyria 3로 안내된다. Veo를 쓰고 싶다면 Vertex AI 공식 문서를 직접 참조해야 한다.

**오디오 & 스피치 생성**

| 리소스 | 활용 아이디어 | 링크 |
| --- | --- | --- |
| Lyria 3 Music Generation | "고품질 음악 클립, 사운드트랙, 효과음 생성" — 예고편 음악, 씬별 스코어 스케치 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/music/getting-started/lyria3_music_generation.ipynb |
| Gemini 3.1 Flash TTS | 대사 프리비즈, 오디오 더빙 프로토타입 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/getting-started/gemini_3_1_flash_tts.ipynb |
| Multi-Speaker Podcast | 다화자 테이블 리드(table read) 자동 생성 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/use-cases/podcast/multi-speaker-podcast.ipynb |
| Dialogue Sentiment Analysis | 대본 감정 곡선 분석, 캐릭터 톤 일관성 검사 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/multimodal-sentiment-analysis/intro_to_multimodal_sentiment_analysis.ipynb |

### 1-3. Phase 4 — Reasoning, State & Logic Hosting (ADK / Agent Engine)

| 리소스 | 설명 | 링크 |
| --- | --- | --- |
| Introduction to Agent Engine | 매니지드 에이전트 런타임 기본 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/intro_agent_engine.ipynb |
| Deploying ADK Agents on Agent Engine | ADK 에이전트를 Agent Engine에 배포하는 튜토리얼 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_deploy_your_first_adk_agent_on_agent_engine.ipynb |
| Live API Streaming on Agent Engine | 양방향 저지연 음성. **"인터랙티브 스크립트 리허설"**을 공식 예시로 제시 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_live_api_on_agent_engine.ipynb |
| Google Maps Agent | 외부 API 툴 연동 패턴 (로케이션 스카우팅에 직결) | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/tutorial_google_maps_agent.ipynb |
| MCP Toolbox for Databases | "MCP로 SQL DB를 안전하게 질의" — ClickHouse 트랙과 궁합 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/tutorial_mcp_toolbox_for_databases.ipynb |

**Function Calling**

- Introduction to Function Calling — https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb
- Forced Function Calling — https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/forced_function_calling.ipynb
- Multimodal Function Calling — https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/multimodal_function_calling.ipynb

### 1-4. Phase 5 — Deployment & Safety

| 리소스 | 설명 | 링크 |
| --- | --- | --- |
| Agent Builder Deployment (버전/환경) | 에이전트 버전 관리·환경 승격 | https://cloud.google.com/dialogflow/cx/docs/concept/version |
| Cloud Run Quickstart | 컨테이너 배포. 제출 요건인 "호스팅된 프로젝트 URL" 확보 경로 | https://cloud.google.com/run/docs/quickstarts |
| Secret Manager | 파트너 API 키(Parallel, ClickHouse, Grafana 토큰) 보관 | https://cloud.google.com/secret-manager/docs |
| Gemini Safety Settings | 생성물 안전성 필터 설정 | https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb#Safety-Settings |

### 1-5. Google Cloud 크레딧 수령 방법

1. **무료 체험**: https://cloud.google.com/free — 신규 계정 대상 기본 무료 크레딧/무료 등급.
2. **해커톤 전용 $100 크레딧**: https://forms.gle/XPe837tzogh8L5sX6
   - 공식 문구: 승인까지 **"1–5 business days, while supplies last"**.
   - 재고 소진 시 마감되므로 **가장 먼저 신청해야 하는 항목**.
3. 크레딧은 Vertex AI / Gemini API / Cloud Run / BigQuery 등 GCP 전반에 사용.

> 실무 팁: $100은 Veo/Imagen 같은 미디어 생성 모델을 마구 돌리기엔 빠듯하다.
> 데모 영상용 생성물은 **미리 캐싱**해 두고, 라이브 데모에서는 텍스트/검색 경로 위주로 태우는 게 안전하다.

### 1-6. ADK (Agent Development Kit) — 별도 정리

공식 사이트: https://adk.dev/ (구 https://google.github.io/adk-docs/ 에서 리다이렉트)

- **언어**: Python, TypeScript, Go, Java, Kotlin
- **에이전트 타입**: 단순 LLM 에이전트, 매니지드 에이전트, 멀티 에이전트 워크플로(sequential / loop / parallel / collaborative)
- **툴**: 커스텀 function tool, **MCP tool**, OpenAPI tool, Google Search 등 빌트인
- **컨텍스트 관리**: "컨텍스트를 소스코드처럼 다룬다" — 자동 필터링·요약·토큰 최적화
- **Graph Workflows (ADK 2.0)**: 결정론적 로직 + LLM 추론을 그래프로 결합
- **세션/메모리/상태**: 대화 컨텍스트, state 관리, 메모리, 컨텍스트 압축
- **모델**: Gemini 외 Claude, OpenAI, Ollama 어댑터 지원
- **배포**: 로컬 컨테이너, Agent Runtime, Cloud Run, GKE
- **평가**: 빌트인 criteria, user simulation, 커스텀 메트릭
- **DX**: Agents CLI 스캐폴딩, web UI, 비주얼 빌더

### 1-7. Agent Starter Pack (강력 추천)

https://github.com/GoogleCloudPlatform/agent-starter-pack

```bash
uvx agent-starter-pack create      # 신규 생성
uvx agent-starter-pack enhance     # 기존 에이전트에 인프라 얹기
```

포함 템플릿 6종:

| 템플릿 | 내용 | 이 해커톤에서의 쓸모 |
| --- | --- | --- |
| `adk` | ADK 기반 ReAct 에이전트 | 기본 뼈대 |
| `adk_a2a` | ADK + **Agent2Agent(A2A) 프로토콜** | 멀티 에이전트 네트워크 요건 충족용 |
| `agentic_rag` | 문서 검색·QA 에이전트 | 대본/IP 아카이브 RAG |
| `langgraph` | LangGraph ReAct | LangChain 생태계 선호 시 |
| `adk_java` | Java ReAct | — |
| `adk_live` | 오디오/비디오/텍스트 멀티모달 RAG | **미디어 트랙에 가장 잘 맞음** |

기본 제공 인프라: Cloud Build 또는 GitHub Actions CI/CD, 관측성, Vertex AI 평가 프레임워크 +
인터랙티브 플레이그라운드, Terraform 기반 RAG 데이터 인제스천 파이프라인.
배포 타깃은 **Cloud Run**과 **Agent Engine**.

> 시간이 없다면 `uvx agent-starter-pack create` 로 `adk_a2a` 또는 `adk_live`를 뽑아
> 파트너 MCP 서버만 붙이는 게 최단 경로다.

---

## 2. 파트너별 리소스

각 트랙은 **런타임에 실제로 그 파트너 서비스를 호출**해야 한다.
README에 이름만 적는 것은 인정되지 않는다 (공식 문구: *"imported and called in code, not just named in README"*).

### 2-1. IBM

파트너 페이지: https://agentic-cinema.devpost.com/details/ibm-resources

**필수 요건**: 프로젝트가 **IBM Bob을 개발 과정의 일부로 사용**해야 한다.
Bob 사용이 없으면 IBM 트랙 자격이 없다.

| 리소스 | 링크 |
| --- | --- |
| IBM Bob 소개 영상 | https://www.youtube.com/watch?v=JKnxSiTlvs8 |
| Quick Start Tutorial | https://bob.ibm.com/docs/ide/getting-started/quickstart |
| Best Practices Guide | https://bob.ibm.com/docs/ide/getting-started/best-practices |
| Trial 신청 | http://bob.ibm.com/trial |
| Confluent (선택, 강력 권장) | https://www.confluent.io/get-started/ |

**IBM Bob이란**
- "AI software development lifecycle (SDLC) partner" — 확장 프로그램이 아니라 **독립 실행형 IDE 앱**
- 모드: `Ask`(읽기 전용) / `Agent`(승인 기반 코드 수정) / `Plan`(계획 수립)
- 승인 워크플로: auto-approve 설정 가능, 실행 전 계획 리뷰
- 요구사항: Bob 앱 다운로드 + Docker(또는 Podman) + Git
- 특징: 로컬에 의존성 설치 없이 컨테이너 안에서 빌드/실행

**Confluent** — 선택이지만 "실시간 데이터·이벤트 기반 워크플로"에 강력 권장.
Kafka 기반 스트리밍으로 프로덕션 이벤트(대본 리비전, 렌더 잡 완료, 촬영 로그)를
에이전트 트리거로 연결하는 그림이 자연스럽다.

**무료 tier**: 별도 크레딧 안내 없음. Bob은 trial 링크로, Confluent는 자체 free trial로 접근.

**활용 아이디어**
- Bob으로 코드베이스 전체를 에이전트가 스캐폴딩 → 개발 과정 자체를 데모 영상에 담기 (요건 충족 + 스토리텔링)
- Confluent 토픽에 "촬영 현장 이벤트" 스트림을 흘리고, Gemini 에이전트가 실시간으로 콜시트를 리플랜

> 주의: IBM 트랙은 "Bob으로 만들었다"는 **개발 프로세스 증빙**이 핵심이라,
> 다른 트랙보다 데모 영상 구성이 달라진다. 개발 화면 녹화를 미리 확보해 둘 것.

### 2-2. Grafana Labs

파트너 페이지: https://agentic-cinema.devpost.com/details/grafana-resources

**핵심 제공물**: **Grafana Cloud MCP Server** — "60+ tools your Gemini agent can call to
query metrics, logs, and traces, search dashboards, and manage alerts and incidents."

| 리소스 | 링크 |
| --- | --- |
| Grafana Cloud 무료 계정 | https://grafana.com/products/cloud/ |
| 계정 생성 안내 | https://grafana.com/docs/grafana-cloud/get-started/create-account/ |
| **호스팅 MCP 엔드포인트** | `https://mcp.grafana.com/mcp` |
| Cloud MCP 설정 문서 | https://grafana.com/docs/grafana-cloud/machine-learning/assistant/configure/cloud-mcp/ |
| **ADK ↔ Grafana Cloud 통합 예제** | https://github.com/google/adk-docs/blob/main/docs/integrations/grafana-cloud.md |
| 오픈소스 Grafana MCP 서버 | https://grafana.com/docs/grafana/latest/developer-resources/mcp/ |
| MCP Introduction | https://grafana.com/docs/grafana/latest/developer-resources/mcp/introduction/ |
| MCP Configuration | https://grafana.com/docs/grafana/latest/developer-resources/mcp/configure/ |
| 클라이언트 설정 예제 | https://grafana.com/docs/grafana/latest/developer-resources/mcp/set-up/client-configuration-examples/ |
| Loki / LogQL | https://grafana.com/docs/loki/latest/query/ |
| Mimir (metrics) | https://grafana.com/docs/mimir/latest/ |
| Tempo (traces) | https://grafana.com/docs/tempo/latest/ |
| AI Observability 개요 | https://grafana.com/docs/grafana-cloud/machine-learning/ai-observability/ |
| AI Observability SDK 시작 (Python/TS/Go/Java/.NET) | https://grafana.com/docs/grafana-cloud/machine-learning/ai-observability/get-started/ |
| MCP 서버 모니터링 블로그(OpenLIT) | https://grafana.com/blog/ai-observability-MCP-servers/ |
| Google 측 MCP tool 설정 | https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/mcp |
| Agent Platform remote MCP | https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/use-agent-platform-mcp |

**시작 절차 (공식)**
1. Grafana Cloud 무료 계정 생성
2. Stack 관리자가 Grafana Assistant 약관 1회 수락
3. MCP 접근에는 **Editor 이상 role** 필요
4. 브라우저를 통한 **OAuth 2.1** 인가

**오픈소스 MCP 서버** (https://github.com/grafana/mcp-grafana)
- 툴 카테고리: 대시보드(검색/조회/수정/패치), 데이터소스 조회·질의, Prometheus/Loki/InfluxDB/ClickHouse/CloudWatch/Elasticsearch 질의, 알림 룰·컨택트 포인트, Incident 생성·추적, OnCall 스케줄·시프트, annotation·snapshot, **패널 이미지 렌더링**, Pyroscope 프로파일링, Sift 조사(에러 패턴 탐지), Agent Observability(대화 추적)
- 인증: `GRAFANA_SERVICE_ACCOUNT_TOKEN` (또는 `..._FILE`). 구 `GRAFANA_API_KEY`는 deprecated
- 설치: `uvx` / Docker(`-t stdio`) / 바이너리 / Helm chart / Go 빌드
- 플래그: `--disable-write`(읽기 전용), `--disable-query`, `--enabled-tools`(admin·Snowflake·Athena·ClickHouse 등 기본 비활성 툴 활성화)

**무료 tier**: Grafana Cloud Free — metrics, logs, traces, dashboards, alerting 포함.
파트너 페이지에는 구체적 한도가 명시되어 있지 않다.

**활용 아이디어 (미디어/엔터)**
- **렌더팜 / VFX 파이프라인 옵저버빌리티 에이전트**: 렌더 잡 메트릭을 Mimir에 넣고,
  에이전트가 "왜 이 샷 렌더가 느린가"를 Loki 로그 + Tempo 트레이스로 자동 조사 → Incident 생성
- **스트리밍 QoE 에이전트**: CDN/플레이어 메트릭 이상 탐지 → 자연어 사후 분석 리포트 + 대시보드 패널 이미지 첨부
- **에이전트 자체 관측**: AI Observability SDK로 Gemini 에이전트의 토큰/지연/툴 호출을 계측 →
  "자기 자신을 모니터링하는 에이전트" 데모. 심사 기준의 Technological Implementation에 유리
- 패널 렌더링 툴로 **에이전트가 만든 그래프 이미지를 데모 영상에 그대로 노출** 가능

### 2-3. Parallel (Parallel Web Systems)

파트너 페이지: https://agentic-cinema.devpost.com/details/parallel-resources

**소개**: "Parallel develops web infrastructure for AI agents" — 자체 크롤링·인덱싱부터
검색, 추출, 추론, 모니터링까지 수직 통합된 스택.

**필수 요건**: **Search API를 런타임에 실제 사용**. 허용 방식:
- 공식 `parallel-web` SDK (Python / TypeScript)
- 지원 통합: Vercel AI SDK의 `@parallel-web/ai-sdk-tools`, LangChain의 `ParallelWebSearchTool`
- Parallel Web Search를 통한 **grounding 설정**

| 리소스 | 링크 |
| --- | --- |
| Search API Quickstart | https://docs.parallel.ai/search/search-quickstart |
| Extract API (URL 콘텐츠 추출) | https://docs.parallel.ai/extract/extract-quickstart |
| Task API (대량 웹 데이터 인리치먼트) | https://docs.parallel.ai/task-api/task-quickstart |
| Monitor API (웹 모니터링·알림) | https://docs.parallel.ai/monitor-api/monitor-quickstart |
| Parallel CLI | https://docs.parallel.ai/integrations/cli |
| Search & Extract MCP Server | https://docs.parallel.ai/integrations/mcp/search-mcp |
| **Gemini Enterprise 통합 가이드** | https://docs.parallel.ai/integrations/google-gemini-enterprise |
| **Google 측 Grounding with Parallel** | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-parallel |
| Playground / 로그인 | https://platform.parallel.ai/login?redirectTo=%2F |
| 회사 소개 | http://parallel.ai |
| Free tier 안내 | https://parallel.ai/blog/free-tier-parallel |
| 지원 | support@parallel.ai |

**크레딧 / 무료 tier**
- 가입 시 **자동으로 $20–$80 크레딧** 지급 (이메일 종류, 지역 등에 따라 차등)
- 추가로 카드 등록 시 **매월 $5 리커링 크레딧** (실제 청구 없음)
- $5로 커버되는 양: Search API 5,000회 / Extract API 5,000회 / Task API 1,000 run / Monitor API 1,666회
- 조건: 카드 1장당 조직 1개, marketplace·postpaid 조직은 제외. 미사용 크레딧은 월말 소멸
- 요청마다 **선불로 비용을 산정**해 실행 전에 가격을 알 수 있음

**Search API 핵심**
- 자연어 `objective` + `search_queries` 리스트를 한 번에 던지고 LLM 최적화된 excerpt를 받음
- 모드: `advanced`(~3s, 최고 품질) / `fast`(~700ms) / `basic` / `turbo`(~200ms)
- 응답: title, url, excerpt + search id, usage 메타데이터

**Gemini Enterprise 그라운딩 통합 (가장 점수 잘 나오는 경로)**

두 가지 경로: Google Cloud Marketplace 구독(자동 인증·통합 과금·ZDR 옵션) 또는 BYOK(API 키 직접 전달).

```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Your query here",
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            parallel_ai_search=types.ToolParallelAiSearch(
                custom_configs={"mode": "basic", "max_results": 10}
            )
        )]
    ),
)
```

파라미터: `mode`("basic"/"advanced"), `max_results`(1–20, 기본 10), `source_policy`(도메인 필터), `excerpts`(길이 제어).
응답의 `groundingMetadata`에 검색 쿼리·출처 인용·근거 매핑이 담긴다.

**활용 아이디어 (미디어/엔터)**
- **박스오피스·경쟁작 리서치 에이전트**: Search API로 트레이드지(Variety, Deadline, THR) 실시간 그라운딩 → 개봉일 배치 시뮬레이션
- **캐스팅/탤런트 인텔리전스**: Task API로 배우 필모·수상·SNS 화제성을 구조화 스키마로 대량 인리치먼트
- **IP 권리·유사작 클리어런스 스캔**: Extract API로 원작 관련 페이지 본문을 뽑아 표절/유사성 리스크 브리핑
- **Monitor API로 개봉 후 여론 모니터링**: 리뷰 어그리게이터·SNS 변동 감지 → 마케팅 에이전트 트리거
- `source_policy`로 신뢰 도메인만 화이트리스트 → 심사에서 "hallucination 대응"을 어필

### 2-4. ClickHouse

파트너 페이지: https://agentic-cinema.devpost.com/details/clickhouse-resources

**소개**: "one of the fastest and most resource-efficient real-time databases and data warehouses."

**필수 요건**: 공식 **MCP 서버(`mcp-clickhouse`)를 통해 런타임에 ClickHouse를 실제 사용**.
ClickHouse Cloud 또는 self-hosted 클러스터 모두 가능.
개발 중 **ClickHouse Agent Skills** 사용은 선택이지만 권장.

| 리소스 | 링크 |
| --- | --- |
| **크레딧 포함 가입 링크** | https://console.clickhouse.cloud/signUp?promo=SIGNUP100 |
| AgentHouse 데모 (chat-with-data, Google 로그인 필요) | https://llm.clickhouse.com/login |
| 공식 MCP 서버 | https://github.com/ClickHouse/mcp-clickhouse |
| 예제 저장소 (LangChain / LlamaIndex / DSPy 통합) | https://github.com/ClickHouse/examples |
| SQL Playground (공개 데이터셋) | ClickHouse 문서 내 SQL Playground |

**크레딧**: 신규 계정에 **ClickHouse Cloud 크레딧 $400**.
위 promo 링크(`?promo=SIGNUP100`)로 가입해야 적용된다.

**mcp-clickhouse 상세**
- MCP `2026-07-28` 스펙 구현, 레거시 initialize 핸드셰이크도 지원
- 노출 툴:
  - `run_query` — SQL 실행 (기본 **read-only**)
  - `list_databases` — DB 목록
  - `list_tables` — 페이지네이션·필터·컬럼 메타데이터 옵션
  - `run_chdb_select_query` — chDB 임베디드 엔진으로 파일/URL/DB 직접 질의
  - `/health` 엔드포인트 (200 OK)
- 설치: `pip install mcp-clickhouse` (chDB 포함 시 `pip install 'mcp-clickhouse[chdb]'`)
- 주요 환경변수:
  ```
  CLICKHOUSE_HOST / CLICKHOUSE_USER / CLICKHOUSE_PASSWORD
  CLICKHOUSE_SECURE / CLICKHOUSE_VERIFY        # DB 쪽 TLS (MCP transport 아님)
  CLICKHOUSE_MCP_AUTH_TOKEN 또는 FASTMCP_SERVER_AUTH   # HTTP/SSE transport 시 필수
  CLICKHOUSE_ALLOW_WRITE_ACCESS / CLICKHOUSE_ALLOW_DROP  # 쓰기 허용
  ```
- transport: stdio(기본) / HTTP / SSE. 미들웨어로 툴 호출 로깅·인증·요청별 설정 오버라이드 가능

**ClickHouse Agent Skills**: 스키마 설계, 쿼리 최적화, 데이터 인제스천 패턴을 다루는 스킬을
CLI로 설치해 개발 중 활용 가능 (제출 요건은 아님).

**활용 아이디어 (미디어/엔터)**
- **"에이전트의 기억(The Agent's Memory)"** — 워크숍 제목 그대로, ClickHouse를 에이전트의 장기 메모리·이벤트 저장소로 사용
- **스트리밍 시청 로그 분석 에이전트**: 수십억 행의 재생 이벤트 위에서 자연어 질의 → 이탈 지점, 완주율, 코호트 분석
- **박스오피스/EPG 실시간 대시보드 에이전트**: 상영관별 좌석·매출 이벤트를 실시간 집계
- **미디어 자산 카탈로그**: 샷 메타데이터(Gemini가 뽑은 캡션·태그)를 ClickHouse에 적재 → 초고속 시맨틱+구조 검색
- **Grafana와 결합**: Grafana MCP의 ClickHouse 질의 툴을 켜면 두 파트너 스택을 한 번에 태울 수 있다(단, 트랙은 하나만 선택)

### 2-5. Replit

파트너 페이지: https://agentic-cinema.devpost.com/details/replit-resources

**필수 요건**
- **Replit Agent를 개발 과정의 일부로 사용**
- **Replit에 직접 배포** (`replit.app` 또는 `replit.dev` 도메인)

| 리소스 | 링크 |
| --- | --- |
| Replit 리소스 문서 (Google Drive PDF) | https://drive.google.com/file/d/1dgNQnlqpOZCkuM4SqCBo2xrbX6DSwFhD/view?usp=sharing |
| **크레딧 코드 신청 폼** | https://forms.gle/pwwvgDvbkgiRpADm6 |

**크레딧 / 자격**
- **$20 크레딧 코드** — Core tier 구독 첫 달 커버
- **신규 Replit 사용자만 해당.** 기존 계정이 있으면 코드가 사용 불가
- 카드 등록은 필요하지만 크레딧 기간 중에는 청구되지 않음
- 크레딧 소진/만료 후에도 앱이 자동으로 unpublish 되지는 않음

**활용 아이디어**
- Replit Agent로 프론트엔드 + Gemini 백엔드를 통째로 스캐폴딩 → 배포까지 한 플랫폼에서 종결
- "호스팅된 프로젝트 URL" 제출 요건을 가장 마찰 없이 충족하는 트랙
- 미디어 팀용 **노코드 지향 내부 툴**(콜시트 생성기, 대본 브레이크다운 뷰어)을 Replit에 올리는 시나리오가 자연스럽다

> 주의: 5개 트랙 중 진입 장벽이 가장 낮아 **경쟁이 몰릴 가능성**이 높다.
> 반대로 Grafana/ClickHouse처럼 인프라 색이 강한 트랙은 미디어 도메인 서사를 잘 짜면 차별화가 쉽다.

---

## 3. 워크숍 · 이벤트 일정

모두 **이미 종료**되었고, 녹화본이 Updates 페이지에 게시되어 있다.
녹화 링크는 https://agentic-cinema.devpost.com/updates 의 "Build Session Recordings" 공지에서 확인.

| 날짜 (2026) | 파트너 | 세션명 |
| --- | --- | --- |
| 8/17 11:00 AM ET | IBM | Build Faster with IBM Bob: AI-Assisted Coding for Hackathon Teams |
| 8/18 11:00 AM ET | ClickHouse | The Agent's Memory: Powering Real-Time AI Workflows with ClickHouse |
| 8/23 11:30 AM ET | Grafana | Premiere Night — Build an Observability Agent with Grafana Cloud MCP |
| 8/23 12:30 PM ET | Parallel | Getting Started with Parallel: Build a Web-Grounded Gemini Agent |
| 8/24 12:00 PM ET | Replit | Replit Live Build Session (제출 마무리 + Q&A) |

**기타 일정**
- 챌린지 런칭: 약 1개월 전. 5개 파트너 트랙 + 총 $75,000 공개
- "Final Call for Submissions" 공지 게시 (마감 3일 전)
- **최종 제출 마감: 2026년 9월 9일 오후 2:00 PDT**

> 별도의 상시 office hours는 공지되지 않았다. 실시간 질의는 Discord와 Discussion Forum이 전부다.

---

## 4. 스타터 키트 · 샘플 코드

### 4-1. 최우선 스타터

| 항목 | 링크 | 비고 |
| --- | --- | --- |
| **Agent Starter Pack** | https://github.com/GoogleCloudPlatform/agent-starter-pack | `uvx agent-starter-pack create` 한 방. CI/CD·관측성·평가 포함 |
| **GoogleCloudPlatform/generative-ai** | https://github.com/GoogleCloudPlatform/generative-ai | 리소스 페이지의 노트북 대부분이 이 레포 소속. 통째로 클론해두면 편함 |
| **googleapis/python-genai** | https://github.com/googleapis/python-genai | Gemini Python SDK |

### 4-2. 파트너 MCP 서버 / 예제

| 항목 | 링크 |
| --- | --- |
| ClickHouse 공식 MCP 서버 | https://github.com/ClickHouse/mcp-clickhouse |
| ClickHouse 예제 (LangChain / LlamaIndex / DSPy) | https://github.com/ClickHouse/examples |
| Grafana MCP 서버 (OSS) | https://github.com/grafana/mcp-grafana |
| Grafana 호스팅 MCP 엔드포인트 | https://mcp.grafana.com/mcp |
| ADK ↔ Grafana Cloud 통합 문서 | https://github.com/google/adk-docs/blob/main/docs/integrations/grafana-cloud.md |
| Parallel Search & Extract MCP | https://docs.parallel.ai/integrations/mcp/search-mcp |
| Parallel CLI | https://docs.parallel.ai/integrations/cli |

### 4-3. 노트북 체크리스트 (미디어 프로젝트 기준 우선순위)

1. `intro_agent_engine.ipynb` — 배포 뼈대
2. `tutorial_deploy_your_first_adk_agent_on_agent_engine.ipynb` — ADK 배포
3. `intro_function_calling.ipynb` — 툴 호출 기본
4. `tutorial_mcp_toolbox_for_databases.ipynb` — MCP로 DB 붙이기 (ClickHouse 트랙 필수급)
5. `intro_multimodal_use_cases.ipynb` + `multimodal_video_transcription.ipynb` — 영상 이해
6. `intro_gemini_3_image_gen.ipynb` — Imagen 3 스토리보드/콘셉트 아트
7. `lyria3_music_generation.ipynb` — 음악
8. `multi-speaker-podcast.ipynb` — 다화자 TTS(테이블 리드)
9. `tutorial_get_started_with_live_api_on_agent_engine.ipynb` — 실시간 음성 리허설

### 4-4. 데모/참고 서비스

- **AgentHouse** (ClickHouse chat-with-data 라이브 데모): https://llm.clickhouse.com/login
- **Parallel Playground**: https://platform.parallel.ai/login?redirectTo=%2F
- **ClickHouse SQL Playground**: 공개 데이터셋으로 스키마 실험

---

## 5. 커뮤니티 채널

| 채널 | 링크 | 용도 |
| --- | --- | --- |
| **해커톤 Discord** | https://discord.gg/7Dqk5ebCD4 | 참가자·스폰서 실시간 소통. 1순위 |
| Devpost Discussion Forum | https://agentic-cinema.devpost.com/forum_topics | 공식 Q&A, 주최 측 답변이 기록으로 남음 |
| Updates 페이지 | https://agentic-cinema.devpost.com/updates | 공지·녹화본 |
| Project Gallery | https://agentic-cinema.devpost.com/project-gallery | 경쟁작 정찰 |
| Participants | https://agentic-cinema.devpost.com/participants | 팀 빌딩 |
| Grafana Community Forum | https://community.grafana.com/ | Grafana 기술 질문 |
| Grafana Community Slack | https://slack.grafana.com/ | 〃 |
| Grafana Help Center | https://grafana.com/help/ | 〃 |
| Parallel Support | support@parallel.ai | Parallel 기술 지원 |
| Devpost 공식 Discord | https://discord.com/invite/HP4BhW3hnp | 플랫폼 일반 문의 |
| Devpost Help Desk | https://help.devpost.com/ | 제출 관련 문제 |

---

## 6. 기술 스택 추천 조합 (트랙별)

### 6-0. 모든 트랙 공통 베이스

```
[Frontend]  Cloud Run 또는 Replit 호스팅 (제출 요건: 호스팅된 URL)
     ↕
[Agent]     ADK (Python) + Gemini
            └ Agent Engine 또는 Cloud Run 배포
            └ Function Calling + MCP tools
     ↕
[Data]      Cloud Storage(원본 미디어) + BigQuery 또는 파트너 DB
[Secrets]   Secret Manager (파트너 API 키)
[Safety]    Gemini Safety Settings
```

부트스트랩: `uvx agent-starter-pack create` → 템플릿 `adk_a2a`(멀티 에이전트) 또는 `adk_live`(멀티모달).

### 6-1. IBM 트랙 — "실시간 프로덕션 오케스트레이션"

| 레이어 | 선택 |
| --- | --- |
| 개발 도구 | **IBM Bob** (필수, 개발 프로세스 증빙) |
| 이벤트 스트림 | **Confluent Cloud** (Kafka) |
| 에이전트 | ADK 멀티 에이전트 (A2A) + Gemini |
| 배포 | Cloud Run |
| 미디어 | Gemini 멀티모달 (촬영 로그 분석), Imagen 3 |

**시나리오 예시** — *Production Control Room Agent*:
현장 이벤트(씬 완료, 장비 이슈, 날씨 변화)를 Confluent 토픽으로 흘리고,
Scheduler / Budget / Logistics 세 개 서브에이전트가 A2A로 협의해 콜시트를 실시간 리플랜.
전 과정을 IBM Bob으로 개발하고 그 화면을 데모에 삽입.

### 6-2. Grafana 트랙 — "미디어 파이프라인 SRE 에이전트"

| 레이어 | 선택 |
| --- | --- |
| 관측성 | **Grafana Cloud MCP** (`https://mcp.grafana.com/mcp`, OAuth 2.1) |
| 텔레메트리 | Mimir(메트릭) / Loki(로그) / Tempo(트레이스) |
| 에이전트 계측 | **Grafana AI Observability SDK** (에이전트 자기 관측) |
| 에이전트 | ADK + Gemini, MCP tool로 60+ Grafana 툴 호출 |
| 부가 | Sift 조사, Incident 생성, 패널 이미지 렌더링 |

**시나리오 예시** — *Render Farm / Streaming QoE Agent*:
렌더 잡·트랜스코딩 큐·CDN 지표를 Grafana Cloud에 넣고, 이상 발생 시 에이전트가
LogQL·TraceQL로 근본 원인을 추적 → Incident 생성 → 패널 이미지를 붙인 자연어 포스트모템 발행.
동시에 AI Observability SDK로 **에이전트 자신의 추론 비용·지연**을 같은 대시보드에 노출.

> 차별화 포인트: "옵저버빌리티 에이전트가 스스로도 관측된다"는 재귀 구조는
> Technological Implementation 점수를 확실히 끌어올린다.

### 6-3. Parallel 트랙 — "웹 그라운디드 인텔리전스"

| 레이어 | 선택 |
| --- | --- |
| 웹 그라운딩 | **Parallel Search API** (Gemini `parallel_ai_search` 툴로 네이티브 그라운딩) |
| 심층 추출 | Extract API |
| 대량 인리치먼트 | Task API |
| 변화 감지 | Monitor API |
| 에이전트 | Gemini Enterprise Agent Platform 그라운딩 + ADK |
| 신뢰성 | `source_policy` 도메인 화이트리스트 + `groundingMetadata` 인용 UI |

**시나리오 예시** — *Greenlight Intelligence Agent*:
기획안을 넣으면 Search API로 유사 IP·경쟁작·시장 반응을 실시간 조사,
Task API로 배우/감독 필모그래피를 구조화, Monitor API로 경쟁작 개봉일 변경을 감시,
Gemini가 종합해 **인용 각주가 달린 그린라이트 메모**를 생성.

> 크레딧이 가장 넉넉하다($20–80 + 월 $5). Search 5,000콜이면 해커톤 규모에선 충분.
> Google 공식 `grounding-with-parallel` 경로를 쓰면 "두 스폰서를 네이티브로 결합"했다는 서사가 깔끔하다.

### 6-4. ClickHouse 트랙 — "에이전트의 기억"

| 레이어 | 선택 |
| --- | --- |
| 저장소 | **ClickHouse Cloud** ($400 크레딧, `?promo=SIGNUP100`) |
| 접근 | **mcp-clickhouse** MCP 서버 (read-only 기본) |
| 에이전트 | ADK + Gemini, MCP Toolbox for Databases 패턴 |
| 인제스천 | Gemini 멀티모달로 영상→샷 메타데이터 추출 후 ClickHouse 적재 |
| 개발 보조 | ClickHouse Agent Skills (스키마 설계·쿼리 최적화) |

**시나리오 예시** — *Studio Analytics Agent*:
(1) Gemini가 영상 아카이브를 캡셔닝·태깅 → ClickHouse `shots` 테이블 적재
(2) 시청/박스오피스 이벤트 수억 행을 같은 클러스터에 적재
(3) 프로듀서가 자연어로 질문 → 에이전트가 `run_query`로 SQL 생성·실행 → 즉답
(4) 대화 이력·툴 호출 로그도 ClickHouse에 써서 **에이전트의 장기 메모리**로 재활용

> 안전장치: `CLICKHOUSE_ALLOW_WRITE_ACCESS`를 끄고 read-only로 시연하되,
> 메모리 쓰기는 별도 인증된 경로로 분리하면 설계 점수에 유리하다.

### 6-5. Replit 트랙 — "빠르게 배포되는 스튜디오 툴"

| 레이어 | 선택 |
| --- | --- |
| 개발 | **Replit Agent** (필수) |
| 호스팅 | **Replit** (`*.replit.app` / `*.replit.dev`, 필수) |
| 에이전트 | Gemini API (`google-genai`) 직접 호출 + ADK |
| 미디어 | Imagen 3 / Lyria 3 / Gemini TTS |
| 크레딧 | Replit $20 + Google Cloud $100 |

**시나리오 예시** — *Script-to-Pitch Deck Agent*:
대본 업로드 → Gemini가 브레이크다운(씬/캐릭터/로케이션) → Imagen 3로 무드보드 →
Lyria 3로 테마 음악 → 다화자 TTS로 핵심 씬 테이블 리드 → 한 페이지 피치덱 웹앱으로 즉시 배포.

> 장점: 마감이 임박했을 때 "호스팅 URL" 요건을 가장 빨리 충족.
> 단점: 진입 장벽이 낮아 유사 제출물이 많을 것. **미디어 도메인 깊이**로 승부해야 한다.

---

## 7. 실행 체크리스트

- [ ] Google Cloud $100 크레딧 폼 제출 (승인 1–5일, 재고 소진 시 종료) — https://forms.gle/XPe837tzogh8L5sX6
- [ ] 트랙 확정 (트랙별 필수 요건이 다름: IBM=Bob 사용, Replit=Replit Agent+Replit 배포, ClickHouse=mcp-clickhouse, Parallel=Search API, Grafana=Cloud MCP)
- [ ] 파트너 크레딧 수령 (ClickHouse `?promo=SIGNUP100` / Parallel 자동 지급 / Replit 신규 계정 폼)
- [ ] `uvx agent-starter-pack create`로 뼈대 생성
- [ ] 파트너 서비스가 **코드에서 import + 호출**되는지 확인 (README 언급만으론 실격)
- [ ] Cloud Run 또는 Replit에 배포하고 public URL 확보
- [ ] public 레포 + **오픈소스 라이선스 파일** 추가
- [ ] 3분 데모 영상 (YouTube/Vimeo, 공개, 영어 또는 영어 자막)
- [ ] Devpost 제출 폼에서 파트너 트랙 선택
- [ ] 마감: **2026-09-09 14:00 PDT**

## 8. 참고 사항 / 주의점

- 리소스 페이지의 일부 링크는 명칭이 최신 브랜딩("Gemini Enterprise Agent Platform")인 반면
  실제 URL은 구 Vertex AI / Dialogflow CX 문서를 가리킨다. 최신 문서는 `docs.cloud.google.com` 쪽을 병행 확인할 것.
- **Veo는 공식 리소스 목록에 없다.** 영상 생성이 필요하면 Vertex AI 문서를 직접 참조하되,
  크레딧 소모가 크므로 사전 생성 후 캐싱 권장.
- Grafana MCP의 강력한 툴(admin, ClickHouse, Snowflake, Athena 등)은 **기본 비활성**이므로
  `--enabled-tools`로 명시적으로 켜야 한다.
- ClickHouse MCP의 HTTP/SSE transport는 `CLICKHOUSE_MCP_AUTH_TOKEN` 없이는 뜨지 않는다.
- Parallel 크레딧은 **미사용분이 월말 소멸**하므로 개발 막판에 몰아쓰지 말 것.
- Replit 크레딧은 **기존 계정에서 사용 불가**. 신규 가입이 필요하면 미리 처리.
