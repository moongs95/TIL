# 🚀 Decoder Model: GPT-1 / GPT-2 / GPT-3 완전 정리

---

# 1. GPT-1 이해하기

## 📌 Decoder 기반 모델
- Transformer **Decoder 구조만 활용**
- 생성에 특화된 **Causal Language Modeling**
- 입력 문맥(이전 단어들)을 기반으로 다음 단어 예측
- **단방향(Unidirectional) self-attention**

---

## 1.1 GPT-1 모델 구조

- Multi-layer Transformer Decoder
- Vocab: BPE(Byte Pair Encoding) 40K
- Positional Embedding 사용
- **Masked Multi-Headed Self-Attention** 적용

### Self-Attention vs Masked Self-Attention
| 방식 | 참조 범위 | 예시 |
|------|---------|-----|
| Self-Attention | 앞 + 뒤 단어 | 우리는 어렵지만 **[MASK]** 한다 → ‘한다’ 활용 |
| Masked Self-Attention | 앞 단어만 | 우리는 어렵지만 **[MASK]** … |

→ 미래 정보(뒤 단어)를 보지 않도록 **Causal Masking**

---

## 1.2 GPT-1 학습 방법

### 🔹 Pre-training
- 언어 모델링(CLM)
- 왼→오 방향으로 다음 단어 예측
- 문장 → N+1개의 학습 샘플 생성

예시  
<start> ___ → This  
<start> This ___ → is  
<start> This is ___ → a  
<start> This is a ___ → sentence  
<start> This is a sentence ___ → <end>

### 🔹 Fine-tuning
- task 입력을 **하나의 문장으로 병합**
- **시작/종료 token(⟨s⟩, ⟨e⟩)** 명시적으로 추가해 생성 안정화

---

## 1.3 GPT-1 Downstream Task 활용

| Task | 구성 방식 | 예시 입력 |
|------|----------|----------|
| Single Sentence Classification | `<s>문장<e>` | 감성 분석 |
| Textual Entailment | `premise $ hypothesis` | 두 문장 관계(참/거짓/중립) |
| Sentence Similarity | 양방향 순서 모두 입력 | STS, MRPC |
| QA / Reasoning | 문서 + 질문 $ 답 후보  | 정답 후보별 softmax |

→ 모든 Task를 **문장 생성 문제로 통일**하여 해결

---

## 1.4 GPT-1 성능 요약
- 기존 task에서 **큰 성능 향상**
- 생성 능력 강력

---

# 2. GPT-2 / GPT-3 발전 과정

## 2.1 공통 개념

| 모델 | Layers | Params | Pretrain Data | Max Length |
|------|--------|--------|---------------|------------|
| GPT-1 | 12 | 117M | 4.8GB | 512 |
| GPT-2 | 48 | 1.5B | 40GB | 1024 |
| GPT-3 | 96 | 175B | 570GB | 2048 |

➡️ **모델 규모 증가 = 성능 증가 (Scaling Laws)**  
➡️ Fine-tuning 없이도 다중 Task 수행 가능(ZSL/OSL/FSL) 강조

---

## 2.2 기존 모델의 한계 및 해결 방향

### 기존 문제
1️⃣ 학습 task에서는 강력하지만,  새로운 task 일반화 어려움  
2️⃣ Fine-tuning 시 데이터 많이 필요  
3️⃣ 분포가 조금만 달라도 성능 급락

### 해결책
✔ 여러 Task를 동시에 수행할 수 있게 **일반화 강화**  
✔ 모델 크기 확대로 표현력 강화 → **Scaling Laws**

---

# 3. GPT-2 핵심 개념

## 언어 모델은 Unsupervised Multi-task Learner
- GPT-1과 구조 동일(Decoder-only Transformer)
- 파라미터 + 데이터 + max length 확대

## Input Format 통일 → Task 구분은 "지시문(prompt)"으로
예시

| Task | 입력 | 출력 |
|------|------|-----|
| 번역 | “번역해줘 : 영어 문장” | 번역된 문장 |
| QA | “질문에 답해라 : 문서 + 질문” | 답변 |

💡 Prompt Engineering의 초창기 형태

---

# 4. GPT-3 핵심 개념

## In-Context Learning (ICL)
- 모델을 **추가 학습하지 않음**
- 입력으로 준 예시를 보고 **추론만으로 적응**

| 유형 | 필요 데이터 | 특징 |
|------|------------|------|
| Zero-shot | 예제 X | 지시문만 보고 작업 이해 |
| One-shot | 1개 예시 | 간접적 규칙 학습 |
| Few-shot | 10~100개 예시 | Fine-tuning 없이 성능↑ |

➡ 사람 학습 방식과 유사해짐! 🤯

---

## GPT-3 성능 요약
- 번역 / QA / NLI / Reasoning 등  
- **학습 안 한 Task에서도 강력한 Zero-shot 성능**

---

# 5. 한계점(GPT-2,3)

### 모델 한계
- 반복적인 문장 생성
- 문맥 일관성 부족
- 논리/추론 비교 문제 약함
- 응답 간 모순 발생 가능

### 시스템 한계
- 거대한 모델 → **추론 비용↑**
- 특정 서비스 적용 → 비효율
- 원하는 task만 학습시키기 어려움

➡ 효율적인 추론 기술 및 모델 압축 필요 (Distillation 등)

---

# 📌 핵심 요약

| 구분 | GPT-1 | GPT-2 | GPT-3 |
|------|------|------|------|
| 목표 | 조건부 생성 모델 | Multi-task | Few-shot Generalist |
| Task 방식 | Fine-tuning | Prompt 기반 | ICL (Zero/Few-shot) |
| 학습 방식 | 생성 기반 PT + FT | Unsupervised MTL | Zero-shot Reasoner |

---

# 🎯 결론

> **Decoder-only 언어 모델은**
> - 언어 생성에 특화되었고
> - 규모 확장(Scaling Laws)으로
> - 학습 없이도 새로운 Task 해결(ICL) 가능하게 발전했다!

➡ 현재 GPT-4/5 시대의 기술적 뿌리가 됨 🌳✨
