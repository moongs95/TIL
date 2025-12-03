# 🏆 자연어처리 경진대회 전략 정리

## 01. 대회 전략 이해하기

- 강의 내용이 100% 성능 향상으로 이어지지는 않음
- **데이터 분석 → 대회 특성 파악 → 상황 맞는 기법 적용**이 핵심

---

## 1.1 데이터 증강 기법 (Data Augmentation for NLP)

> 데이터 다양성을 늘려 **일반화 성능 향상**

### 🔹 주요 기법
| 기법 | 개념 | 특징 |
|---|---|---|
| EDA | 유의어 치환/삽입/삭제/스왑 | 단어 수준 증강 |
| AEDA | 문장부호 추가 | 가장 간단 + 성능 효과 검증됨 |
| Back Translation | 번역 후 원 언어로 역번역 | 문장 품질 좋음 + 비용 높음 |

---

### EDA (Easy Data Augmentation)
- 단어 단위 변경을 통한 증강 방법
- 4가지 규칙
  - **SR**: Synonym Replacement (유의어 교체)
  - **RI**: Random Insertion (임의 단어 삽입)
  - **RS**: Random Swap (두 단어 위치 변경)
  - **RD**: Random Deletion (임의 단어 삭제)

→ *텍스트 노이즈로 모델을 더 강하게 만듦*

---

### AEDA (An Easier Data Augmentation)
- **문장부호 삽입만으로 데이터 다양화**
- 사용 예: `. , : ; ! ?`
- **EDA보다 구현 간단 + 성능 좋음**

---

### Back Translation
- 한국어 → 영어 → 한국어 (또는 일본어 → 한국어)
- 구조 변경 + 의미 유지 효과 🡅
- 품질 좋지만 번역 비용이 발생

---

## 1.2 Ensemble & K-fold

> 여러 모델의 장점을 합쳐 **성능 최대로 끌어올리기**

### 🔥 Ensemble

| 방식 | 개념 | 적용 예 |
|---|---|---|
| Hard Voting | 다수결 | 분류(Classification) |
| Soft Voting | 확률 평균 → 최상 확률 선택 | NLP 대부분 Task |

- NLP에서 **Soft Voting**이 더 많이 활용됨  
→ logit 혹은 prob 평균

---

### 🔁 K-fold Cross Validation

- 데이터를 k개로 나누고 **모든 데이터가 평가에 한 번씩 사용**
- 작은 데이터셋일수록 효과적
- K개의 모델 → **Ensemble과 자연스럽게 연결**

---

## 1.3 추가적인 학습 전략

### TAPT & DAPT

| 전략 | 데이터 타입 | 적용 목적 | 예시 |
|---|---|---|---|
| TAPT | 같은 Task 데이터 | Task 적응 | 문서 요약 Task → 요약 corpus 활용 |
| DAPT | 같은 Domain 데이터 | Domain 적응 | 의료 Task ↔ 의료 문서 사전학습 |

> 성능 향상 폭: **Pretraining > DAPT > TAPT**  
> 데이터가 제한적이면 **TAPT가 가성비 최고**

---

---

# ✨ 최신 대회 전략 (필수)

## 2.1 Test-Time 전략
| 기법 | 설명 |
|---|---|
| TTA (Test-Time Augmentation) | 입력을 변형 → 예측 여러 번 → 평균 |
| Multi-Checkpoint Ensemble | epoch 별 best checkpoint 앙상블 |

---

## 2.2 Prompt 기반 방법 (LLM 활용 가능 시)
- Instruction 기반 라벨 생성 → **Pseudo Labeling**
- Zero-shot / Few-shot 활용

---

## 2.3 데이터 품질 개선이 가장 중요
- 중복, 오탈자, HTML, 노이즈 제거
- Label leakage 여부 확인
- 텍스트 Normalization 전략 필수

---

## 2.4 모델 관련
- Transformer 계열 활용 (RoBERTa/KorBERT/KLUE 등)
- Parameter Efficient Tuning (LoRA/Prefix Tuning)

---

# 📌 요약

| 전략 | 목적 | 장점 |
|---|---|---|
| 데이터 증강 | 데이터 다양성 증가 | 일반화 성능↑ |
| 앙상블 & K-fold | 안정적이고 높은 성능 | 과적합 방지 |
| TAPT / DAPT | Task/Domain 적응 | 추가 성능 향상 |
| Test-Time / Prompt 전략 | 실제 성능 최적화 | 마지막 한 끗 개선 |

> **핵심: 데이터 분석 + 상황별 전략 선택이 진짜 실력!** 🚀
