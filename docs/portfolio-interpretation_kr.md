# 포트폴리오 해석 (Portfolio Interpretation)

## 1. 프로젝트 맥락

CRA-RBM Assistant는 데이터 엔지니어링, 백엔드 개발, 데이터 품질 경험이 임상시험 모니터링 워크플로에 어떻게 적용될 수 있는지 보여 주는 포트폴리오 프로젝트입니다.

처음에는 CRA 모니터링 활동을 구조화된 소프트웨어 워크플로로 옮기는 데 초점을 두었고, 이후 ClinicalTrials.gov 공개 등록부 데이터를 기반으로 한 별도의 클라우드 데이터 엔지니어링 파이프라인을 소비하도록 확장되었습니다.

현재 프로젝트는 다음 두 가지 연결 역량을 시연합니다.

1. **임상 도메인 워크플로 설계**
   - 위험 기반 모니터링 지원
   - 필수 문서 준비 상태
   - 프로토콜 일탈 추적
   - ICF 버전 일치성 점검
   - 위임 / 교육 일치성 점검
   - 모니터링 보고서 초안 생성

2. **데이터 → 애플리케이션 통합**
   - Databricks Serving Layer 통합
   - FastAPI 등록부 API
   - BigQuery / dbt 분석 통합
   - Supabase로의 연구 import
   - 안정적인 API를 통한 AI Agent tool 통합

---

## 2. 핵심 포트폴리오 메시지

이 프로젝트의 핵심 메시지는 다음과 같습니다.

> **구조화된 데이터는 실제 애플리케이션 워크플로와 연결될 때 가치가 생긴다.**

CRA-RBM Assistant는 데이터를 저장하거나 시각화하는 데서 멈추지 않습니다.

다음을 연결합니다.

```text
ClinicalTrials.gov Public Registry
        ↓
Cloud Data Engineering Pipeline
        ↓
Databricks Serving / BigQuery Analytics
        ↓
FastAPI
        ↓
CRA-RBM Application
        ↓
CRA Assistant Agent
```

이를 통해 원천 공개 데이터가 다음으로 이어지는 흐름을 보여 줍니다.

- 분석용 데이터셋
- 애플리케이션용 serving 모델
- 최종 사용자 워크플로
- AI tool 인터페이스

---

## 3. 보여 주는 강점

### 데이터 모델링과 데이터 품질

- 등록부 데이터와 합성 운영 데이터의 분리
- 명시적인 애플리케이션 지향 데이터 계약
- 날짜 / 버전 일치성 검증
- 상태(status) 기반 추적
- 이슈 분류
- 감사(audit) 유사 변경 추적성

### 데이터 엔지니어링 통합

- Databricks Serving Layer 소비
- BigQuery 분석 데이터 소비
- dbt analytics mart 통합
- 데이터 플랫폼과 애플리케이션 사이의 서비스 경계로서 FastAPI
- 하위 데이터 소스를 바꾸면서도 안정적인 프론트엔드 계약 유지

### 백엔드 및 API 설계

- 등록부 검색 / 상세 API
- 기존 import 워크플로용 호환 API
- 분석 API
- study / site / monitoring API
- 인증된 쓰기 작업
- 애플리케이션 DB 책임과 외부 등록부 데이터의 분리

### 워크플로 설계

- study import
- 사이트 위험 검토
- 필수 문서 준비 상태
- 프로토콜 일탈 검토
- ICF 일치성 점검
- 위임 / 교육 점검
- 모니터링 보고서 초안 생성
- CRA 후속 조치 생성

### AI 통합

- 등록부 검색 tool
- 등록부 상세 tool
- Databricks 직접 접근 대신 FastAPI 재사용
- 등록부 사실 데이터와 합성 CRA 운영 데이터의 명확한 분리

---

## 4. 기능 ↔ 엔지니어링 매핑

| Feature                     | Domain / Workflow               | Engineering Strength Demonstrated              |
| --------------------------- | ------------------------------- | ---------------------------------------------- |
| Registry Search             | 공개 임상시험 탐색              | 애플리케이션 지향 Serving 모델 소비            |
| Registry Study Detail       | 구조화된 연구 조회              | API 계약을 통한 nested 데이터 전달             |
| Study Import                | 등록부 → 내부 워크스페이스      | 데이터 매핑 및 호환 레이어 설계                |
| Clinical Trial Analytics    | trial 추세 / 분포               | BigQuery + dbt analytics mart 소비             |
| Risk Dashboard              | 사이트 위험 우선순위화          | 지표 모델링 및 대시보드 통합                   |
| Essential Document Tracker  | 사이트 파일 준비 상태           | 상태 기반 데이터 관리                          |
| Protocol Deviation Tracker  | 일탈 후속 조치                  | 이슈 분류 및 구조화된 후속 추적                |
| ICF Version Check           | 동의서 버전 검토                | 날짜 / 버전 일치성 검증                        |
| Delegation & Training Check | 스태프 준비 상태 검토           | 레코드 간 일치성 검증                          |
| Monitoring Report Draft     | 모니터링 문서화                 | 구조화된 데이터→문서 워크플로                  |
| Audit-like Logs             | 변경 추적성                     | 트리거 기반 이력 추적                          |
| Auth-gated Import           | 통제된 쓰기 작업                | 인증을 고려한 서비스 설계                      |
| Agent Registry Tools        | AI 보조 등록부 조회             | API 재사용 및 tool 기반 AI 통합                |

---

## 5. 데이터 플랫폼 통합

애플리케이션은 별도의 `clinical-trials-data-platform` 프로젝트와 연결됩니다.

데이터 플랫폼이 제공하는 흐름:

```text
ClinicalTrials.gov
        ↓
Bronze
        ↓
Silver
        ↓
Quality
        ↓
Gold / Serving
```

CRA-RBM Assistant는 두 가지 하위 경로를 소비합니다.

### Application Serving Path

```text
Databricks Serving
        ↓
FastAPI Registry API
        ↓
Study Search / Detail / Import
```

### Analytics Path

```text
Databricks Gold
        ↓
BigQuery
        ↓
dbt Analytics Mart
        ↓
FastAPI
        ↓
Clinical Trial Analytics Dashboard
```

이 분리는 다음의 차이를 보여 줍니다.

- **분석용 데이터셋**
- **애플리케이션 serving 데이터셋**

하나의 데이터 모델이 두 목적을 모두 억지로 담당하지 않도록 했습니다.

---

## 6. 애플리케이션 통합 전략

중요한 엔지니어링 결정 중 하나는, 하위 데이터 소스를 바꾸면서도 기존 프론트엔드 워크플로를 유지한 것입니다.

이전:

```text
Frontend
    ↓
FastAPI
    ↓
ClinicalTrials.gov API
```

현재:

```text
Frontend
    ↓
FastAPI
    ↓
Databricks Serving Layer
```

기존 study import UI와 프론트엔드 계약은 대체로 그대로 유지했습니다.

이를 통해 다음을 시연합니다.

- 하위 호환 API 설계
- 프론트엔드 결합도 감소
- 서비스 레이어 추상화
- 애플리케이션 전체를 재설계하지 않고 데이터 소스 전환

---

## 7. 데이터 경계 설계

이 프로젝트는 다음을 의도적으로 구분합니다.

### Public Registry Facts

예시:

- NCT ID
- title
- phase
- status
- conditions
- interventions
- outcomes
- eligibility criteria

### Synthetic CRA Operational Data

예시:

- site risk
- query aging
- protocol deviations
- essential document issues
- ICF inconsistencies
- follow-up actions

이 두 데이터 범주는 동등한 성격으로 제시되지 않습니다.

공개 등록부 데이터에는 모든 프로토콜 수준·운영 모니터링 정보가 들어 있지 않기 때문에, 이 경계는 중요합니다.

알 수 없는 운영 정보를 등록부 데이터로부터 만들어내지 않습니다.

---

## 8. AI Agent 통합

CRA Assistant Agent는 CRA-RBM FastAPI를 통해 등록부 데이터에 접근합니다.

```text
CRA Assistant Agent
        ↓
searchRegistryStudies
getRegistryStudyDetail
        ↓
FastAPI
        ↓
Databricks Serving
```

Agent는 Databricks를 직접 조회하지 않습니다.

이 설계가 보여 주는 점:

- tool 기반 AI 통합
- 애플리케이션 API 재사용
- AI 로직과 물리 데이터 테이블 간 결합도 감소
- 등록부 사실 데이터와 합성 데모 데이터의 명확한 분리

---

## 9. 포트폴리오 포지셔닝

이 프로젝트는 목표 역할에 따라 다르게 제시할 수 있습니다.

### 데이터 엔지니어 역할

강조할 점:

- 데이터 플랫폼 → 애플리케이션 통합
- Serving Layer 설계
- 분석용 vs 애플리케이션용 데이터 모델 분리
- BigQuery / dbt 소비
- API 기반 데이터 전달
- 안정적인 애플리케이션 계약
- 데이터 품질 및 일치성 검증
- end-to-end 데이터 라이프사이클

추천 프레이밍:

> 기존 임상시험 워크플로 애플리케이션을 확장해, 공개 등록부 데이터를 외부 API에서 직접 소비하지 않도록 바꿨습니다. 대신 FastAPI를 통해 Databricks 기반 Serving Layer를 사용하고, 분석 데이터는 BigQuery와 dbt로 전달합니다. 덕분에 동일한 원천 데이터가 애플리케이션 검색/상세 워크플로와 분석 대시보드를 서로 다른 데이터 모델로 지원할 수 있게 되었습니다.

### CRA / 임상 운영 역할

강조할 점:

- CRA 모니터링 워크플로 이해
- 위험 기반 검토
- 필수 문서 준비 상태
- 프로토콜 일탈 후속
- ICF 일치성 점검
- 합성 모니터링 시나리오
- 모니터링 문서화 지원

---

## 10. 이 프로젝트가 주장하지 않는 것

이 프로젝트는 다음을 주장하지 않습니다.

- 검증된 임상시험 시스템
- 프로덕션 CTMS
- 프로덕션 EDC
- 검증된 audit trail
- 21 CFR Part 11 준수 시스템
- 실제 환자 또는 사이트 성과 데이터의 원천
- CRA 판단의 대체물
- 프로덕션 규모 임상 데이터 플랫폼

대신 다음을 시연하기 위한 포트폴리오 프로토타입입니다.

- 데이터 워크플로 설계
- 애플리케이션 통합
- CRA 지향 도메인 모델링
- 데이터 품질 로직
- 클라우드 데이터 엔지니어링 개념
- AI tool 통합

---

## 11. 전체 포트폴리오 서사

관련 프로젝트 세 개는 하나의 연결된 포트폴리오 스토리를 이룹니다.

```text
Clinical Trials Data Platform
        ↓
CRA-RBM Assistant
        ↓
CRA Assistant Agent
```

### Clinical Trials Data Platform

시연하는 내용:

- ingestion
- transformation
- data quality
- incremental processing
- analytics modeling
- application serving

### CRA-RBM Assistant

시연하는 내용:

- API 통합
- 애플리케이션 데이터 소비
- CRA 워크플로 모델링
- 대시보드 / 검토 워크플로
- 인증된 study import

### CRA Assistant Agent

시연하는 내용:

- tool 기반 AI 통합
- 애플리케이션 API 재사용
- 원천을 인지한(source-aware) 조회
- 등록부 검색 / 상세 지원

세 프로젝트를 합치면 다음을 보여 줍니다.

> **Public data → Data Engineering → Application Serving → Domain Workflow → AI Tool Integration**

---

> **영문 원본:** [portfolio-interpretation.md](portfolio-interpretation.md)
