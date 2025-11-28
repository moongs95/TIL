# Encoder-Decoder Model (BART) 이해하기

---

## 01. Encoder-Decoder 기본 구조

### 1.1 Encoder 구조
- **역할**: Source 문장의 정보를 **압축**
- **특징**
  - 문장 이해 / 분류 Task에 강함 (예: 감정 분석)
  - **Masked Language Modeling (MLM)** 방식으로 학습
    - 문장 중 임의 Token을 [MASK]로 대체하고 해당 Token 예측
    - **양방향(Bidirectional)** 문맥 활용 → BERT 구조 기반

---

### 1.2 Decoder 구조
- **역할**: Encoder 정보를 활용해 **다음 단어 생성**
- **특징**
  - 요약, 번역 등 **Text Generation**에 강함
  - **Causal Language Modeling (CLM)** 기반
    - 이전 토큰만 보고 다음 토큰 예측
    - **단방향(Unidirectional)** 성격 → GPT 구조 기반

---

### 1.3 Encoder-Decoder 구조 (Seq2Seq)
- Encoder + Decoder 함께 사용
- **Sequence-To-Sequence(Task 전환)**에 최적화
  - 입력 Sequence → 목적 Sequence로 변환
  - 입력/출력 길이가 다르더라도 처리 가능
- 대표 Task:
  - **요약(Summarization)**
  - **번역(Machine Translation)**

---

## 02. BART (Bidirectional and Auto-Regressive Transformers)

### 2.1 BART 개요
- **Transformer 기반 Encoder-Decoder 구조**
- 입력 문장에 **Noise를 추가** → 이를 **복원**하도록 Pre-training
- 다양한 Noise 추가 방식 → **범용성 매우 높음**
- Fine-tuning 시 **Sequence Generation Task에서 매우 뛰어남**

---

### 2.2 BART Pre-training — 5가지 Noise 방식

| Noise 방식 | 설명 | Decoder 목표 |
|-----------|------|--------------|
| Token Masking | 일부 토큰을 [MASK]로 대체 | 원래 문장 복원 |
| Token Deletion | 일부 토큰을 제거 | 원래 문장 복원 |
| Text Infilling | 연속된 Span 단위 마스킹 | 원래 문장 복원 |
| Sentence Permutation | 문장 단위를 섞어서 입력 | 올바른 순서 문장 생성 |
| Document Rotation | 임의 토큰을 문장 시작으로 회전 | 올바른 원문 복원 |

📌 **Text Infilling + Sentence Permutation 조합이 가장 성능 우수**

---

### 2.3 Fine-tuning
- Encoder에 **Source 문장**, Decoder에서 **Target 문장 생성**
- **Autoregressive 생성 방식**
- 번역 Task에서:
  - 새로운 언어 처리 위해 **Randomly Initialized Encoder 추가**
  - **다른 Vocabulary 사용 가능**

---

### 2.4 BART로 수행 가능한 Downstream Tasks

| Task 유형 | Task 예시 | 설명 |
|----------|-----------|-----|
| Sequence Classification | 감정 분석(NSMC) | Encoder와 Decoder 입력 동일 → Decoder 마지막 토큰 기반 분류 |
| Token Classification | NER, POS Tagging | Decoder 마지막 레이어의 Token Representation 활용 |
| Sequence Generation | 요약, 질의응답 | Decoder가 Autoregressive하게 생성 |
| Machine Translation | 다국어 번역 | 새로운 언어에 대해 추가 Encoder 학습 가능 |

---

### 2.5 실험 결과 정리
- Encoder-Decoder 구조 기반으로 **요약, 번역에서 매우 높은 성능**
- Noise 방식 성능 비교:
  - **Text-Infilling > Sentence Permutation 조합 > Masking / Deletion**
  - Document Rotation 단독 사용 효과는 낮은 편
- **다중 문장 Task**에서 더욱 강점 발휘

---

## 핵심 정리

| 요소 | 설명 |
|------|------|
| 모델 구조 | Transformer Encoder-Decoder |
| 학습 방식 | Noise 추가 → 원문 복원 |
| 주요 장점 | 다양한 Generation Task에서 강력한 성능 |
| 중요한 Noise 방식 | **Text Infilling** |

📌 **BART = BERT(이해) + GPT(생성) 강점 결합한 Seq2Seq 모델**

---

## 기억해야 할 한 줄 요약
> “BART는 노이즈가 추가된 문장을 복원하는 Pre-training을 통해 **이해와 생성 모두 강력한** 범용 Encoder-Decoder 모델이다.”
