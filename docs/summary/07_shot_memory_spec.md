# 07. Shot Memory — 상세 설계

트랙: **ClickHouse** · 포지셔닝: **"편집 어시스턴트를 위한, 수십만 샷을 자연어로 검색하고 러프컷을 조립하는 에이전트 팀"**

---

## 1. 제품 정의

### 1-1. 타깃 직군
- 1차: 다큐멘터리·장편 편집 어시스턴트 (푸티지 로깅·셀렉트 담당)
- 2차: 방송국·스튜디오 아카이브 담당, 예고편 편집자
- 3차: 유튜브 채널 편집자 (수백 시간 촬영분에서 하이라이트 발췌)

### 1-2. 해결하는 문제
편집 어시스턴트는 촬영분 전체를 보며 로그 시트에 "누가, 어디서, 어떤 샷, 어떤 분위기"를 손으로 적는다. 다큐멘터리는 촬영분 200~500시간이 흔하고 로깅에 수 주가 든다. 편집자가 "비 오는 밤에 두 사람이 마주보는 클로즈업"을 찾으면 어시스턴트가 로그 시트를 뒤져 후보를 골라 오는 데 반나절이 걸린다. 예고편·티저 조립은 이 탐색을 수십 번 반복한다.

### 1-3. 제공 가치 (숫자로 제시할 것)
| 작업 | 현재 | Shot Memory |
| --- | --- | --- |
| 100시간 푸티지 로깅 | 어시스턴트 2~3주 | 배치 인제스트 수 시간 (무인) |
| 조건 검색 1회 | 30분~반나절 | 1초 이내 |
| 60초 티저 초안 | 하루 | 1분 (에이전트 조립) + 편집자 검수 |

### 1-4. 사용자 여정
1. 편집자가 영상 파일(또는 Cloud Storage 버킷 경로)을 등록 → 인제스트 잡 실행
2. 대시보드에 인제스트 진행률과 누적 샷 수 표시
3. 자연어로 검색 → 썸네일 그리드 + 각 샷의 메타데이터 칩 + 에이전트가 만든 SQL 패널
4. 샷을 타임라인에 드래그하거나, "60초 티저, 긴장→해소" 같은 편집 의도를 입력해 자동 조립
5. 연속성 경고(시간대·의상·축 위반) 확인, 샷 교체 승인
6. EDL(CMX3600) 또는 FCPXML 내보내기 → Premiere/Resolve/FCP에서 열기

---

## 2. 아키텍처

```
┌──────────────────────────────────────────────────────────────────────┐
│ Google Cloud                                                          │
│                                                                       │
│  [Cloud Storage]  원본 영상 / 썸네일 / 프록시                          │
│        │                                                              │
│        ▼                                                              │
│  [Cloud Run Job]  Ingest Pipeline (Python)                            │
│    1. 샷 경계 검출 (PySceneDetect ContentDetector)                     │
│    2. 샷별 프록시 클립 + 대표 프레임 3장 추출 (ffmpeg)                  │
│    3. Gemini 3.8 Flash  →  구조화 메타데이터 (response_schema 강제)       │
│    4. Vertex AI multimodalembedding@001  →  1408d 임베딩 (video 모드)   │
│    5. ClickHouse INSERT (clickhouse-connect, 배치 1,000행)             │
│        │                                                              │
│        ▼                                                              │
│  [Cloud Run Service]  Agent App (ADK + FastAPI + Web UI)              │
│    ┌─────────────────────────────────────────────┐                    │
│    │ EditorAssistant (Root LlmAgent)             │                    │
│    │  ├─ Librarian        (LlmAgent)  ──┐        │                    │
│    │  ├─ CutAssembler     (LlmAgent)    │ MCPToolset                  │
│    │  ├─ ContinuityChecker(LlmAgent)    ├──────────► mcp-clickhouse    │
│    │  └─ Narrator         (LlmAgent)  ──┘        │     (stdio)        │
│    └─────────────────────────────────────────────┘        │           │
│    Secret Manager: CLICKHOUSE_PASSWORD, GOOGLE_API_KEY    │           │
└───────────────────────────────────────────────────────────┼───────────┘
                                                            ▼
                                              [ClickHouse Cloud]  shots 테이블
                                              벡터 인덱스 + 메타데이터 컬럼
```

### 2-1. Google Cloud 제품 사용 목록 (README 다이어그램에 박스로 명시)
| 제품 | 용도 | 런타임 여부 |
| --- | --- | --- |
| Google ADK (`google-adk`) | 멀티에이전트 오케스트레이션, MCPToolset | 런타임 |
| Gemini 3.8 Flash / 3.1 Pro (`google-genai`) | 샷 메타데이터 추출, 편집 의도 해석, 연속성 판단 | 런타임 + 인제스트 |
| Vertex AI Multimodal Embeddings (`google-cloud-aiplatform`) | 샷 임베딩, 질의 임베딩 | 런타임 + 인제스트 |
| Cloud Run Service | 에이전트 앱 + UI 호스팅 | 런타임 |
| Cloud Run Jobs | 배치 인제스트 | 인제스트 |
| Cloud Storage | 원본·프록시·썸네일 | 런타임 |
| Secret Manager | 자격증명 | 런타임 |

### 2-2. ClickHouse 사용 방식
- **저장**: `shots` 테이블에 샷당 1행. 임베딩은 `Array(Float32)` 컬럼, 메타데이터는 타입 컬럼.
- **검색**: `cosineDistance(embedding, {q})` 기반 ANN + 메타데이터 `WHERE` 필터를 한 쿼리로 결합하는 하이브리드 검색.
- **런타임 결합**: 에이전트는 **mcp-clickhouse의 `run_query`**로만 ClickHouse에 접근한다. 직접 드라이버 호출은 인제스트 잡에만 쓴다. 이 분리가 "MCP로 런타임 결합"을 코드로 증명한다.
- **장기 기억**: 검색 이력·조립된 시퀀스·편집자 승인 로그를 `sessions`, `sequences` 테이블에 적재해 에이전트가 이전 선택을 참조한다.

---

## 3. 데이터 모델

### 3-1. ClickHouse 스키마

```sql
CREATE TABLE shots
(
    film_id          LowCardinality(String),
    film_title       String,
    shot_id          String,
    shot_index       UInt32,
    t_in             Float64,
    t_out            Float64,
    duration         Float64 MATERIALIZED t_out - t_in,
    caption          String,
    people_count     UInt8,
    time_of_day      Enum8('day'=1,'night'=2,'dawn'=3,'dusk'=4,'unknown'=0),
    interior         Enum8('interior'=1,'exterior'=2,'unknown'=0),
    weather          LowCardinality(String),
    shot_size        Enum8('ecu'=1,'cu'=2,'mcu'=3,'ms'=4,'mls'=5,'ls'=6,'els'=7,'unknown'=0),
    camera_move      LowCardinality(String),
    emotion          LowCardinality(String),
    tension          UInt8,
    dialogue_present Bool,
    dominant_colors  Array(String),
    objects          Array(String),
    characters       Array(String),
    thumbnail_uri    String,
    proxy_uri        String,
    embedding        Array(Float32),
    ingested_at      DateTime DEFAULT now(),
    INDEX emb_idx embedding TYPE vector_similarity('hnsw', 'cosineDistance', 1408)
)
ENGINE = MergeTree
ORDER BY (film_id, shot_index);

CREATE TABLE sequences
(
    sequence_id  String,
    session_id   String,
    intent       String,
    shot_ids     Array(String),
    created_at   DateTime DEFAULT now(),
    approved     Bool DEFAULT false
)
ENGINE = MergeTree ORDER BY (session_id, created_at);

CREATE TABLE search_log
(
    session_id  String,
    query_text  String,
    sql_text    String,
    result_ids  Array(String),
    latency_ms  UInt32,
    created_at  DateTime DEFAULT now()
)
ENGINE = MergeTree ORDER BY (session_id, created_at);
```

`vector_similarity` 인덱스는 ClickHouse 25.x 이상에서 사용 가능하다. ClickHouse Cloud 최신 버전은 지원하며, 미지원이면 인덱스 없이 `cosineDistance` 브루트포스로도 수만 행은 수십 ms 안에 끝난다.

### 3-2. Gemini 메타데이터 추출 스키마 (response_schema)

```json
{
  "type": "object",
  "required": ["caption","people_count","time_of_day","interior","weather",
               "shot_size","camera_move","emotion","tension","dialogue_present",
               "dominant_colors","objects","characters"],
  "properties": {
    "caption":          {"type":"string", "description":"1~2문장, 편집자가 로그 시트에 쓸 수준"},
    "people_count":     {"type":"integer"},
    "time_of_day":      {"type":"string", "enum":["day","night","dawn","dusk","unknown"]},
    "interior":         {"type":"string", "enum":["interior","exterior","unknown"]},
    "weather":          {"type":"string"},
    "shot_size":        {"type":"string", "enum":["ecu","cu","mcu","ms","mls","ls","els","unknown"]},
    "camera_move":      {"type":"string", "enum":["static","pan","tilt","dolly","handheld","zoom","crane","unknown"]},
    "emotion":          {"type":"string"},
    "tension":          {"type":"integer", "minimum":1, "maximum":5},
    "dialogue_present": {"type":"boolean"},
    "dominant_colors":  {"type":"array", "items":{"type":"string"}},
    "objects":          {"type":"array", "items":{"type":"string"}},
    "characters":       {"type":"array", "items":{"type":"string"}}
  }
}
```

입력은 샷 프록시 클립(최대 10초, 저해상도) 1개. 10초를 넘는 샷은 대표 프레임 3장 + 클립 앞 10초로 대체한다.

### 3-3. 임베딩
- 모델: `multimodalembedding@001`, video 모드, 1408차원
- 샷당 프록시 클립 1개를 넣어 video embedding 1개 획득. 검색 시 질의 텍스트를 같은 모델의 text 모드로 임베딩해 동일 공간에서 비교한다.
- 비용 절감: 5초 미만 샷은 대표 프레임 1장 image 모드로 대체 가능.

---

## 4. 에이전트 설계 (ADK)

### 4-1. 구성

| 에이전트 | 타입 | 역할 | 툴 |
| --- | --- | --- | --- |
| `EditorAssistant` | Root `LlmAgent` | 사용자 의도 분류 → 서브에이전트 위임. 대화 상태(현재 필름, 타임라인) 유지 | sub_agents 4개 |
| `Librarian` | `LlmAgent` | 자연어 → 하이브리드 검색 SQL 구성 → `run_query` → 결과 랭킹·요약 | `embed_query`, MCPToolset(`run_query`, `list_tables`) |
| `CutAssembler` | `LlmAgent` | 편집 의도(길이·구조·감정 곡선) → 후보 검색 여러 번 → 샷 시퀀스 → EDL 생성 | `Librarian`을 AgentTool로 호출, `build_edl` |
| `ContinuityChecker` | `LlmAgent` | 시퀀스의 시간대·실내외·의상·축 방향 불일치 검출, 심각도 부여 | MCPToolset(`run_query`), `compare_frames`(Gemini 비전) |
| `Narrator` | `LlmAgent` | 왜 이 샷을 골랐는지, 대안은 무엇인지 편집자 언어로 설명 | 없음 |

### 4-2. 툴 정의 (Python 함수 툴)
- `embed_query(text) -> list[float]` : Vertex multimodalembedding text 모드
- `build_edl(sequence: list[ShotRef], fps) -> str` : CMX3600 EDL 문자열 생성
- `compare_frames(shot_a, shot_b) -> ContinuityReport` : 두 샷 대표 프레임을 Gemini에 넣어 의상·소품·조명 방향·시선 방향 비교
- `MCPToolset(StdioServerParameters(command="uv", args=["run","--with","mcp-clickhouse","--python","3.13","mcp-clickhouse"], env={...}))`

### 4-3. Librarian이 생성하는 하이브리드 검색 SQL 예시

질의: "비 오는 밤, 두 사람, 클로즈업"

```sql
WITH [ ... 1408 floats ... ] AS q
SELECT shot_id, film_title, t_in, t_out, caption, thumbnail_uri,
       cosineDistance(embedding, q) AS dist
FROM shots
WHERE time_of_day = 'night'
  AND people_count = 2
  AND shot_size IN ('cu','mcu')
  AND (weather ILIKE '%rain%' OR caption ILIKE '%rain%')
ORDER BY dist ASC
LIMIT 24
```

Librarian 프롬프트 원칙
- 확실한 조건만 `WHERE`로 내리고 모호한 조건은 벡터 거리에 맡긴다.
- 필터 결과가 0건이면 필터를 한 단계씩 완화해 재질의한다(최대 3회).
- 항상 실행한 SQL과 건수·지연시간을 응답에 포함해 UI 패널에 노출한다.
- 임베딩 벡터는 SQL 문자열에 직접 넣지 않고 `embed_query` 결과를 파라미터로 바인딩한다. mcp-clickhouse `run_query`가 파라미터를 지원하지 않으면 벡터를 임시 테이블 `query_vectors`에 INSERT 후 서브쿼리로 참조한다.

### 4-4. CutAssembler 동작
1. 의도 파싱: 목표 길이, 구조(예: 긴장 상승 → 클라이맥스 → 해소), 톤, 필수 포함 요소
2. 구조를 3~5개 구간으로 나누고 구간별 `tension` 범위·샷 사이즈 진행(ls → ms → cu) 조건 생성
3. 구간마다 Librarian 호출 → 후보 8개
4. 구간 길이 배분에 맞춰 샷 선택. 같은 필름·연속 shot_index 우선(컷 연결 자연스러움)
5. `ContinuityChecker`로 인접 샷 검사 → 경고 있는 샷은 후보 2순위로 교체
6. `build_edl` → 타임라인 UI에 렌더 + `sequences` 테이블 저장

### 4-5. ContinuityChecker 규칙
- 메타데이터 규칙(SQL만으로 판정): 인접 샷의 `time_of_day` 불일치, `interior` 불일치, 같은 캐릭터인데 `dominant_colors` 급변
- 비전 규칙(`compare_frames`): 의상·소품 차이, 시선 방향(180도 규칙), 조명 방향
- 출력: `{pair, rule, severity: low|mid|high, explanation, suggested_replacement}`

---

## 5. 인제스트 파이프라인

```
입력: gs://bucket/films/{film_id}/source.mp4
 1. ffprobe → fps, duration
 2. PySceneDetect ContentDetector(threshold=27) → 샷 리스트 [(t_in, t_out)]
    · 1초 미만 샷은 이전 샷에 병합
 3. 샷마다 ffmpeg
    · 프록시: 320p, 앞 10초, h264 → gs://bucket/proxies/{shot_id}.mp4
    · 썸네일: 25%·50%·75% 지점 jpg → gs://bucket/thumbs/{shot_id}_{n}.jpg
 4. Gemini 3.8 Flash (response_schema) ← 프록시 클립
    · 동시성 8, 429 시 지수 백오프
 5. multimodalembedding@001 video 모드 ← 프록시 클립
 6. 1,000행 단위 배치 INSERT (clickhouse-connect)
 7. 진행률을 Firestore 또는 ClickHouse `ingest_jobs` 테이블에 기록 → UI 폴링
```

### 5-1. 데모 데이터셋 (퍼블릭 도메인 확인 완료 작품)
| 작품 | 연도 | 특징 | 예상 샷 수 |
| --- | --- | --- | --- |
| Night of the Living Dead | 1968 | 흑백, 야간·실내외 다양, 긴장 곡선 뚜렷 | ~1,200 |
| Nosferatu | 1922 | 무성, 표현주의 조명, 클로즈업 많음 | ~600 |
| His Girl Friday | 1940 | 대화 위주, 실내, 인물 2~3명 샷 풍부 | ~700 |
| Charade | 1963 | 컬러, 파리 로케이션, 실외·야간·비 장면 | ~1,300 |
| Plan 9 from Outer Space | 1959 | 연속성 오류가 유명해 ContinuityChecker 데모용 | ~800 |
| The Last Man on Earth | 1964 | 황량한 실외, 고독 감정 | ~900 |

합계 약 5,500샷. "1만 샷 이상" 카운터를 위해 Internet Archive 퍼블릭 도메인 작품 4~5편을 추가한다. 각 작품의 퍼블릭 도메인 여부는 README에 출처와 함께 기재한다.

### 5-2. 비용 추정 (10,000샷 기준, 2026-09 공식 단가)

전제: 샷당 프록시 10초(저해상도 약 100 tokens/초 → 1,000) + 프롬프트 300 + JSON 출력 250 tokens.

| 추출 모델 | 입력 $/1M | 출력 $/1M | 샷당 | 10,000샷 |
| --- | --- | --- | --- | --- |
| Gemini 2.5 Flash-Lite | 0.10 | 0.40 | $0.00023 | **$2.3** |
| Gemini 2.5 Flash | 0.30 | 2.50 | $0.0010 | $10 |
| Gemini 3.5 Flash-Lite | 0.30 | 2.50 | $0.0010 | $10 |
| **Gemini 3.8 Flash** (2026-12-31까지 도입가) | 0.75 | 3.75 | $0.0019 | **$19** |
| Gemini 3.1 Pro Preview | 2.00 | 12.00 | $0.0056 | $56 |

| 임베딩 | 단가 | 10,000샷 |
| --- | --- | --- |
| Gemini Embedding (텍스트, 캡션 ~100 tokens) | $0.15/1M | $0.15 |
| **Gemini Embedding 2 image 모드** (대표 프레임 1장) | $0.00012/장 | **$1.2** |
| Gemini Embedding 2 video 모드 (10프레임) | $0.00079/프레임 | $79 (비추천) |

| 기타 | 비용 |
| --- | --- |
| ClickHouse | 로컬 Docker $0 / Cloud는 $400 크레딧 내 |
| 서버·스토리지 | 개인 서버 $0 |

**권장 조합**: 추출 **Gemini 3.8 Flash** + 임베딩 **Gemini Embedding 2 image 모드** → 10,000샷 약 **$20**. 월 $10 Developer Program 크레딧으로 절반 상쇄.
Embedding 2 image 모드는 API 키로 호출되는 멀티모달 임베딩이라 Vertex 없이 12-2의 텍스트 임베딩보다 나은 검색 품질을 얻는다. 질의는 같은 모델의 텍스트 모드로 임베딩한다.

모델 배치
- 샷 메타데이터 추출: `gemini-3.8-flash` (agentic video understanding 지원, 도입가 적용 중)
- 편집 의도 해석·조립·Narrator: `gemini-3.8-flash` (호출 수 적어 비용 무관, 필요 시 `gemini-3.1-pro-preview`)
- 연속성 비전 비교: `gemini-3.8-flash`
- 검증용 재추출(상위 샷만): `gemini-3.1-pro-preview` 선택

---

## 6. UI 설계

단일 페이지 앱. 좌측 필름 목록, 중앙 작업 영역, 우측 에이전트 패널.

| 영역 | 구성 |
| --- | --- |
| 상단 바 | 필름 선택 · 인제스트 상태 · **누적 샷 수 카운터** |
| 검색 | 자연어 입력 → 썸네일 그리드(호버 시 프록시 재생) · 각 카드에 메타데이터 칩 · "이 샷과 비슷한" 버튼 |
| SQL 패널 (접이식) | Librarian이 실행한 SQL · 건수 · 지연시간 ms |
| 타임라인 | 드래그 앤 드롭 · 구간별 감정 곡선 미니 그래프 · 연속성 경고 아이콘 |
| 에이전트 패널 | 진행 중인 에이전트와 단계 표시(Librarian 검색 중 → CutAssembler 조립 중 → ContinuityChecker 검사 중) · Narrator 설명 |
| 승인 | 경고별 "교체안 적용 / 무시" · 시퀀스 저장 |
| 내보내기 | EDL(CMX3600) 다운로드 · FCPXML |

게스트 접근: 로그인 없이 사전 인제스트된 필름으로 검색·조립 가능. 인제스트 실행만 토큰 필요.

---

## 7. 저장소 구조

```
shot-memory/
├── LICENSE                     Apache-2.0
├── README.md                   아키텍처 다이어그램 · Google Cloud/ClickHouse 사용 표 · 실행법 · 데이터 출처
├── ARCHITECTURE.md
├── agent/
│   ├── __init__.py
│   ├── agent.py                root_agent = EditorAssistant
│   ├── subagents/
│   │   ├── librarian.py
│   │   ├── cut_assembler.py
│   │   ├── continuity_checker.py
│   │   └── narrator.py
│   ├── tools/
│   │   ├── clickhouse_mcp.py   MCPToolset 생성
│   │   ├── embeddings.py       embed_query
│   │   ├── edl.py              build_edl
│   │   └── vision.py           compare_frames
│   └── prompts/
├── ingest/
│   ├── pipeline.py
│   ├── scenes.py
│   ├── describe.py             Gemini 호출
│   ├── embed.py
│   └── load.py                 clickhouse-connect
├── web/                        UI (Vite + 경량 프레임워크)
├── sql/
│   └── schema.sql
├── deploy/
│   ├── Dockerfile.agent
│   ├── Dockerfile.ingest
│   └── cloudrun.yaml
├── scripts/
│   ├── download_public_domain.sh
│   └── run_ingest_job.sh
└── docs/
    └── demo_script.md
```

---

## 8. 배포

| 구성요소 | 배포 |
| --- | --- |
| Agent App | Cloud Run Service, 컨테이너 내부에서 mcp-clickhouse를 stdio 서브프로세스로 실행. `PORT` 환경변수 준수 |
| Ingest | Cloud Run Job, 필름당 1 실행. CPU 4, 메모리 8GB, 타임아웃 최대 |
| ClickHouse | ClickHouse Cloud, promo 링크 가입(`?promo=SIGNUP100`) |
| 시크릿 | Secret Manager → Cloud Run 환경변수 마운트 |
| 로컬 개발 | `adk web`으로 에이전트 단독 실행, ClickHouse는 Cloud 접속 |

호스팅 URL이 크레딧 소진으로 내려가도 데모 영상이 심사 근거가 된다(주최측 확인). 다만 심사 기간 첫 2주는 살려 두는 것을 목표로 한다.

---

## 9. 3분 데모 영상 스크립트

| 시간 | 화면 | 내레이션 요지 |
| --- | --- | --- |
| 0:00–0:20 | 실제 로그 시트 스프레드시트, 타임코드를 손으로 적는 장면 | "다큐 편집 어시스턴트는 100시간 푸티지를 3주 동안 손으로 로깅한다. 편집자의 '비 오는 밤 클로즈업 찾아줘' 한마디에 반나절이 사라진다." |
| 0:20–0:50 | 상단 카운터 "6 films · 10,412 shots", 인제스트 파이프라인 다이어그램 한 장 | "Shot Memory는 Gemini가 모든 샷을 보고 로그를 쓰고, Vertex AI가 임베딩하고, ClickHouse가 기억한다." |
| 0:50–1:40 | 검색 3회 라이브. ① "rainy night, two people, close-up" ② "lonely man walking through empty street, wide shot" ③ ①의 결과 카드에서 "find similar" | SQL 패널을 열어 "에이전트가 만든 하이브리드 쿼리, 0.18초, 24건" 표시 |
| 1:40–2:20 | "Build a 60-second teaser: tension rising to a climax, then release" 입력 → 에이전트 패널에 Librarian → CutAssembler → ContinuityChecker 진행 → 타임라인 생성 → 경고 1건(실내/실외 불일치) → 교체안 승인 → EDL 다운로드 → Resolve에서 열리는 화면 | "에이전트 팀이 구간별로 검색하고 조립하고 연속성을 검사한다. 편집자는 승인만 한다." |
| 2:20–2:50 | 아키텍처 다이어그램. Google ADK · Gemini 3.8 Flash · Gemini Embedding 2 · Cloud Run · Cloud Storage · **ClickHouse MCP** 박스 강조 | "ClickHouse는 SQL 챗봇이 아니라 에이전트의 장기 기억이다. mcp-clickhouse로 런타임에 결합된다." |
| 2:50–3:00 | 포지셔닝 문장 + 리포 URL + 라이브 URL | |

영어 내레이션 또는 영어 자막 필수. 배경 음악은 퍼블릭 도메인 또는 무음. 영상 내 로고는 자체 로고만.

---

## 10. 제출물 체크리스트

### 형식 요건
- [ ] 저장소 public, 루트에 `LICENSE`(Apache-2.0)
- [ ] 저장소 생성일이 2026-07-27 이후
- [ ] `google-adk`, `google-genai`, `google-cloud-aiplatform` 런타임 import·호출이 `agent/` 아래에 존재
- [ ] `mcp-clickhouse` 런타임 호출이 `agent/tools/clickhouse_mcp.py`에 존재하고 실제 검색 경로가 이를 통함
- [ ] 호스팅 URL 시크릿 브라우저에서 접속 확인, 로그인 벽 없음
- [ ] 데모 영상 3분 이내, YouTube 공개, 영어
- [ ] Devpost 텍스트 설명 영어 4요소(무엇을, 어떻게 만들었나, Google Cloud 사용, 파트너 사용)
- [ ] 팀원 전원 Devpost 프로젝트에 등록

### 콘텐츠 요건
- [ ] README 아키텍처 다이어그램에 Google Cloud 제품명과 ClickHouse MCP를 박스로 표기
- [ ] README에 데모 필름 6편의 퍼블릭 도메인 근거(출처 URL) 기재
- [ ] README에 "ClickHouse를 제거하면 검색·조립이 동작하지 않는다" 명시
- [ ] 영상 앞 20초에 실무 문제, 2분 20초까지 실제 화면 동작
- [ ] Google 외 AI 모델·프레임워크 import 잔재 없음 (`grep -ri "openai\|anthropic\|langchain"` 0건)
- [ ] 영상·스크린샷에 상용 BGM·타사 로고 없음

### 마감
- 2026-09-09 14:00 PDT = **KST 2026-09-10 06:00**. 최소 12시간 전 제출.

---

## 11. 리스크와 대응

| 리스크 | 대응 |
| --- | --- |
| Gemini 비디오 처리 쿼터 초과 | 동시성 제한 + 백오프. Flash로 1차 추출, 상위 샷만 Pro. 데모는 사전 인제스트된 데이터로 진행 |
| `vector_similarity` 인덱스 미지원 버전 | 브루트포스 `cosineDistance`로 대체. 1만 행이면 수십 ms |
| mcp-clickhouse `run_query`에 1408차원 벡터를 문자열로 넣으면 SQL이 너무 김 | 임시 테이블 `query_vectors`에 INSERT 후 서브쿼리 참조 (쓰기 권한은 별도 MCP 인스턴스 또는 `CLICKHOUSE_ALLOW_WRITE_ACCESS` 한정) |
| Cloud Run에서 stdio MCP 서브프로세스 콜드스타트 | min-instances 1, 앱 기동 시 MCP 세션 미리 생성 |
| 퍼블릭 도메인 판정 오류 | 미국 기준 1929년 이전 작품 또는 저작권 갱신 누락이 문서화된 작품만 사용. 출처 기재 |
| 심사위원이 "Agent Builder 요건 = Gemini Enterprise 배포"로 해석 | ADK가 Agent Builder 제품군임을 README에 명시. 여력이 있으면 Agent Engine에도 병행 배포 |

---

## 12. 로컬 우선 구성 (개인 서버 활용)

규정상 Google에 남아야 하는 것은 **모델 호출**뿐이다. 나머지는 개인 서버에서 실행해도 요건을 충족한다.

### 12-1. 배치표

| 구성요소 | 로컬 가능 | 방법 | 근거 |
| --- | --- | --- | --- |
| ClickHouse | O | Docker `clickhouse/clickhouse-server` 1컨테이너 | 규정이 self-hosted 클러스터 명시 허용 |
| mcp-clickhouse | O | stdio 서브프로세스 | 원래 로컬 실행이 기본 |
| ADK 에이전트 앱 + UI | O | 개인 서버 + Cloudflare Tunnel 또는 보유 도메인으로 공개 URL | 주최측 "무료 티어 호스팅 배포도 유효" 답변 |
| 인제스트 파이프라인 | O | 로컬 CPU (PySceneDetect, ffmpeg, 배치 INSERT) | Google 요건 없음 |
| 영상·썸네일·프록시 저장 | O | 로컬 디스크 + 정적 파일 서빙 | Cloud Storage 대체 |
| Gemini 호출 | X | `google-genai` + **Gemini API 키** (Vertex 불필요, GCP 결제 불필요) | 타사 모델 금지, SDK 런타임 호출 요건 |
| 임베딩 | X | `gemini-embedding-001` 텍스트 임베딩 (API 키) | 아래 12-2 참고 |

### 12-2. 임베딩 변경안
원안의 Vertex `multimodalembedding@001`은 GCP 프로젝트와 결제가 필요하다. 완전 로컬 지향이면 다음으로 대체한다.

- Gemini가 뽑은 `caption` + `emotion` + `objects` + `characters` + `camera_move`를 하나의 서술문으로 합쳐 `gemini-embedding-001`(3072차원, API 키)로 임베딩
- 검색 질의도 같은 모델로 임베딩
- 스키마의 `embedding Array(Float32)`와 인덱스 차원을 3072로 변경
- 영상 직접 임베딩보다 품질은 약간 낮지만 캡션이 상세하면 실용 차이는 작다. 추출 스키마의 `caption`을 2~3문장으로 늘려 보완한다.

### 12-3. 트레이드오프
Technological Implementation 기준은 "Google Cloud를 얼마나 효과적으로 썼는가"를 본다. 완전 로컬 구성은 Google 제품이 **ADK + Gemini** 둘로 줄어 이 항목이 약해진다.

### 12-4. 절충안 (권장)
1. 개발·인제스트·ClickHouse·데이터는 전부 로컬
2. 마감 전 **에이전트 앱 컨테이너 하나만 Cloud Run**에 배포
   - ClickHouse는 로컬에 두고 Cloud Run에서 터널 경유 접속, 또는 마지막에 ClickHouse Cloud($400 크레딧)로 `INSERT ... SELECT FROM remote()`로 복사
   - 자격증명은 Secret Manager로
3. README 다이어그램에 Cloud Run · Secret Manager 박스가 추가되고 비용은 거의 없다
4. 임베딩은 12-2의 API 키 방식을 유지해도 되고, GCP 결제를 켤 수 있으면 원안의 Vertex multimodal로 복귀

### 12-5. 로컬 ClickHouse 기동

```bash
docker run -d --name shot-memory-ch \
  -p 8123:8123 -p 9000:9000 \
  -e CLICKHOUSE_USER=shotmem -e CLICKHOUSE_PASSWORD=change-me \
  -v $PWD/data/clickhouse:/var/lib/clickhouse \
  clickhouse/clickhouse-server:latest
```

mcp-clickhouse 환경변수는 `CLICKHOUSE_HOST=localhost`, `CLICKHOUSE_PORT=8123`, `CLICKHOUSE_SECURE=false`.
