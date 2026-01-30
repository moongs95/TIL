# 📌 TIL: Data-Centric AI의 미래

## 01. Data-Centric AI의 미래

### 1.1 개요

#### Foundation Model의 시대

2022년 11월 30일 **ChatGPT** 공개 이후,  
Data-Centric AI에서도 **LLM을 중심으로 큰 변화**가 시작되었다.

- 대규모 **비라벨(unlabeled) 데이터**를 기반으로 사전학습
- 다양한 **다운스트림 태스크**에 적응 가능
- 데이터 자체보다 **데이터를 어떻게 구성·확장·활용하는가**가 중요해짐

👉 이제 Data-Centric AI는  
**“개별 태스크용 데이터 관리” → “Foundation Model에 필요한 데이터 전략”**으로 확장됨

#### Data-Centric AI의 핵심 키워드 (미래)

- **Multilingual**
- **Multimodal**
- **Synthetic Data**

---

### 1.2 Multilingual

#### 과거: Unilingual Language Model

트랜스포머 이전에는 대부분 **단일 언어(Unilingual)** 모델이 주류였다.

**이유**
1. LSTM 기반 seq2seq 모델의 한계
   - 여러 언어를 하나로 인코딩하기에 학습 시간이 매우 오래 걸림
   - 모델 사이즈 확장에 제약 존재
2. 다중 언어에 대한 수요 자체가 적었음
   - 기계 번역 외에는 활용도가 낮았음
   - 두 언어만 포함되어도 “다중언어 데이터”로 간주

**예시**
- Multi30K: 영어–독일어 이미지 설명 데이터셋

#### 현재: Multilingual LLM

- 트랜스포머 이후 다중 언어 연구는 지속되었으나, 여전히 Unilingual이 주류
- **LLM 등장 이후**
  - Multilingual 성능이 Unilingual을 뛰어넘기 시작
  - Multilingual이 **기본(default)** 이 되어가는 추세

👉 Data-Centric 관점의 변화  
- 특정 언어 데이터만 정제 → ❌  
- **다국어 데이터의 균형, 커버리지, 품질 관리** → ⭕

---

### 1.3 Multimodal

#### Unimodal → Multimodal

과거의 데이터/모델 특징:
- 하나의 태스크, 하나의 도메인, 하나의 모달리티에 집중
- 높은 성능을 위해 **단일 모달(Unimodal)** 중심 설계

Multimodal 연구는 존재했으나:
- 성능이 낮아 실사용에 한계
- 특정 태스크용 데이터셋에 국한

**예시**
- TextVQA: 이미지 속 텍스트에 대한 질의응답

#### Foundation Model 이후의 변화

- LLM을 중심으로 **Multimodal Foundation Model** 등장
- 텍스트 + 이미지 + 음성 + 비디오를 통합적으로 처리
- Data-Centric 관점에서:
  - 서로 다른 모달리티 간 **정합성(alignment)** 이 중요
  - 모달 간 노이즈, 누락, 불균형 관리가 핵심 이슈

---

### 1.4 Synthetic Data

#### Synthetic Data란?

- 실제 세계에서 수집한 데이터가 아닌
- **알고리즘, 시뮬레이션, 생성 모델**을 통해 만들어진 인위적 데이터

#### Synthetic Data의 등장 배경

- GPT-4 등 LLM이 인간 수준 이상의 결과를 생성
- 모델이 생성한 데이터를 다시 학습에 활용 가능
- **“모델 → 데이터 생성 → 새로운 모델 학습”** 구조 가능

#### Synthetic Data의 현재

- ChatGPT로 생성한 데이터가
  - 일부 태스크에서 **인간 생성 데이터보다 우수**하다는 연구 결과 등장

#### Synthetic Data의 장점

- **비용 및 시간 절감**
  - 이미지 라벨링 비용: 약 6달러
  - 이미지 합성 비용: 약 6센트
- **희귀 조건 대응 가능**
  - 현실에서 발생하기 어려운 상황 시뮬레이션 가능
- **프라이버시 문제 없음**
  - 개인정보 침해 위험 낮음
- **데이터 편향 완화**
  - 의도적으로 분포 제어 가능

#### Synthetic Data의 미래

- 생성 모델의 성능 향상과 함께 사용 빈도 지속 증가 예상
- Data-Centric AI의 핵심 전략 중 하나로 자리 잡을 가능성 높음

👉 미래의 Data-Centric AI  
- “데이터를 수집한다” → ❌  
- **“데이터를 설계한다”** → ⭕

---

## ✍️ TIL 정리 한 줄 요약

> Data-Centric AI의 미래는  
> **Foundation Model을 중심으로, Multilingual·Multimodal·Synthetic Data를 어떻게 설계하고 관리하느냐에 달려 있다.**
