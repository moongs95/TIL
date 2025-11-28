# BERT 이후의 모델 이해하기  
(BERT 파생 모델 요약 정리)

---

## 📌 개요
BERT를 기반으로 다양한 개선 모델이 등장했으며, 각 모델은  
**학습 효율성 / 파라미터 최적화 / 성능 개선 / 속도 개선**에 초점을 두고 발전함.

대표 파생 모델:
- **RoBERTa**
- **SpanBERT**
- **ELECTRA**
- **ALBERT**
- **DistilBERT**

---

## 1️⃣ RoBERTa — Dynamic Masking + NSP 제거

**논문: A Robustly Optimized BERT Pretraining Approach**

### 주요 개선점
| 항목 | 기존 BERT | RoBERTa |
|------|-----------|---------|
| Masking 방식 | Static Masking | **Dynamic Masking** |
| 사전학습 Task | MLM + NSP | **MLM only** |
| 학습 데이터 | 16GB | **160GB 이상** |
| Batch size | 256 | **8K** |

### Static Masking (BERT 문제점)
- 마스킹이 전처리 시 **한 번만 적용**
- 항상 같은 단어만 마스킹 → **과적합(Overfitting) 위험**

### Dynamic Masking (RoBERTa 장점)
- 학습 중 **매 스텝마다 마스킹 새로 적용**
- 더 다양한 token 예측 → **일반화 성능 향상**

### NSP 제거
- NSP가 실제 문장 관계 학습에 **도움이 적음**
- **단일 문서 기반 입력이 가장 좋은 성능**

---

## 2️⃣ SpanBERT — Span 마스킹 + Span Boundary Objective

**논문: Improving Pre-training by Representing and Predicting Spans**

### 핵심 아이디어
- Mask를 **연속된 token span** 단위로 적용
- Span 전체 정보를 예측하도록 학습

### 추가 Loss: **SBO (Span Boundary Objective)**
- Span 양 끝 토큰 임베딩을 활용해 전체 span 복원

| 항목 | BERT | SpanBERT |
|------|------|----------|
| 마스킹 | Token Masking | **Span Masking** |
| 학습 목적 | MLM + NSP | **MLM + SBO** |
| 입력 | 문장쌍 | **단일 문장** |

📌 질문답변(QA), 구조적 정보가 중요한 Task에서 성능 ↑

---

## 3️⃣ ELECTRA — 학습 효율 극대화 (RTD 방식)

**논문: Efficiently Learning an Encoder that Classifies Token Replacements Accurately**

### 문제: BERT의 비효율성
- **오직 15% 마스크된 Token만** loss 계산

### ELECTRA 학습 구조
| 구성 | 역할 |
|------|------|
| **Generator (작은 MLM)** | 가짜 토큰 생성 |
| **Discriminator (ELECTRA)** | 가짜 토큰 판별 |

### 학습 목표: **RTD (Replaced Token Detection)**
- 입력 **모든 토큰**에 대해 학습 → **100% Token 활용**
- 효율성 극대화 → 더 작은 모델에서도 성능 우수

| 항목 | BERT | ELECTRA |
|------|------|--------|
| 학습 방식 | MLM & NSP | **RTD** |
| Efficiency | 낮음 | **매우 높음** |

📌 Small-size 모델에서 특히 강력한 성능 발휘!

---

## 4️⃣ ALBERT — 파라미터 공유 + 임베딩 분리 (경량화)

**논문: A Lite BERT for Self-Supervised Learning of Language Representations**

### 목적
- 성능 유지하면서 **파라미터 극적 감소**
- GPU 메모리 부담 감소 + 속도 증가

### 핵심 기술
1) **Factorized Embedding Parameterization**  
- Embedding 크기(E)와 Hidden size(H)를 분리하여  
  **임베딩 파라미터 크게 감소**

2) **Cross-layer Parameter Sharing**  
- 모든 Transformer Layer 파라미터 공유  
  → 모델 크기 획기적으로 축소

3) **SOP (Sentence Order Prediction)**  
- NSP 대신 **문장 순서를 맞추는 Task**
- 실제 문장 관계 학습에 더 효과적

### 비교 요약
| 항목 | BERT | ALBERT |
|------|------|--------|
| 파라미터 수 | Base: 110M / Large: 340M | **Base: 12M / Large: 18M** |
| 사전학습 Task | MLM + NSP | **MLM + SOP** |
| 효율성 | 낮음 | **매우 높음** |

📌 대형 모델일수록 이점이 매우 큼

---

## 5️⃣ DistilBERT — Knowledge Distillation 기반 경량화

**논문: A Distilled version of BERT**

### 핵심 개념: Knowledge Distillation
- Teacher: BERT
- Student: 작은 BERT 모델이 **Teacher의 soft label을 학습**

### 성능 & 효율 비교
| 항목 | BERT | DistilBERT |
|------|------|------------|
| 파라미터 | 110M | **66M (-40%)** |
| 정확도 | 100% | **97% 유지** |
| 학습 속도 | 기준 | **+60% 빠름** |

📌 모바일 환경, 실시간 시스템에 적합

---

## 📌 모델별 특징 요약 표

| 모델 | 주요 특징 | 장점 |
|------|---------|-----|
| **RoBERTa** | Dynamic Masking / NSP 제거 | 성능 전반적 향상 |
| **SpanBERT** | Span Masking + SBO | QA/문서 구조 Task에 강함 |
| **ELECTRA** | RTD (모든 Token 학습) | 작은 모델에서도 높은 효율 |
| **ALBERT** | 파라미터 공유 + SOP | 메모리/속도 최적화 |
| **DistilBERT** | Knowledge Distillation | 97% 성능 유지하며 경량화 |

---

## 🧠 핵심 한 줄 정리
> BERT 이후의 모델들은 **성능(A→S), 효율(E), 경량화(L), 속도(F)** 중 하나를 목표로 발전했다.

( A=Accuracy / E=Efficiency / L=Lightweight / F=Fast )
