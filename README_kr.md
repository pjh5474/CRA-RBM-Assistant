# CRA-RBM Assistant

CRA-RBM Assistant는 공개 임상시험 정보와 합성(synthetic) 사이트 모니터링 데이터를 구조화하여, 임상시험 코디네이터(CRA)의 모니터링 준비를 지원하기 위한 프로토타입 웹 애플리케이션입니다.

CRA 모니터링 개념을 구조화된 데이터 워크플로, 검토 대시보드, 이슈 추적, 보고서 초안 생성으로 옮기는 데 초점을 둡니다.

이 프로젝트는 프로토콜 검토, 사이트 모니터링 준비, 쿼리/일탈 후속 조치, 위험 기반 모니터링(RBM)과 관련된 핵심 워크플로를 구현함으로써 백엔드 개발, 데이터 품질 관리, 임상 연구 운영을 연결합니다.

## Live Demo (라이브 데모)

- **프론트엔드:** https://cra-rbm-assistant.vercel.app
- **백엔드 API 문서:** https://cra-rbm-assistant.onrender.com/docs

> **참고:** 백엔드는 Render 무료 플랜에 호스팅되어 있습니다. 유휴 상태 후 첫 요청 시 응답까지 시간이 걸릴 수 있습니다(cold start).

## Deployment (배포)

배포 구성:

- **Frontend:** Vercel
- **Backend:** Render
- **Database/Auth:** Supabase

모노레포에서 루트 디렉터리를 분리해 프론트엔드와 백엔드를 각각 배포합니다.

- **Vercel root directory:** `frontend`
- **Render root directory:** `backend`

## 1. 프로젝트 배경

CRA(Clinical Research Associate)는 프로토콜 준수, 피험자 안전, 데이터 무결성, 필수 문서 준비 상태, 시험용 의약품 관리, 사이트 성과 모니터링을 통해 임상시험 품질을 지원하는 역할을 합니다.

임상시험이 더욱 데이터 중심·위험 기반으로 운영됨에 따라, CRA는 규정과 문서뿐 아니라 데이터 흐름, 시스템 사용, 쿼리 관리, 사이트별 위험 지표도 이해해야 합니다.

본 프로젝트는 소프트웨어 엔지니어링 및 데이터 관리 경험이 CRA 관련 워크플로에 어떻게 적용될 수 있는지 보여 주기 위한 포트폴리오 프로젝트로 개발되었습니다.

### 커리어 전환 맥락

데이터 관리·소프트웨어 개발 경험을 바탕으로 CRA 역할로 전환하기 위한 포트폴리오 프로젝트입니다.

데이터 품질 관리, 이슈 추적, API 개발, 데이터베이스 설계, 대시보드 구현이 CRA 모니터링 워크플로에 적용되는 방식을 보여 줍니다.

이 프로젝트가 보여 주는 핵심 역량:

- 운영 데이터를 검토 가능한 워크플로로 구조화
- 누락·대기·만료·미해결 항목 추적
- 위험 지표와 CRA 후속 조치 연결
- 사이트 수준 데이터를 모니터링 보고서 초안으로 변환
- 데이터 변경에 대한 감사(audit) 유사 추적성 적용
- 임상시험 운영, 데이터 품질, 모니터링 준비 간 관계 이해

## 2. 프로젝트 목표

CRA 지향 모니터링 지원 프로토타입을 구축하여 다음을 수행합니다.

- 임상 연구 정보 가져오기 또는 정의
- 프로토콜 관련 핵심 요소 추출
- SIV·IMV 체크리스트 항목 생성
- 합성 사이트 모니터링 데이터 관리
- 사이트별 위험 점수 계산
- 고위험 사이트에 대한 CRA 후속 조치 제안

본 애플리케이션은 실제 환자 데이터나 기밀 임상시험 문서를 사용하지 않습니다. 모든 사이트 수준 데이터는 포트폴리오·교육 목적으로만 생성된 합성 데이터입니다.

## 3. 주요 기능

### Study Overview (연구 개요)

다음과 같은 구조화된 연구 정보를 표시합니다.

- 연구 제목
- Phase(단계)
- 적응증(Indication)
- 연구 설계
- 중재(Intervention)
- 대조군(Comparator)
- 1차 평가변수(Primary endpoint)
- 2차 평가변수(Secondary endpoint)
- 선정 기준(Inclusion criteria)
- 제외 기준(Exclusion criteria)

### CRA Checklist Generator (CRA 체크리스트 생성)

다음 항목에 대한 CRA 지향 체크리스트를 제공합니다.

- SIV(Site Initiation Visit, 사이트 개시 방문)
- IMV(Interim Monitoring Visit, 중간 모니터링 방문)
- 필수 문서 검토
- 동의서(ICF) 검토
- 적격성 검토
- 안전성 보고 절차
- 시험용 의약품 관리
- 원시자료·eCRF 일치성

### Site Risk Dashboard (사이트 위험 대시보드)

합성 모니터링 데이터로 사이트 모니터링 정보와 계산된 위험 점수를 시각화합니다.

- 등록(Enrollment) 진행률(표시용, 점수 미반영)
- Open query 수
- Query 경과 일수
- 프로토콜 일탈 건수
- SAE 보고 지연
- 누락 필수 문서
- IP 관리·ICF 이슈(risk factors로 표시)
- 위험 점수(Risk score)
- 위험 수준(Risk level)

### CRA Follow-up Action Items (CRA 후속 조치)

감지된 사이트 위험에 따라 다음과 같은 후속 조치를 제안합니다.

- Query 해결 후속
- 프로토콜 일탈 근본 원인 검토
- SAE 보고 절차 재교육
- 필수 문서 대조(reconciliation)
- 사이트 스태프 재교육 검토

### ClinicalTrials.gov Study Import (공개 연구 가져오기)

ClinicalTrials.gov API를 이용한 공개 임상시험 등록부 검색 및 미리보기를 지원합니다.

현재 기능:

- 키워드로 공개 임상시험 검색
- NCT ID, 제목, phase, 질환, 중재, 연구 설계, outcomes, 선정·제외 기준 미리보기
- 선택한 공개 연구를 Supabase PostgreSQL에 import
- import된 연구에 대한 합성 데모 사이트·모니터링 지표 자동 생성
- 기존 Study Overview·Risk Dashboard 워크플로에 import 연구 표시
- import 상태를 created(신규) / updated(갱신)로 구분

### Trigger-based Audit-like Logs (트리거 기반 감사 유사 로그)

PostgreSQL 트리거 기반 변경 로그로 데이터 변경 추적성 개념을 시연합니다.

추적 대상:

- studies / sites / monitoring_metrics의 insert·update·delete
- JSONB를 이용한 변경 전·후 데이터 비교

규제용 검증된 audit trail이 아니며, 추적성 개념 시연용입니다.

### Site Review Hub (사이트 검토 허브)

사이트 위험, 문서 준비 상태, 프로토콜 일탈, ICF 버전 이슈, 모니터링 보고서 초안 접근을 한 페이지에 통합합니다.

CRA 모니터링 준비를 사이트 단위로 조직할 수 있음을 보여 줍니다.

### Enhanced Monitoring Report Draft (강화된 모니터링 보고서 초안)

다음을 통합한 IMV 스타일 모니터링 보고서 초안을 생성합니다.

- 사이트 위험 요약
- 필수 문서 준비 상태 소견
- 프로토콜 일탈 소견
- ICF 버전 관리 소견
- CRA 후속 조치 계획

구조화된 모니터링 데이터가 CRA 문서 작성 준비를 어떻게 지원하는지 시연합니다.

### Essential Document Readiness Tracker (필수 문서 준비 추적)

합성 문서 레코드로 사이트별 필수 문서 상태를 추적합니다.

문서 상태:

- Ready(준비 완료)
- Missing(누락)
- Pending(대기)
- Expired(만료)

준비 점수(readiness score)를 계산하고 문서 관련 후속 필요 사항을 요약합니다.

### Protocol Deviation Tracker (프로토콜 일탈 추적)

다음 기준으로 프로토콜 일탈을 추적합니다.

- Category(범주)
- Severity(심각도)
- Status(상태)
- Subject code(피험자 코드)
- Root cause(근본 원인)
- Corrective action(시정 조치)
- Preventive action(예방 조치)

단순 건수를 넘어 이슈 분류·후속 추적을 시연합니다.

### ICF Version Control Check (ICF 버전 관리 점검)

피험자 동의 기록이 동의일 기준 유효했던 ICF 버전과 일치하는지 확인합니다.

날짜 기반 버전 일치 검증으로 데이터 품질 로직과 CRA 동의서 검토를 연결합니다.

### Authentication and Import Protection (인증 및 Import 보호)

Supabase Auth로 쓰기 작업을 보호합니다.

로그인 없이 대시보드·CRA 워크플로 페이지를 조회할 수 있으며, Supabase 레코드를 생성·수정하는 ClinicalTrials.gov import는 인증이 필요합니다.

## 4. 시스템 아키텍처

### 현재 아키텍처

```
Next.js Frontend
        ↓
FastAPI Backend (app/api/ 라우터 모듈)
        ↓
Supabase PostgreSQL
        ↓
CRA Review Services
```

**백엔드 서비스 예시**

- Risk Scoring Service
- Action Item Service
- Site Review Summary Service
- Monitoring Report Draft Service
- Essential Document Readiness Service
- Protocol Deviation Service
- ICF Version Check Service

→ CRA Dashboard / Site Review Hub

### 외부 연구 Import 흐름

```
ClinicalTrials.gov API
        ↓
FastAPI External Study Import API
        ↓
Supabase PostgreSQL
        ↓
합성 운영 데모 데이터 생성
  - 데모 사이트
  - 모니터링 지표
  - 필수 문서
  - 프로토콜 일탈
  - ICF 버전·피험자 동의
        ↓
Site Review Hub / Risk Dashboard / Monitoring Report Draft
```

### 인증 범위

```
비로그인 사용자
  → 대시보드·사이트 리뷰·감사 로그 등 읽기 전용 조회

로그인 사용자 (Supabase Auth)
  → ClinicalTrials.gov 연구 Import (Supabase 쓰기)
```

### 계획된 자동화 아키텍처

```
n8n Scheduled Workflow
        ↓
FastAPI High-risk Site Alert API
        ↓
Slack / Discord / Email Notification
```

## 5. 데이터 출처

공개 연구 수준 데이터와 합성 사이트 운영 데이터를 분리합니다.

**공개 데이터**

- ClinicalTrials.gov 공개 등록부
- NCT ID, 제목, phase, 질환, 중재, outcomes, 선정·제외 기준

**합성 데모 데이터**

- 사이트 정보
- 모니터링 지표
- 필수 문서 상태
- 프로토콜 일탈
- ICF 버전·피험자 동의
- CRA 후속 조치
- 모니터링 보고서 초안 입력값

실제 피험자·환자 데이터, 실제 사이트 성과, 기밀 스폰서 프로토콜, 독점 임상시험 문서는 사용하지 않습니다.

## 6. MVP 범위

현재 MVP는 공개 연구 수준 데이터와 합성 사이트 운영 데이터로 CRA 지향 사이트 검토 워크플로를 시연합니다.

포함 항목:

- ClinicalTrials.gov 공개 연구 검색·상세 미리보기
- 인증 기반 공개 연구 Supabase import
- import 연구에 대한 합성 운영 데이터 자동 생성
- Study overview·Site risk dashboard
- 통합 사이트 검토용 Site Review Hub
- CRA 후속 조치 권고
- 강화된 모니터링 보고서 초안 생성
- 필수 문서 준비 추적
- 프로토콜 일탈 추적
- ICF 버전 관리 점검
- 트리거 기반 감사 유사 변경 로그

## 7. 위험 점수 산정 로직

다음 지표를 기반으로 사이트 위험을 계산합니다.

- Open query 수
- Query 경과 일수
- 프로토콜 일탈 건수
- SAE 보고 지연 건수
- 누락 필수 문서 수
- IP 관리(IP accountability) 이슈 건수
- ICF 이슈 건수

`targetEnrollment`·`currentEnrollment`는 대시보드에서 사이트 맥락 정보로 표시되지만, 위험 점수 계산에는 사용되지 않습니다.

**위험 수준**

| 점수     | 수준         |
| -------- | ------------ |
| 0~2점    | Low(낮음)    |
| 3~5점    | Medium(중간) |
| 6점 이상 | High(높음)   |

상세 로직: [docs/risk-scoring-logic.md](docs/risk-scoring-logic.md)

## 8. 기술 스택

**현재**

| 구분               | 기술                              |
| ------------------ | --------------------------------- |
| Frontend           | Next.js                           |
| Backend            | FastAPI                           |
| Database           | Supabase PostgreSQL               |
| Authentication     | Supabase Auth                     |
| External API       | ClinicalTrials.gov API            |
| Audit-like logging | PostgreSQL trigger 기반 변경 로그 |

**향후**

- 자동화: n8n
- 배포: Vercel, Render/Railway/Fly.io, AWS 등
- AI: LLM 기반 프로토콜 요약·체크리스트 생성

FastAPI는 API 개발 속도, 공개 등록부 연동, 위험 점수 로직, 향후 LLM 문서 처리에 적합합니다.

Supabase PostgreSQL은 연구·사이트·체크리스트·모니터링 지표를 관계형으로 관리하면서 MVP 개발·배포 속도를 높이기 위해 선택했습니다.

## 9. 인증(Auth)

### 인증 및 Import 보호

로그인 없이 연구 대시보드, 사이트 리뷰 페이지, 모니터링 보고서 초안, 감사 로그, CRA 검토 모듈을 조회할 수 있습니다.

ClinicalTrials.gov 연구 import는 Supabase PostgreSQL에 레코드(합성 데모 운영 데이터 포함)를 생성·수정하므로 Supabase Auth로 보호합니다.

포트폴리오 데모 접근성을 유지하면서, 배포 환경에서 무분별한 DB 쓰기를 방지하는 설계입니다.

**현재 인증 범위**

- 대시보드 검토: 공개 읽기
- 연구 import: 인증 필요
- 사용자별 row 소유권: MVP 미구현
- 다중 테넌트 RLS: 향후 프로덕션 버전 계획

## 10. 프로젝트 한계

본 프로젝트는 프로토타입이며 다음 한계가 있습니다.

- CRA의 전문적 판단을 대체하지 않습니다.
- 규제·의학적 조언을 제공하지 않습니다.
- 실제 임상시험 피험자 데이터를 사용하지 않습니다.
- 위험 점수 로직은 시연용으로 단순화되어 있습니다.
- 체크리스트는 MVP에서 사전 정의 규칙·템플릿 기반입니다.
- 감사 유사 로그는 검증된 audit trail이 아닙니다.
- 전자서명, 시스템 밸리데이션, 21 CFR Part 11 등 검증된 임상시스템 요건은 구현하지 않습니다.
- import 보호용 Auth만 있으며, 사용자별 row 소유권·RLS 다중 테넌트 격리는 MVP에 없습니다.
- import 연구·생성 데모 데이터는 현재 데모 DB에서 공유됩니다.

## 11. 향후 개선

계획 항목:

- n8n 기반 고위험 사이트 알림 워크플로
- 프로토콜 PDF 업로드·파싱
- 프로토콜 개정본 비교
- 위임·교육 로그 일치 점검
- 사이트 모니터링 지표 CSV 업로드
- 필수 문서 추적 CSV 업로드
- 일탈·문서·ICF 수동 편집 페이지
- 모니터링 보고서 초안 PDF/Markdown보내기
- LLM 보조 프로토콜 요약·CRA 체크리스트 생성
- import 공개 연구 기반 모니터링 포커스 영역 LLM 생성
- 사용자별 row 소유권·RLS 다중 테넌트 접근 제어
- 프로덕션 환경 배포

## 12. 현재 MVP 상태

구현 완료 항목:

- 연구 목록·연구 개요 페이지
- SIV·IMV 체크리스트 표시
- 사이트별 위험 점수 계산
- Site risk dashboard
- CRA 후속 조치 권고
- ClinicalTrials.gov 검색·상세 미리보기
- Supabase 연구 import (created/updated 상태)
- import 시 합성 데모 사이트·모니터링 지표 자동 생성
- 테이블 수준 변경 추적용 트리거 기반 감사 유사 로그
- FastAPI 백엔드 (`app/api/` 기능별 라우터)
- Next.js 프론트엔드 (`components/` 도메인별 컴포넌트)
- Supabase PostgreSQL
- JSON 시드·합성 모니터링 데이터
- Supabase Auth 로그인/회원가입
- 인증 기반 ClinicalTrials.gov import
- Site Review Hub
- Enhanced Monitoring Report Draft
- Essential Document Readiness Tracker
- Protocol Deviation Tracker
- ICF Version Control Check

## 13. API 엔드포인트

백엔드 라우터: `backend/app/api/` (studies, risk, site_monitoring, checklists, clinical_trials, audit_logs, alerts 등)

### Study APIs

| Method | Endpoint                               | 설명                           |
| ------ | -------------------------------------- | ------------------------------ |
| GET    | `/api/studies`                         | 전체 샘플 연구 목록            |
| GET    | `/api/studies/{study_id}`              | 연구 상세                      |
| GET    | `/api/studies/{study_id}/sites`        | 연구별 사이트 목록             |
| GET    | `/api/studies/{study_id}/risk-sites`   | 위험 점수가 계산된 사이트 목록 |
| GET    | `/api/studies/{study_id}/action-items` | CRA 후속 조치 항목             |

### Checklist APIs

| Method | Endpoint              | 설명                   |
| ------ | --------------------- | ---------------------- |
| GET    | `/api/checklists`     | 전체 체크리스트 템플릿 |
| GET    | `/api/checklists/siv` | SIV 체크리스트         |
| GET    | `/api/checklists/imv` | IMV 체크리스트         |

### Risk APIs

| Method | Endpoint          | 설명                  |
| ------ | ----------------- | --------------------- |
| GET    | `/api/risk/sites` | 전체 사이트 위험 점수 |

### External Clinical Trial APIs

| Method | Endpoint                                        | 설명                                                     |
| ------ | ----------------------------------------------- | -------------------------------------------------------- |
| GET    | `/api/external/clinical-trials/search`          | ClinicalTrials.gov 공개 연구 검색                        |
| GET    | `/api/external/clinical-trials/{nct_id}`        | NCT ID로 공개 연구 상세                                  |
| POST   | `/api/external/clinical-trials/{nct_id}/import` | Supabase import 및 합성 데모 데이터 생성 (**인증 필요**) |

### Audit Log APIs

| Method | Endpoint          | 설명                            |
| ------ | ----------------- | ------------------------------- |
| GET    | `/api/audit-logs` | 트리거 기반 감사 유사 변경 로그 |

### Alert APIs

| Method | Endpoint                      | 설명                    |
| ------ | ----------------------------- | ----------------------- |
| GET    | `/api/alerts/high-risk-sites` | 고위험 사이트 알림 목록 |

### Site Monitoring APIs

| Method | Endpoint                                                          | 설명                        |
| ------ | ----------------------------------------------------------------- | --------------------------- |
| GET    | `/api/studies/{study_id}/sites/{site_id}/review-summary`          | 통합 사이트 검토 요약       |
| GET    | `/api/studies/{study_id}/sites/{site_id}/monitoring-report-draft` | 강화된 모니터링 보고서 초안 |
| GET    | `/api/studies/{study_id}/sites/{site_id}/essential-documents`     | 필수 문서 준비 요약         |
| GET    | `/api/studies/{study_id}/sites/{site_id}/protocol-deviations`     | 프로토콜 일탈 요약          |
| GET    | `/api/studies/{study_id}/sites/{site_id}/icf-version-check`       | ICF 버전 일치 점검          |

## 14. 로컬 실행 방법

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**API 문서:** http://localhost:8000/docs

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### 환경 변수

**Backend** — `backend/.env` 생성:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
DATA_SOURCE=supabase
```

**Frontend** — `frontend/.env.local` 생성:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_SUPABASE_URL=your_supabase_project_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

예시 파일: `frontend/.env.example`

## 15. 스크린샷

### Study List (연구 목록)

![Study List](docs/images/study-list.png)

### ClinicalTrials.gov Study Import

![Study Import](docs/images/study-import.png)

### Login and Auth-gated Import

![Login](docs/images/login.png)

### Study Overview

![Study Overview](docs/images/study-overview.png)

### Site Risk Dashboard

![Site Risk Dashboard](docs/images/risk-dashboard.png)

### Site Review Hub

![Site Review Hub](docs/images/site-review-hub.png)

### Enhanced Monitoring Report Draft

![Enhanced Monitoring Report Draft](docs/images/enhanced-monitoring-report.png)

### Essential Document Readiness Tracker

![Essential Document Readiness](docs/images/essential-documents.png)

### Protocol Deviation Tracker

![Protocol Deviation Tracker](docs/images/protocol-deviations.png)

### ICF Version Control Check

![ICF Version Control Check](docs/images/icf-version-check.png)

### Trigger-based Audit-like Logs

![Audit Logs](docs/images/audit-logs.png)

## 16. Supabase 설정

연구, 사이트, 모니터링 지표, 체크리스트, 감사 유사 로그 등에 Supabase PostgreSQL을 사용합니다.

**주요 테이블**

- studies
- sites
- monitoring_metrics
- checklist_templates
- essential_documents
- protocol_deviations
- icf_versions
- subject_consents
- audit_logs

초기 시드 데이터는 백엔드 시드 스크립트로 삽입합니다. 선택된 운영 테이블에는 insert·update·delete 시 oldData·newData JSONB 스냅샷을 기록하는 트리거 기반 감사 유사 로그가 적용됩니다.

```bash
cd backend
python scripts/seed_supabase.py
```

## 17. 라이선스

MIT License

본 프로젝트는 포트폴리오 프로토타입이며, 실제 임상시험 운영, 규제 제출, 검증된 임상시스템 용도가 아닙니다.

---

> **참고:** 영문 원본은 [README.md](README.md)를 참고하세요.
