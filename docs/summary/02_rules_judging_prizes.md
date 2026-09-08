# Agentic Cinema: The Blockbuster Hackathon — 규정 · 심사 · 상금 정리

출처
- https://agentic-cinema.devpost.com/rules (공식 Official Rules)
- https://agentic-cinema.devpost.com/details/dates (일정)
- https://agentic-cinema.devpost.com/ (개요)

주최 정보
- **Sponsor**: Google LLC — 1600 Amphitheater Parkway, Mountain View, CA 94043
- **Administrator**: Devpost, Inc. — 222 Broadway, Floor 19, New York, NY 10038
- **문의**: support@devpost.com / 개인정보 관련 googlecloudnexthackathon@google.com

---

## 1) 참가 자격 (Eligibility)

### 1-1. 연령 / 거주지
- 거주 국가·주·지역의 **성년 연령 이상**이어야 함.
  > "be above the age of majority in the country, state, province or jurisdiction of residence (or at least twenty years old in Taiwan)"
  - 대만 거주자는 **만 20세 이상**.
  - 한국 거주자는 성년(만 19세 이상)이면 참가 가능.

### 1-2. 참가 불가 국가·지역 (거주자 기준)
아래 국가·지역 **거주자는 참가 불가**:

| 구분 | 목록 |
| --- | --- |
| 국가 | Italy(이탈리아), Brazil(브라질), Cuba, Iran, Syria, North Korea, Sudan, Belarus, Russia, Afghanistan, China(중국), Djibouti, Iraq, Kazakhstan, Somalia, Venezuela, Vietnam(베트남) |
| 지역 | Quebec(캐나다 퀘벡주), Crimea, Donetsk 및 Luhansk 지역(우크라이나), Antarctica, Western Sahara |

> 원문: "OPEN TO EVERYONE EXCEPT FOR RESIDENTS OF" + 위 목록

**한국(대한민국)은 제외 목록에 없음 → 참가 가능.**

### 1-3. 참가 불가 인원 (관계자)
> "Employees, interns, contractors, and official office-holders of Google, the Partner Entities ... and their parent companies, subsidiaries, affiliates ... are ineligible to participate"

- Google, 파트너사(IBM, Grafana Labs, Parallel, ClickHouse, Replit), Devpost 및 그 모회사·자회사·계열사의 **임직원, 인턴, 계약직, 임원**
- 위 인원의 **직계 가족 및 동거 가족**도 불가

### 1-4. 팀 구성
- **최대 4인** (`"limited to a maximum of four (4) individuals"`)
- 팀원 전원이 개별적으로 자격 요건을 충족해야 하며, **Devpost 프로젝트에 전원 등록**되어야 함
- 팀/단체는 **대표자 1인(Representative)** 지정 필요
- 여러 팀에 소속 가능하되, 각 제출물이 고유하고 실질적으로 달라야 함
  > "join more than one team or organization with a unique and substantially different Submission"

### 1-5. 다중 제출
- 개인/팀은 **여러 건 제출 가능**
- 단, 각 제출물은 **고유하고 실질적으로 달라야 함**
  > "each Submission must be unique and substantially different"
- 실질적 차이 여부의 판단은 **주최측 재량**

---

## 2) 일정 (PDT / KST 병기)

> KST = PDT + 16시간

| 항목 | PDT (현지) | KST (한국) |
| --- | --- | --- |
| 제출 시작 (Submission Period 개시) | 2026-07-27 (월) 1:45 PM PDT ※공식 규정 본문은 9:00 AM PT 표기 | 2026-07-28 (화) 05:45 (또는 2026-07-28 01:00) |
| **제출 마감 (Deadline)** | **2026-09-09 (수) 2:00 PM PDT** | **2026-09-10 (목) 06:00** |
| 심사 기간 시작 | 2026-09-10 (목) 12:00 PM PDT ※규정 본문은 9/23 시작 표기 | 2026-09-11 (금) 04:00 |
| 심사 기간 종료 | 2026-10-08 (목) 12:00 PM PDT ※규정 본문은 10/7 종료 표기 | 2026-10-09 (금) 04:00 |
| 수상자 개별 통보 | 약 2026-10-07 전후 (전화 또는 이메일) | — |
| **수상자 발표 (Winners Announced)** | **2026-10-13 (화) 12:00 PM PDT** | **2026-10-14 (수) 04:00** |
| 수상자 명단 공개 (Winners List) | 2026-10-12 이후 | — |

> 주의: Dates 페이지와 Official Rules 본문의 시각 표기가 일부 다름(제출 시작 1:45PM vs 9:00AM, 심사 기간 9/10~10/8 vs 9/23~10/7). **가장 중요한 제출 마감 `September 9, 2026 2:00 PM PDT`는 양쪽 일치**하므로 이를 절대 기준으로 삼을 것.

기타 기한
- **Google Cloud $100 크레딧 신청 마감: 2026-08-31 11:59 PM PST**
- 수상 통보 후 **영업일 2일(two business days) 내 응답** 필수, 미응답 시 실격
- 자격 증빙 서류 제출도 **2일 내** 완료 필요

---

## 3) 제출 요구사항 체크리스트

### 3-1. 무엇을 만들어야 하나 (What to Create)
- **Gemini + Google Cloud Agent Builder** 기반의 **작동하는(production-ready) AI 에이전트 또는 멀티에이전트 네트워크**
- **파트너 제품 1개 이상 통합** (선택한 트랙에 해당)
- 대상 도메인: **영화·미디어·엔터테인먼트 워크플로**(영화 제작자, 시나리오 작가, 제작진, 팬 대상)
- 실행 플랫폼: `"at least one of the following platforms: web, Android, or iOS"`

### 3-2. Google Cloud 사용 요건 (필수 · 배타적)
- Gemini models on Agent Platform, BigQuery ML 및 관련 API 사용
- **다른 벤더의 AI 사용 전면 금지**
  > "No other AI models, agent frameworks, or AI APIs are permitted, regardless of vendor — this includes but is not limited to AWS, Microsoft, OpenAI, and Anthropic AI tools"
  - 예외: 파트너 제품에 내장된 AI 기능은 허용
  - **⚠️ Claude/Anthropic, OpenAI, AWS Bedrock 등 사용 시 실격**

### 3-3. 트랙별 파트너 제품 요건

| 트랙 | 필수 조건 (원문) |
| --- | --- |
| **IBM** | "your project must be built using IBM Bob as part of the development process" — 개발 과정에서 IBM Bob 사용 필수. Confluent는 선택(권장) |
| **Grafana Labs** | "your project must actively use the Grafana stack at runtime, primarily through the Grafana Cloud MCP server" — 런타임에 Grafana Cloud MCP 서버 실사용 |
| **Parallel** | "your project must actively use Parallel's Search API at runtime" — 런타임에 Parallel Search API 실사용 |
| **ClickHouse** | "your project must actively use ClickHouse at runtime via the official ClickHouse MCP server" — 공식 ClickHouse MCP 서버로 클러스터 연결 |
| **Replit** | "the finished project must be hosted and deployed directly on Replit" — Replit Agent로 빌드하고 Replit에 배포 |

### 3-4. 제출물 체크리스트

- [ ] **Devpost 제출 폼** 작성 및 트랙 선택
- [ ] **텍스트 설명 (Text Description)**
  - [ ] 기능/동작 요약
  - [ ] 사용 기술 스택
  - [ ] 데이터 소스 정보
  - [ ] 프로젝트에서 얻은 발견/배운 점(findings and learnings)
- [ ] **데모 영상 (Demo Video)**
  - [ ] **최대 3분** — `"longer submissions evaluated only to 3-minute mark"` (초과분은 심사 대상 아님)
  - [ ] 의도한 플랫폼에서 **실제 동작하는 모습**을 보여줄 것
  - [ ] **YouTube 또는 Vimeo에 업로드**, **공개(public)** 설정
  - [ ] **영어 음성 또는 영어 자막** 필수
  - [ ] 제3자 광고·슬로건·로고·상표·저작물 포함 금지
  - [ ] 비방·모욕·성적·욕설·불법 콘텐츠 금지
  - [ ] 원작이며 미공개작이어야 함
- [ ] **코드 저장소 URL**
  - [ ] **공개 저장소** (GitHub / GitLab / Bitbucket)
  - [ ] **OSI 승인 오픈소스 라이선스 파일이 최상단에서 탐지 가능**해야 함 (`"open-source license file detectable at the top"`)
  - [ ] 전체 소스코드 + 에셋 + 실행 방법(instructions) 포함
  - [ ] Google Cloud 및 파트너 서비스가 **실제로 import되고 호출되는 것이 코드에서 확인 가능**해야 함 — `"imported and actually called ... not just named in the README"`
- [ ] **호스팅된 프로젝트 URL** — 심사·테스트용 (`"a URL to the hosted Project for judging and testing"`)
- [ ] **언어**: 모든 서면 제출물은 **영어** (`"Written parts of entries must be in English"`)

> 아키텍처 다이어그램은 규정상 **명시적 필수 항목이 아님** (권장 수준). 단, 심사 기준 Technological Implementation·Design 점수에 유리하므로 포함 권장.

### 3-5. 신규 프로젝트 요건 (매우 중요)
> "Projects must be newly created by the entrant during the Contest Period. The Project must be Your original creation not a modification or extension of Your or anyone else's existing work."

- **대회 기간 중 새로 만든 프로젝트만 인정**
- 본인 또는 타인의 **기존 작업물의 수정·확장은 불가**

### 3-6. 제출 후 수정 (SUBMISSION MODIFICATIONS) — 원문
> "Prior to the end of the Contest Period, you may save draft versions of your submission on Devpost to your portfolio before submitting the Submission materials to the Contest for evaluation. Once the Contest Period has ended, you may not make any changes or alterations to your Submission, but you may continue to update the Project in your Devpost portfolio. After the Contest Period, fully at their discretion, the Sponsor and Devpost may permit you to modify part of your Submission after the Contest Period for the purpose of adding, removing or replacing material that potentially infringes a third party mark or right, discloses personally identifiable information, or is otherwise inappropriate. The modified Submission must remain substantively the same as the original Submission with the only modification being what the Sponsor and Devpost permits."

요약: 마감 후에는 **일절 수정 불가**. 예외적으로 상표·저작권 침해 소지, 개인정보 노출, 부적절 콘텐츠 제거 목적에 한해 주최측 재량으로 허용될 수 있으며, 그 경우에도 **실질적으로 동일**해야 함.

---

## 4) 심사 기준 (Judging Criteria)

### 4-1. Stage One — Pass/Fail 스크리닝
> "The first stage will determine via pass/fail whether the Submission meets a baseline level of viability, in that the Submission includes all Submission requirements, reasonably addresses the challenge and reasonably applies both the required data provided by Partner and Google Cloud products."

- 제출 요건 전부 충족 여부 + 챌린지 부합 여부 + 파트너 데이터/Google Cloud 제품의 합리적 적용 여부를 **통과/탈락**으로 판정
- **자동화 도구(automated tools)의 보조로 진행될 수 있음** → 저장소·라이선스·URL 등 기계적으로 검증 가능한 항목 누락 시 즉시 탈락 위험

### 4-2. Stage Two — 4개 기준, **동일 가중치 (각 25%, 퍼센트 명시는 없고 "equally weighted")**

| # | 기준 (원문) | 원문 설명 | 한글 |
| --- | --- | --- | --- |
| 1 | **Technological Implementation** | "How well is the project built, and how effectively does it use Google Cloud and the Partner services as part of the solution?" | 프로젝트가 얼마나 잘 만들어졌는가, 그리고 Google Cloud와 파트너 서비스를 솔루션의 일부로서 얼마나 효과적으로 활용했는가 |
| 2 | **Design** | "Does the project deliver a complete, coherent product experience not just a technical proof of concept?" | 단순 기술 PoC가 아니라 완결적이고 일관된 제품 경험을 제공하는가 |
| 3 | **Potential Impact** | "Does the project make a credible, specific case for solving a real problem for a real audience and does the solution actually address it based on what's demonstrated?" | 실제 사용자층의 실제 문제를 해결한다는 구체적·설득력 있는 논거가 있는가, 그리고 시연된 내용상 실제로 그 문제를 해결하는가 |
| 4 | **Quality of the Idea** | "Is this a creative, non-obvious use of Google Cloud and the Partner services and does the team show genuine understanding of the problem space?" | Google Cloud와 파트너 서비스를 창의적이고 비자명하게 사용했는가, 팀이 문제 영역을 진정으로 이해하고 있는가 |

### 4-3. 수상자 결정 · 동점 처리
- 각 **트랙별로 최고 점수** 제출물이 잠정 수상자로 선정
- 동점 시: `"comparing scores on each criterion in the order listed"` — **위 표의 순서대로 개별 기준 점수를 비교**
  1. Technological Implementation → 2. Design → 3. Potential Impact → 4. Quality of the Idea
- 그래도 동점이면 **심사위원 투표**

### 4-4. 통보 절차
- 2026-10-07 전후, **전화 또는 이메일**로 통보
- **영업일 2일 내 응답 필수** → 미응답 시 실격, 차순위 제출물로 대체
- 자격 선언서(eligibility declaration) 및 필요 서류를 **2일 내** 제출하지 않으면 상금 몰수
- 검증 조항:
  > "THE AWARD OF A PRIZE TO A POTENTIAL WINNER IS SUBJECT TO VERIFICATION OF THE IDENTITY, QUALIFICATIONS AND ROLE OF THE POTENTIAL WINNER IN THE CREATION OF THE SUBMISSION."
- 당첨 확률: `"Odds of winning any prize depends on the number of eligible entries received during the Contest Period and the skill of the entrants."`

---

## 5) 상금 (Prizes)

**총상금 $75,000 USD** — 5개 트랙 × 트랙당 $15,000, 트랙별 구조 동일.

| 트랙 | 1위 | 2위 | 3위 | 트랙 합계 |
| --- | --- | --- | --- | --- |
| IBM | $7,500 + 소셜미디어 홍보 기회 | $4,500 | $3,000 | $15,000 |
| Grafana Labs | $7,500 + 소셜미디어 홍보 기회 | $4,500 | $3,000 | $15,000 |
| Parallel | $7,500 + 소셜미디어 홍보 기회 | $4,500 | $3,000 | $15,000 |
| ClickHouse | $7,500 + 소셜미디어 홍보 기회 | $4,500 | $3,000 | $15,000 |
| Replit | $7,500 + 소셜미디어 홍보 기회 | $4,500 | $3,000 | $15,000 |
| **합계** | $37,500 | $22,500 | $15,000 | **$75,000** |

각 등수는 트랙당 **1명(1팀)**.

### 없는 것 (확인됨)
- **그랜드 프라이즈(전체 대상) 없음** — 트랙별 1~3위만 존재
- **Honorable Mention 없음**
- **보너스 상금 없음**
- 상금 외 비현금 부상은 **1위의 소셜미디어 홍보 기회**뿐

### Google Cloud 크레딧 (상금 아님, 참가 지원)
> "Access to Google Cloud may be obtained by (1) signing up for a no cost trial at https://cloud.google.com/free or (2) using an existing Google Cloud account for which you may request $100 in Google Cloud credits by completing this form by August 31st, 2026 11:59 PM PST."

- $100 크레딧, **2026-08-31 11:59 PM PST까지 폼 작성** 필요
- **보장되지 않음** — `"not guaranteed"`, `"at Google's discretion"`
- 크레딧 초과 사용분의 요금은 **참가자 부담**

### 세금
> "Winners are responsible for reporting and paying all applicable taxes"
- 수상자가 자국 세법에 따라 신고·납부 책임. 주최측이 세무 목적으로 상금 일부를 원천징수할 수 있음.

---

## 6) 지적재산권 · 기타 조항

### 6-1. INTELLECTUAL PROPERTY RIGHTS (원문)
> "By submitting a Submission in this Contest, the entrant hereby licenses and will license the Non-Proprietary Aspects (as defined below) of the Submission and the source code used to generate the Submission under an Open Source Initiative-approved license (see www.opensource.org) that in no event limits commercial use of such code or model containing or depending on such code. As defined above, 'Non-Proprietary Aspects' means any Google products and services used to generate the Submission and other third party software that is commercially available software not owned by the submitter individual or organization used to generate the Submission.
>
> To the extent your or your team or organization's Submission makes use of generally commercially available software not owned by you or your team or organization that was used to generate the Submission, but that can be procured by Google or Partner without undue expense, you do not grant the license in the preceding sentence to that software.
>
> As between Google and the entrant, the entrant retains ownership of all intellectual and industrial property rights (including moral rights) in and to any videos provided for the Contest. As a condition of entry, entrant grants Google, its subsidiaries, agents and Partners, a perpetual, irrevocable, worldwide, royalty-free, and non-exclusive license to use, reproduce, adapt, modify, publish, distribute, publicly perform, create a derivative work from, and publicly display such video(s) (1) for the purposes of allowing Google and its affiliates and the Judges to evaluate the video for purposes of the Contest, and (2) in connection with advertising and promotion via communication to the public or other groups, including, but not limited to, the right to make screenshots, animations and video clips available for promotional purposes."

정리
- 제출물의 **Non-Proprietary Aspects**와 생성에 사용된 소스코드는 **OSI 승인 라이선스(상업적 이용 제한 없는)** 로 공개해야 함 → 실질적으로 **저장소 오픈소스화 의무**
- 데모 영상의 **소유권은 참가자에게 유지**되나, Google·파트너에게 **영구·취소불가·전세계·무상·비독점 라이선스** 부여 (심사 목적 + 광고/홍보 목적, 2차 저작물 제작 포함)

### 6-2. 진술 및 보증 (Warranties)
- 제출물이 본인의 **원작**이며 필요한 모든 권리를 보유
- 제3자의 지적재산권·프라이버시권·퍼블리시티권을 침해하지 않음
- 사용한 모든 데이터에 대한 라이선스를 보유

### 6-3. 면책 (Indemnification)
> "indemnify and keep indemnified"
- 아래 사유로 인한 책임에 대해 Contest Entities를 면책:
  제출물의 IP 침해 / 허위 진술 / 규정 위반 / 제3자 청구 / 상금 사용·오용

### 6-4. 퍼블리시티
- 상금 수령 시, Sponsor·Partner가 수상자의 **성명·초상·제출물을 추가 보상 없이 광고 및 홍보 목적으로 사용**하는 데 동의한 것으로 간주

### 6-5. 개인정보
- Google이 자사 Privacy Policy에 따라 개인정보 수집. 파트너사는 각자의 정책에 따라 처리
- 열람·삭제 요청: googlecloudnexthackathon@google.com

### 6-6. 일반 조건
- Google은 부정행위·기만·불공정 행위·괴롭힘 시 `"disqualify any entrant"` 가능
- 대회 무결성이 훼손되면 Sponsor가 `"cancel, terminate, modify or suspend"` 가능

---

## 7) 주의해야 할 실격 사유 (Disqualification Risks)

### 🔴 즉시 실격 — 절대 금지
1. **Google Cloud 외 AI 벤더 사용** — OpenAI, Anthropic(Claude), AWS, Microsoft의 AI 모델·에이전트 프레임워크·AI API 일체 사용 금지. (파트너 제품 내장 AI 기능만 예외)
2. **기존 프로젝트 재활용** — 대회 기간 이전에 만든 것, 또는 기존 작업물의 수정·확장 제출
3. **신원·연락처·권리 보유에 관한 허위 기재** — `"immediate elimination"`
4. **제출 프로세스 조작(tampering)**
5. **참가 불가 국가 거주 또는 관계사 임직원**

### 🟠 Stage One에서 탈락하기 쉬운 항목 (자동 검증 대상)
6. **코드 저장소가 비공개(private)**
7. **OSI 승인 오픈소스 라이선스 파일이 저장소 최상단에 없음**
8. **README에만 언급하고 실제 코드에서 Google Cloud/파트너 서비스를 호출하지 않음** — `"not just named in the README"`
9. **호스팅된 프로젝트 URL 미제공** 또는 심사 시점에 접속 불가
10. **데모 영상이 비공개/제한 공개**, 또는 YouTube·Vimeo가 아닌 플랫폼
11. **트랙별 파트너 제품 필수 요건 미충족** (예: Grafana 트랙인데 런타임에 MCP 서버를 안 씀)
12. **영어 미사용** — 서면 제출물이 영어가 아니거나 영상에 영어 자막 없음
13. **web/Android/iOS 중 어느 플랫폼에서도 실행되지 않음**

### 🟡 감점·리스크 요인
14. **데모 영상 3분 초과** — 3분 이후는 심사에서 **아예 보지 않음**. 핵심 데모를 앞부분에 배치할 것
15. **영상 내 제3자 로고·상표·저작권 있는 음악/영상 사용** (영화 클립, 상용 BGM 특히 주의 — 영화 도메인 해커톤이라 위험이 큼)
16. **팀원을 Devpost 프로젝트에 등록하지 않음** — 상금 배분/자격 검증 불가
17. **마감 후 수정 시도** — 불가능. 마감 시각 기준 상태로 고정
18. **수상 통보 후 영업일 2일 내 무응답** — 실격 및 차순위 승계
19. **중복성 있는 다중 제출** — "unique and substantially different" 미충족 시 주최측 재량으로 무효

### ✅ 마감 직전 최종 점검 (KST 2026-09-10 06:00 이전)
- [ ] 저장소 public + LICENSE 파일 루트에 존재 (OSI 승인, 상업적 이용 허용)
- [ ] 코드에서 Gemini/Agent Builder 및 파트너 SDK 실제 호출 확인
- [ ] 호스팅 URL 외부 접속 테스트 (시크릿 브라우저)
- [ ] 데모 영상 YouTube/Vimeo Public, 3분 이내, 영어(또는 영어 자막)
- [ ] Devpost 폼: 트랙 선택, 텍스트 설명 4요소(기능/기술/데이터소스/배운 점), 팀원 전원 등록
- [ ] 저작권 있는 영화·음악 클립 미사용 재확인
