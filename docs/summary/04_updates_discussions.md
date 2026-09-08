# 04. 주최측 업데이트 & 디스커션 포럼 정리

출처: https://agentic-cinema.devpost.com/ (updates / forum_topics / participants)
수집 기준일: 2026-09-08 (마감 D-1 시점)

- 대회명: Agentic Cinema: The Blockbuster Hackathon (주최: Google Cloud, 운영: Devpost)
- 마감: **2026년 9월 9일 오후 2:00 PDT**
- 참가자: **9,904명**
- 상금: 총 **$75,000** — 5개 파트너 트랙 × $15,000 (1위 $7,500 / 2위 $4,500 / 3위 $3,000)
- 파트너 트랙: IBM · Grafana · Parallel · ClickHouse · Replit
- 공식 담당자: **Janet Fang (Devpost Manager, janet@devpost.com)** — 포럼 공식 답변의 대부분이 이 사람 명의
  - 그 외 Dustin Healy (ClickHouse 측 지원 응답)

---

## 1. 주최측 업데이트 타임라인

업데이트는 총 10건. 성격상 **(a) 대회 개시/트랙 공지**, **(b) 파트너 빌드 세션 예고·녹화본**, **(c) 마감 리마인더** 세 종류로만 구성되어 있고,
**규칙 변경이나 마감 연장 공지는 업데이트 게시물에 없다.** (마감일 9/7 → 9/9 정정은 업데이트가 아니라 포럼 답변에서 확인됨. 아래 2-⑫ 참조)

| # | 날짜(상대) | 제목 | 핵심 내용 |
|---|---|---|---|
| 10 | 약 1개월 전 (7월 하순, 대회 개시) | **The Challenge is Live — Meet Your Partners** | 대회 개시 공지. "Gemini + Google Cloud Agent Builder 기반의 동작하는 에이전트를 만들고, 파트너사 제품 또는 MCP를 통합하라". 5개 트랙(IBM/Grafana/Parallel/ClickHouse/Replit) 공개, 총 $75,000·트랙당 $15,000 안내. Google Cloud는 무료 체험 또는 **폼 신청으로 $100 크레딧**(승인 1~5영업일), **크레딧 신청 마감 8/31**. Resources 탭·디스코드 안내 |
| 9 | 25일 전 (약 8/14) | **Upcoming Events** | 주간 빌드 세션 4건 예고 — IBM Bob(8/17 8AM PT), ClickHouse(8/18 8AM PT), Grafana(8/20 8:30AM PT), Parallel(8/21 9:30AM PT). 각 Zoom 등록 링크 포함 |
| 8 | 22일 전 (8/17) | **IBM Build Session starts today at 11AM ET / 8AM PT** | "Build Faster with IBM Bob: AI-Assisted Coding for Hackathon Teams" — Richard Boyd 진행. 코드 생성·문서화·리팩터링 시연 |
| 7 | 21일 전 (8/18) | **Tomorrow: ClickHouse Build Session at 11AM ET / 8AM PT** | "The Agent's Memory: Powering Real-Time AI Workflows with ClickHouse" — MCP 서버를 통해 ClickHouse를 Gemini Enterprise 에이전트의 실시간 데이터 레이어로 연결. 난이도 Intermediate |
| 6 | 19일 전 (8/19) | **Grafana Build Session starts tomorrow at 11:30AM ET / 8:30AM PT** | "Premiere Night — Build an Observability Agent with Grafana Cloud MCP and Google ADK" — 에이전트를 처음부터 만들고 인시던트를 조사시키는 시연 |
| 5 | 18일 전 (8/20) | **Parallel Build Session starts tomorrow at 12:30PM ET / 9:30AM PT** | "Getting Started with Parallel: Build a Web-Grounded Gemini Agent" — Gemini에 Parallel Search 연결, grounding 메타데이터 확인, 소스 인용 검토 |
| 4 | 17일 전 (8/22) | **Replit Build Session this Monday at 12:00PM ET / 11:00AM CT** | 8/24(월) 예고. "Ship Your Agentic Cinema Submission: Live Build + Q&A with Replit" |
| 3 | 15일 전 (8/24) | **Replit Build Session today at 12:00PM ET / 11:00AM CT** | 당일 리마인더. Manny Bernabe 진행, 셋업·호스팅·디버깅 Q&A. Zoom 등록 링크 |
| 2 | 14일 전 (8/25) | **Build Session Recordings** | **5개 세션 녹화본 전부 공개** (아래 링크 표 참조) |
| 1 | 1일 전 (2026-09-07) | **Final Call for Submissions** | "제출 완료까지 3일 남았습니다" — 최종 마감 리마인더 |

### 빌드 세션 녹화본 링크 (업데이트 #2)

| 파트너 | YouTube |
|---|---|
| Replit | https://youtu.be/2N_x5eZCisk |
| Parallel | https://youtu.be/6BG12veBOII |
| Grafana | https://youtu.be/jFhd6KzC_pM |
| ClickHouse | https://youtu.be/JIwe_YG6Rys |
| IBM | https://youtu.be/OGMbNN5jGso |

### 타임라인에서 읽히는 것

- 대회 개시(7/27) → 8월 중순 2주간 파트너 빌드 세션 집중 → 8/31 크레딧 신청 마감 → 9/9 제출 마감.
- 5개 트랙이 처음부터 전부 공개된 것이 아니라 **순차 공개**되었다. 포럼 답변("we just released 3 more partners today")으로 보아 초기에는 2개 트랙만 있었고 이후 3개가 추가됨.
- 마감 직전 3주간 주최측 업데이트가 사실상 없다가 D-3에 리마인더 1건만 나옴. 규칙 관련 소통은 전부 포럼에서 개별 답변으로 처리되었다.

---

## 2. 규칙·제출 관련 공식 답변 모음 (Q → A)

> 아래 A는 별도 표기가 없으면 전부 **Janet Fang (Devpost Manager)** 의 공식 답변이다.
> **이 대회에서 가장 논쟁적이고 가장 많이 반복된 주제는 "Section 7.B의 AI 도구 제한"이다.** ①~④를 반드시 먼저 읽을 것.

### ① AI 도구 제한은 런타임만인가, 개발 과정 전체인가? ★★★ (가장 중요)

**Q** (Faris Irfan / Loordhu Jeyakumar / Suresh Poonepalle 등 최소 4개 스레드에서 반복 질문)
"Section 7.B의 AI 도구 제한은 프로젝트가 런타임에 호출하는 모델/API에만 적용되나요, 아니면 Claude Code·ChatGPT·Codex 같은 개발용 코딩 어시스턴트에도 적용되나요?"

**A (공식)**
> "Section 7.B's AI-tooling restriction covers your whole development workflow, not just what runs in the submitted project."
> "the restriction applies to your whole dev workflow, not only to what's called at runtime."

즉 **개발 전 과정에 적용된다.** 구체적으로:

- 허용: **Google의 코딩 도구만** — Gemini CLI, Gemini Code Assist, AntiGravity(Google Antigravity) suite, Vertex AI 등 Google Cloud AI 도구 + **선택한 트랙 파트너의 내장 AI 기능**
- 금지: ChatGPT, Codex, Claude 등 그 외 모든 서드파티 AI 모델/어시스턴트
- 적용 범위: 코딩·스캐폴딩·트러블슈팅뿐 아니라 **비코드 영역(프로젝트 기획, 일정 관리, 요구사항 해석)까지** 포함
- 즉 "런타임에는 Gemini만 쓰니까 개발은 아무 도구나 써도 된다"는 해석은 **명시적으로 부정됨**

### ② 규칙을 모르고 서드파티 AI로 이미 코드를 짰다면?

**Q** (Nitish K) "Codex로 만든 스캐폴딩을 전부 버리고 Google Antigravity 에이전트만으로 처음부터 다시 만들면 자격이 유지되나요?"

**A (공식)**
- 유지된다. 단 **기존 코드를 전부 폐기하고 허용된 Google 도구로 재작성**해야 한다.
- **프로젝트의 컨셉과 아키텍처는 유지해도 된다.** 같은 저장소 안에서 재작성해도 무방.
- **"검토·검증만 한 것"으로는 컴플라이언스가 회복되지 않는다** (non-compliant 코드를 사람이 리뷰했다고 compliant가 되는 게 아님).
- "non-code strategy and feasibility analyses are treated completely differently from implementation artifacts" — 비코드 전략/타당성 분석은 구현 산출물과 완전히 다르게 취급된다.
- 다만 제출물에는 "actual, running code and a working technical implementation"이 반드시 있어야 한다.

### ③ IBM Bob은? Google Stitch는?

**Q** (Suresh Poonepalle) "IBM Bob과 Google Stitch는 개발 시점 도구인데 허용되나요?"

**A (공식)**
- **IBM Bob: 전면 허용.** IBM 트랙의 필수 파트너 도구이므로 "using it (including its internal multi-model orchestration) is expected and fully permitted" — 내부적으로 멀티모델 오케스트레이션을 하더라도 문제없음.
- **Google Stitch: 불가.** Google 제품이지만 **공식 Google Cloud AI 스위트에 속하지 않으므로** Section 7.B의 허용 도구가 아니다. "regardless of whether you'd only use it at design time" — 디자인 타임에만 써도 안 됨.
- 권장: **README에 사용한 모든 툴링을 문서화**할 것.

### ④ AI 제한에 대한 참가자 반발

- Tarik Moody: 이미 다른 코딩 어시스턴트를 유료 구독 중인데, 규칙 때문에 Google AntiGravity를 추가로 구매/업그레이드해야 하는 비용 문제를 지적.
- "왜 다른 코딩 에이전트를 금지하는가"라는 후속 질문 및 "브레인스토밍용 ChatGPT는 되는가"라는 질문은 **답변되지 않은 채 남아 있음**.
- Gemini CLI를 유료 API 키로 쓰는 경우에 대한 질문도 **미답변**.

### ⑤ "신규 프로젝트만" 규칙 — 대회 시작 전에 만든 프로젝트

**Q** (Zaeem Khan) "7/17에 리포를 만들고 7/19에 핵심 프로토타입을 완성했습니다. 대회는 7/27 시작인데, 제출 폼에서 'Existing'을 선택하면 되나요?"

**A (공식)** — Official Rules Section 7.B 인용
> "Projects must be newly created by the entrant during the Contest Period. The Project must be Your original creation not a modification or extension of Your or anyone else's existing work."

- 리포와 프로토타입이 모두 7/27 이전이므로 **자격 미달**.
- **제출 폼에서 'Existing'을 고르는 것은 예외 조항이 아니다.** (폼 옵션이 있다고 기존 프로젝트가 허용되는 게 아님)
- 참가자가 "규칙 확정 전에 Devpost에 대회가 올라와 있어서 초기 참가자가 불리했다"고 항의하자, 주최측은 반박: "the hackathon rules, project requirements and submission requirements, including the July 27 Contest Period start date, were not posted prior to the July 27th start date" — 7/27 이전에는 규칙 자체가 게시되지 않았으므로 불이익이 없었다.

### ⑥ 기존에 보유한 자체 IP(세계관)를 소재로 쓰는 것은?

**Q** (andrianadreamrealm Vuceljic, 마감 하루 전 질문) "기존에 제가 소유한 'Dream Realm' 픽션 세계관을 배경/레퍼런스로만 쓰고 **코드는 전혀 재사용하지 않는** 신규 에이전트 앱을 만들면 'New Projects Only'에 걸리나요?"

**A** — **답변 없음 (0 comments).** 마감 직전 질문이라 공식 해석이 나오지 않았다.

### ⑦ Replit 트랙 요건

**Q** (Virginia Neacsu) "Replit Agent로 만들고 replit.app에 배포하면 충분한가요, 아니면 Replit 서비스에 대한 명시적 API/MCP 호출도 필요한가요?"

**A (공식)**
> "This is all you need for Replit: your project must be built using Replit Agent as part of the development process, and the finished project must be hosted and deployed directly on Replit (a project URL on a replit.app or replit.dev domain). Projects not deployed on Replit's platform will not meet this requirement, regardless of how the code was written."

- 별도의 Replit API/MCP 호출 **불필요**.
- 단 **replit.app / replit.dev 도메인에 실제 배포**되어야 한다. 코드를 어떻게 짰든 Replit 플랫폼에 배포되지 않으면 요건 미달.

### ⑧ Replit 트랙 + Google SDK 요건은 어떻게 충족하나?

**Q** (Miguel Olave) "Replit AI Integrations로 Google Gemini를 고르면 Google Cloud SDK 사용 요건이 충족되나요, 아니면 SDK를 수동 설정해야 하나요?"

**A (공식)** — 두 요건은 별개다.
- **트랙 요건**: Replit Agent로 빌드 + Replit(.app/.dev)에 배포
- **전체 제출 요건(모든 트랙 공통)**: 코드가 런타임에 다음 4개 Google SDK 중 하나를 import·호출해야 함 —
  **`google-adk`, `google-genai`, `google-generativeai`, `google-cloud-aiplatform`**
- 결론: Replit AI Integrations에서 Google Gemini를 선택하면 통합이 **자동으로 필요한 Google SDK를 프로비저닝**하므로 별도 API 키 설정 없이 충분하다 (런타임에 실제로 Google 데이터/컨텍스트를 쓴다는 전제).

### ⑨ IBM 트랙 요건 — Bob만으로 MCP 요건이 충족되나?

**Q** (Asad Ali) "IBM Bob 사용만으로 파트너 MCP 요건이 충족되나요, 아니면 Confluent 런타임 통합도 필요한가요?"

**A (공식)**
- "IBM Bob usage satisfies the requirement!" — **Bob 사용만으로 충족.**
- 요건은 "be built using IBM Bob as part of the development process" — 개발 과정에서 Bob을 쓸 것.
- **Confluent는 선택 사항**이나 실시간 데이터·이벤트 기반 워크플로 강화를 위해 권장됨.
- 모든 제출물은 AI가 워크플로/의사결정/고객경험/운영 결과를 어떻게 유의미하게 개선하는지 보여줘야 함.

### ⑩ Parallel 트랙 — 호스팅 데모가 실시간 Search API를 호출해야 하나?

**Q** (Tyler Rabiger) "authoritative 검색은 ~90초가 걸리는데 데모 영상은 3분 제한입니다. 호스팅 데모가 매번 새 Search API 호출을 해야 하나요, 검증된 실제 실행 결과의 사전 생성 리플레이도 되나요?"

**A (공식, Parallel 팀 확인)**
- **사전 생성 데모 허용.** "a real, pre-generated demo on the hosted URL"이 가능하다. 단 "your video and repo clearly show the project genuinely calling Parallel Search at runtime" — 영상과 리포에서 실제로 런타임에 Parallel Search를 호출한다는 것이 명확히 드러나야 한다.
- 심사 중 라이브 API 호출은 **필수 아님**.
- "You don't need to expose your own API key or ask judges to provide one just to make the public demo live" — 공개 데모를 살리자고 본인 API 키를 노출하거나 심사위원에게 키를 요구할 필요 없음.
- 공개 데모에 나오는 서드파티 이름·URL은 **가상(fictional)이거나 마스킹**되어야 한다.

### ⑪ 데모 영상에 실제 웹 검색 결과(실제 회사명·URL)를 노출해도 되나? ★

**Q** (Masakazu Tanaka, Parallel 트랙 팩트체킹 프로젝트) "Search API가 실제 웹페이지를 가져오는데, 데모 영상·스크린샷에 실제 도메인/제목/URL을 그대로 보여도 되나요?"

**A (공식, Parallel 팀 가이드 확인)**
- **공개 자료(데모 영상·스크린샷)에는 가상의 웹사이트를 쓸 것.** 서드파티 상표 조항 준수를 위해 mock 데이터 사용.
- **라이브 호스팅 앱은 실제 검색 결과를 그대로 보여줘도 된다.** 심사위원이 진짜 통합을 평가해야 하기 때문.
- 요약: **공개물 = mock, 라이브 데모 = 실제.**

### ⑫ 마감일이 9/7인가 9/9인가?

**Q** (Zaqueu Ribeiro) "Devpost 페이지는 2026-09-09인데 Official Rules에는 2026-09-07 2:00PM PT로 되어 있습니다."

**A (공식)** — "updated everything to the September 9th deadline." **9월 9일이 정답**이며 규칙 문서도 9/9로 갱신됨.

### ⑬ 크레딧이 만료된 뒤에는 심사위원이 어떻게 프로젝트를 테스트하나?

**Q** (Anirudh Reddy Velagala) "심사 기간이 끝나기 전에 프로모션 크레딧이 소진/만료되면 어떻게 평가하나요?"

**A (공식)**
> "Judges evaluate what's submitted - hosted Project URL, demo video, and repo"

- 라이브 환경이 무한정 유지될 필요 **없음**.
- 호스팅 버전이 내려가더라도 **에이전트가 완전히 동작하는 것을 보여주는 데모 영상이면 충분**.
- 크레딧이 허용하는 한 호스팅 URL을 살려두되, 만료 후에는 영상이 백업 역할을 한다.
- 즉 **무료 크레딧 소진 후 유료 결제를 켜야 한다는 압박은 없다.**

### ⑭ 스코프 — 헐리우드 대작만 대상인가, 인디 크리에이터도 되나? ★

**Q** "Agentic Cinema라는 이름이 대형 프로덕션만 뜻하나요? 유튜버·틱톡커·인플루언서용 도구도 되나요?"

**A (공식)**
> "You are absolutely allowed—and highly encouraged—to build tools for YouTube studios, TikTokers, indie creators, and social media influencers."

근거로 제시된 논리:
- 현대의 "studio crew"에는 방구석 1인 프로듀서도 포함된다.
- 인디 크리에이터도 전통 영화와 **동일한 병목**을 겪는다 — 각본, 스토리보드, 오디오 편집, 오디언스 인게이지먼트.
- **에이전틱 AI는 여러 제작 역할을 혼자 겸하는 솔로 크리에이터에게 특히 적합**하다.

주최측이 직접 예시로 든 방향:
- Imagen 3를 쓴 **AI 스크립트→스토리보드 에이전트**
- **YouTube 영상 최적화 도구**
- Gemini TTS를 쓴 **팟캐스트/오디오 자동 편집기**

기술 요건 재확인: 모든 제출물은 **Gemini Enterprise Agent Platform**을 사용하고 **5개 파트너 트랙 중 하나와 런타임에 통합**되어야 한다.

> 미해결: Tim Dries가 "Vertex AI에 배포한 Google ADK 2.7.1이 'Agent Builder' 요건을 충족하나, 아니면 Gemini Enterprise 배포가 필수인가?"를 물었으나 **답변 없음**. (트랙 요건 해석상 잠재적 리스크 지점)

### ⑮ 자격 — 정부기관 직원

**Q** (Malik Kabir) "정부기관 직원인데, 미디어/엔터테인먼트나 파트너사와 아무 이해충돌이 없습니다. 규칙이 모든 공무원을 배제하나요, 실제 이해충돌이 있는 경우만인가요?"

**A (공식)**
> "government-agency employment is its own categorical bar under our rules - anyone employed by a government agency is ineligible to participate, regardless of whether their specific role or agency creates a conflict."

**정부기관 소속이면 이해충돌 여부와 무관하게 일괄 참가 불가.** 질문자는 개발 착수 전에 확인했다며 참가를 포기.

### ⑯ 자격 — 비대상 국가(브라질) 거주자

**Q** (Zaqueu Ribeiro, 브라질) "적격 국가 목록에 브라질이 없습니다. 상금을 포기하고 비경쟁으로 참가해도 되나요?"

**A (공식)**
> "you're welcome to participate - you can build, submit, and take part in the event alongside everyone else, and your project will still show up in the project gallery. The one thing eligibility affects is prize consideration."

**빌드·제출·갤러리 게재 모두 가능. 자격이 영향을 주는 것은 오직 상금 심사뿐.**

### ⑰ Google Cloud $100 크레딧 — 신청·승인·재신청

- 신청: 폼 제출 → **승인 1~5영업일**. **신청 마감 8/31.**
- **결제 카드 등록은 필수**: "completing Google's payment verification step (adding a valid card) is a standard requirement" — 빌링 계정 활성화를 위한 표준 절차이며, 승인된 사용분은 $100 크레딧이 커버.
- **프로모션 $100 쿠폰은 일반 무료 크레딧과 별도로 도착**하며 Google Cloud Console의 Billing에서 직접 리딤해야 함 (참가자 Shrushti Wakchaure 공유).
- **재신청 가능**: "You may submit another request as long as you're out of your current credits and there are still credits available for the Google team to give out." — 현재 크레딧을 소진했고 Google 팀에 남은 크레딧이 있으면 재신청 가능.
- **개인 지출 환급은 없음**: "We don't have a program for reimbursing personal funds already spent."
- 크레딧 소스는 Google Cloud 외에 **ClickHouse, Replit, Parallel, IBM** 각 파트너 리소스 페이지에도 있음.
- **Replit 크레딧 코드 신청 폼**: https://forms.gle/pwwvgDvbkgiRpADm6

### ⑱ ClickHouse 비용 절감

**A (Dustin Healy)** — 레플리카 수를 줄이고 서비스 스펙을 낮출 수 있다. **Settings 탭 → Scaling 섹션 → "Active Now" 카드 → 편집 버튼**에서 조정.

### ⑲ GCP 계정 생성 차단(OR_BACR2_31)

**Q** (Rao Huzaifa) "카드를 넣을 때마다 OR_BACR2_31 오류로 무료 체험 계정 생성이 막힙니다. 해외결제 가능·잔액 충분·주소 정확 확인했습니다."

**A (공식)** — 이 오류는 **Google Cloud 내부 검증 시스템에서 발생하며 Devpost/주최측이 우회해 줄 수 없다.** 해결책 3가지:
1. 해외 서비스용으로 설계된 **로컬 핀테크의 가상/외화 카드** 사용 — 일반 카드가 실패하는 경우 자주 성공
2. **Google Cloud Billing Support에 직접 문의** — 계정이 없어도 검증 홀드를 수동 해제해 줄 때가 있음
3. **우회 경로**: GCP 빌링이 끝내 안 되면 **Gemini API 액세스로 Google ADK를 쓰고 무료 티어 호스팅에 배포**해도 유효한 제출 경로다

### ⑳ Cloud Run 배포가 404를 반환하는 문제

**Q** (Daniel Nwaneri) 새 GCP 프로젝트에서 Cloud Run 서비스가 `Ready=True`이고 IAM도 맞는데 공개 `.run.app` URL이 Google 브랜드 404(GFE 레벨)를 반환하고 **요청 로그가 전혀 남지 않음**. 레지스트리·리전을 바꿔도 재현. Google 공식 퍼블릭 이미지로 한 대조 테스트는 정상 → 플랫폼 이슈로 추정.

**A (공식)**
1. 관련 커뮤니티 포럼 스레드를 인용해 **Google Cloud Support에 티켓 제출**
2. **컨테이너 리스닝 포트가 Cloud Run의 `PORT` 환경변수와 일치하는지 확인** — 불일치 시 이 증상이 난다
3. 주최측이 Google Cloud 파트너 컨택으로 에스컬레이션하겠다고 답변

### ㉑ Gemini API 쿼터 초과

**Q** (Yusra Irfan) "Gemini 이미지 생성에서 quota-exceeded. 8/31 크레딧 마감을 놓쳤습니다. 규칙에 맞는 이미지/영상 생성 대안이 있나요?"

**A (참가자 Supan Roy)** — "Use gemini-3.5-flash-lite, it has higher daily limit" (일일 한도가 더 높은 모델로 전환). *주최측 공식 답변은 아님.*

### ㉒ IBM Bob 접근 문제 (미해결 다수)

- **비즈니스 이메일 요구**: 인도 개인 참가자 Atchayam G가 Gmail로 가입 시 "Please use your business email address to continue"로 차단. Devpost/IBM에 개인 참가자용 프로비저닝 요청 → **답변 없음 (0 comments)**.
- 반면 다른 참가자(Dave Vockell, Akshay A)는 **"Google로 가입(sign up with Google)" 옵션을 쓰면 개인 이메일로도 가입됐다**고 공유. → 실무 우회법.
- **무료 크레딧이 1시간 만에 소진**: Dave Vockell — 무료 40 Bob coins가 1시간 만에 바닥. 추가 크레딧 없으면 "$200+ cost" 우려. → **주최측 답변 없음.**
- **Bob 백엔드 오류**: Imamu Frazier — "Request Failed Error while calling Bob's backend service" 반복. 주최측 "checking with the IBM team on this!" 이후 후속 없음.
- **IBM 트랙 증빙 요건**: Veronika Kashtanova — "IBM Bob 사용을 입증하지 못하면 IBM 트랙 요건 미달"이라는데, **구체적으로 어떤 증빙이 필요한가?** → **답변 없음 (0 comments).** ← IBM 트랙 참가자에게 실질적 리스크.

### ㉓ 파트너 트랙 공개 시점과 크레딧 지연

**Q** (List of sponsors 스레드) "남은 스폰서 공개는 언제인가? 한 달 전 낸 크레딧 신청은 어떻게 됐나?"

**A (공식)** — "We'll be announcing the remaining partner tracks soon - we just released 3 more partners today." / 크레딧은 "please allow 1-5 business days!"
이후 1주일이 지나도 코드가 안 왔고(스팸함에도 없음), 주최측은 **janet@devpost.com으로 직접 이메일하라**고 안내. 스레드는 미해결 상태로 종료.

### ㉔ GenAI SDK를 Gemini Enterprise Agent Platform에 연결하는 법

**Q** (Miguel Olave) "문서를 봐도 `gcloud login`이 shell console에서 유지되지 않고 API가 동작하지 않는다. 예제를 달라."

**A** — **답변 없음 (0 comments).**

---

## 3. 디스커션에서 드러난 참가자들의 주요 관심사/이슈

포럼은 총 **2페이지 / 약 31개 스레드**. 주제별 분포와 온도를 정리하면:

### (1) 압도적 1위 — Section 7.B AI 도구 제한 (최소 5개 스레드)

관련 스레드: `44739 AI tools`(3), `44644 Question about the AI usage limitation (Grafana track)`(4), `44942 development-time vs runtime`(1), `44968 Section 7.B ... development tools or only what the project runs`(4), `44940 Additional credits for a clean compliant rebuild`(3)

- **핵심 쟁점**: "개발 도구까지 Google 것만 써야 한다"는 규칙이 (a) 명시적으로 눈에 띄지 않았고 (b) 상식과 어긋나서, **이미 상당량을 만든 뒤에야 알게 된 참가자가 다수**였다.
- 그 결과 "코드를 전부 버리고 다시 짜야 하나" → "다시 짜느라 크레딧이 다 날아갔는데 추가 크레딧을 달라"로 이어지는 연쇄 이슈 발생 (44940이 그 대표 사례: 프로토타입 검증에 $100 중 $72 소진).
- **비용 형평성 불만**: 이미 다른 코딩 어시스턴트를 유료 구독 중인 참가자가 Google AntiGravity를 추가 구매해야 하는 문제.
- **경계선 질문이 대거 미답변**: 브레인스토밍용 ChatGPT, Gemini CLI + 유료 API 키, "왜 다른 에이전트를 금지하는가" 등.
- **실무적 시사점**: 제출 시 **README에 사용 툴링을 명시**하고, 서드파티 AI 산출물이 남아 있지 않은지 확인할 것. "리뷰만 했다"는 방어는 통하지 않는다.

### (2) 2위 — 크레딧 부족·미지급·환급 (최소 6개 스레드)

관련: `44622 List of sponsors`(8, 최다 댓글), `44827 GCP & ClickHouse credits clarification`(5), `44940`(3), `44913 My Bob free trial ran out in an hour`(2), `44709 Replit track ... credits`(2), `44919 IBM Bob`(1)

- **패턴이 매우 일관**: ① 신청했는데 코드가 안 옴(스팸함에도 없음) ② 받은 크레딧이 너무 빨리 소진됨 ③ 카드 등록 요구에 대한 거부감 ④ 이미 쓴 개인 돈은 환급 불가.
- **파트너별 무료 티어가 실제 개발에 부족하다**는 불만이 공통적: Replit 무료 티어는 "프롬프트 2번이면 한도 도달", IBM Bob 무료 40 coins는 "1시간 만에 소진".
- 주최측 대응은 대체로 "폼으로 재신청하라 / 1~5영업일 기다려라 / janet@devpost.com으로 메일하라" 수준. **개인 지출 환급 프로그램은 명시적으로 없다.**
- **거절 사례**: 우크라이나 NGO 대표가 비영리 인증(Microsoft·Google Ad Grants·TechSoup·Adobe·Canva 파트너십 보유)에도 불구하고 $100 크레딧을 **2회 연속 거절**당함 → 미답변.

### (3) 3위 — 트랙 요건의 정확한 해석 (최소 6개 스레드)

- **Replit**: "Agent로 빌드 + Replit 배포"만으로 충분한가? → 충분 (2개 스레드에서 동일 질문). 단 replit.app/dev 배포는 절대 요건.
- **IBM**: Bob만으로 되나 Confluent도 필요한가? → Bob만으로 충분, Confluent는 선택. 다만 **"Bob 사용 증빙"의 형식은 끝내 불명확**.
- **Parallel**: 호스팅 데모가 라이브 호출을 해야 하나? → 사전 생성 리플레이 허용.
- **ClickHouse**: 비용 절감법 위주.
- **공통 SDK 요건**이 반복 확인됨 — `google-adk` / `google-genai` / `google-generativeai` / `google-cloud-aiplatform` 중 하나를 런타임에 import·호출.
- **미해결 리스크**: "Vertex AI의 Google ADK 배포가 Agent Builder 요건을 충족하는가, Gemini Enterprise 배포가 필수인가" — 답변 없음. 많은 참가자가 여기에 걸릴 수 있음.

### (4) 자격(Eligibility) 관련 불안 (3개 스레드)

- 대회 시작 전 코드 → **탈락**. 폼의 'Existing' 옵션은 구제책이 아님.
- 정부기관 직원 → **일괄 배제**.
- 비적격 국가(브라질) → **참가·제출·갤러리 게재는 가능, 상금만 제외**.
- 자기 소유 IP(세계관) 재사용 → **미답변**.
- 공통점: 참가자들이 **개발에 시간을 쓰기 전에 확인하려 한다**는 것. 규칙이 엄격하게 해석된다는 인식이 퍼져 있음.

### (5) 인프라·플랫폼 장애 (3개 스레드)

- GCP 계정 생성 차단(OR_BACR2_31) — 특히 비미국권 참가자.
- Cloud Run `.run.app` 404 — 플랫폼 레벨 의심, `PORT` 불일치 점검 권고.
- Gemini API 쿼터 초과 — 이미지 생성 한도.
- IBM Bob 백엔드 오류 / 비즈니스 이메일 요구.
- → **주최측이 직접 해결할 수 없는 영역이 많고, "Google Cloud Support로 가라"로 귀결**되는 경향.

### (6) 상표·저작권/공개물 안전성

- 실시간 웹 검색 결과의 실제 회사명·URL 노출 문제. **답: 공개물은 mock, 라이브 데모는 실제.**
- 이 스레드(44673)는 댓글 6개로 상위권 — 팩트체킹·검색 기반 프로젝트가 많다는 방증.

### (7) 스코프 해석 — "Cinema"의 범위

- 참가자들이 "헐리우드급 프로덕션 도구여야 하나"를 걱정했고, 주최측이 **인디/유튜브/틱톡 크리에이터 도구를 적극 권장**한다고 명확히 답함. 이는 **아이디어 선택에 직접 영향을 주는 가장 유용한 공식 답변** 중 하나.

### (8) 기타

- 피드백 요청 스레드: `Flashframe — photosensitivity screening on the ClickHouse track` (ffmpeg로 프레임 밝기 추출 → ClickHouse MCP로 스트리밍 → SQL로 UK Ofcom 2.12 / ITU-R BT.1702 위반 탐지 → Gemini가 원인 판정). 실제 제출작 수준의 완성도를 보여주는 사례. 응답 없음.
- 잡담성 스레드 1건 (`AI` — "AI가 생산성을 높이나 낮추나", 댓글 0).
- 포르투갈어 스레드 1건 (브라질 참가자) — 국제 참가 비중을 보여줌.

### 종합 인상

> **이 대회의 최대 함정은 기술이 아니라 규칙이다.**
> ① 개발 도구까지 Google 것만 허용하는 Section 7.B, ② 7/27 이후 신규 프로젝트만 허용, ③ 트랙별 배포/SDK 요건 — 이 셋에서 탈락 위험이 집중된다.
> 반면 크레딧 만료·라이브 데모 유지는 **데모 영상으로 충분히 방어 가능**하다는 것이 공식 입장이므로 과도하게 걱정할 필요가 없다.

---

## 4. 참가자 현황

| 항목 | 값 |
|---|---|
| 총 등록 참가자 | **9,904명** |
| 참가 상태 | 마감 시점까지 등록 오픈 |
| 마감 | 2026-09-09 14:00 PDT |
| 스킬 분포 / 팀 구인 통계 | **비공개** — "Please log in to browse this hackathon's participants" (Devpost 로그인 필요) |

- `/participants` 페이지는 **로그인하지 않으면 총원 숫자만 노출**되고, 스킬 브레이크다운·팀 빌딩(구인 중) 통계·필터는 볼 수 없다.
- 포럼 활동으로 유추되는 참가자 구성:
  - **국제 참가 비중이 높다** — 인도, 브라질, 우크라이나, 파키스탄, 일본, 나이지리아 등에서의 글이 확인됨.
  - **개인/솔로 참가자가 많다** — 팀 결성 관련 스레드가 사실상 없고, 대신 "개인 이메일로 IBM Bob 가입이 안 된다", "무료 티어가 부족하다" 같은 **개인 참가자 특유의 리소스 문제**가 포럼 상위를 차지한다.
  - 9,904명 등록 대비 포럼 스레드는 31개로, **활발히 완주 중인 참가자 비율은 훨씬 작을 가능성**이 높다.

---

## 5. 실행 체크리스트 (위 내용에서 도출)

- [ ] **개발 전 과정에서 Google 계열 AI 도구 + 트랙 파트너 내장 AI만 사용**했는지 확인 (Gemini CLI / Gemini Code Assist / AntiGravity / Vertex AI). Google Stitch는 불가.
- [ ] README에 **사용한 AI 툴링을 명시적으로 문서화**.
- [ ] 리포·코드가 **2026-07-27 이후 신규 생성**인지 확인. 제출 폼의 'Existing'은 면책이 아님.
- [ ] 런타임에 `google-adk` / `google-genai` / `google-generativeai` / `google-cloud-aiplatform` 중 하나를 **실제로 import·호출**.
- [ ] 선택한 트랙의 고유 요건 충족:
  - Replit → Replit Agent로 빌드 + **replit.app/replit.dev에 배포**
  - IBM → **IBM Bob 사용 증빙** (Confluent는 선택)
  - Parallel → 리포/영상에서 **런타임 Parallel Search 호출이 명확히 보이게**, 공개물의 서드파티 이름·URL은 mock
  - ClickHouse → MCP 서버 경유 실시간 데이터 레이어
  - Grafana → Grafana Cloud MCP + ADK
- [ ] **데모 영상에서 end-to-end 동작을 완전히 보여줄 것** — 크레딧 만료 후 라이브가 죽어도 이것이 심사 근거가 된다.
- [ ] 공개 자료(영상·스크린샷)에 **실제 제3자 상표/도메인 노출 금지** (mock 사용).
- [ ] 제출물 3종 준비: **호스팅된 Project URL + 데모 영상 + 리포**.
