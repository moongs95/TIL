# 언어모델이란 무엇인가?

---

# 1. 언어모델이란?

## 1.1 자연언어란?

**자연언어 (Natural Language)**  
- 인간의 언어  
- 정보 전달의 수단이며 인공언어와 대비되는 개념  

---

## 1.2 언어모델의 정의

언어모델(Language Model) = **지식 표현 체계**

컴퓨터가 자연언어를 이해할 수 있도록  
문장의 구성 요소(글자, 형태소, 단어, 단어열, 문단 등)에 **확률을 부여**하고,  
이 확률을 기반으로 **다음 단어를 예측하거나 문장을 생성하는 모델**.

**언어모델이란?**
- 단어 시퀀스에 확률을 부여(assign)
- 가장 자연스러운 단어 시퀀스를 찾거나 문맥 정보를 이해하는 모델
- 자연어의 규칙을 기계가 다룰 수 있도록 수학적으로 모델링한 것

---

# 2. 언어모델의 종류 및 특징

## 2.1 언어모델에 대한 흔한 오해
- 언어모델의 시작 = LLM? → ❌  
- 언어모델의 시작 = BERT or GPT? → ❌  
→ 훨씬 이전부터 존재했던 전통적 언어모델(LM)이 있음.

---

## 2.2 전통적인 언어모델의 역사

언어모델은 아래 순서로 발전:

1) 규칙기반 →  
2) 통계기반(단어 기반, 구문 기반) →  
3) 신경망 기반 →  
4) Transformer 기반 →  
5) LLM 기반

---

## 2.3 규칙기반 언어모델

- 언어의 **문법적 규칙을 사전에 명시**하고 그 규칙에 따라 문장을 분석
- 초기 NLP 연구 방법
- 한계:
  - 어순이 정형화되지 않으면 처리 어려움
  - 규칙 정의에 많은 비용 소요
  - 정확도 낮음

---

## 2.4 통계기반 언어모델

- 단어열이 가지는 **확률 분포**를 기반으로 다음 단어 조합을 예측
- 조건부 확률 기반 모델링  
  → 이전 단어가 주어졌을 때 다음 단어의 확률 P(wᵢ | wᵢ₋₁…)
- 실제 언어의 단어열 분포를 근사하는 것이 목표
- 대표 예: **N-gram 언어모델**

---

## 2.5 딥러닝 기반 언어모델

- 퍼셉트론 기반 신경망을 사용하여 **단어 의미적 유사성** 학습 가능
- 장점:
  - 문맥(Context) 반영
  - 희소성 문제 완화
  - 학습 데이터에 없는 문장도 문맥 기반으로 예측 가능

### 신경망 언어모델(NNLM)의 발전 단계
1. Feed-forward Neural LM  
2. RNN 기반 LM  
3. **Transformer 기반 LM (현대 NLP의 표준)**

---

# 3. Transformer 시대

Transformer 이후 NLP는 큰 변화가 생김.

## 3.1 Transformer의 영향력

Transformer 구조 기반으로 다양한 패밀리 모델 등장:

- Encoder-only → **BERT 계열**
- Decoder-only → **GPT 계열**
- Encoder-Decoder → **BART, T5, Transformer-XL 등**

---

## 3.2 Encoder vs Decoder

### Encoder
- 모든 단어에 동시에 어텐션 가능 → **양방향 이해**
- 문장 이해 중심 task에 적합
  - 문장분류
  - 감정분석
  - 자연어추론(NLI)
  - 문서 의미 파악 등

### Decoder
- 이전 단어(왼쪽 문맥)만 보고 다음 단어 생성 → **Auto-regressive**
- 생성 중심 task에 적합
  - 텍스트 생성
  - 대화 모델
  - 요약
  - 번역 생성 등

---

# 4. 대표적인 언어모델 구조

## 4.1 Encoder 기반 모델

### BERT
- Bidirectional Encoder
- **MLM (Masked LM):** 마스킹된 토큰 예측
- **NSP (Next Sentence Prediction)**

### RoBERTa
- 더욱 큰 데이터 + 더 긴 학습  
- NSP 제거 + Dynamic Masking  
→ BERT보다 성능 우수

---

## 4.2 Decoder 기반 모델

### GPT
- Auto-regressive
- 다음 토큰 예측
- Fine-tuning 없이도 좋은 성능 → **Zero-shot / Few-shot의 등장**

GPT 시리즈:
- GPT-1 → 사전학습의 효과 강조  
- GPT-2 → 대규모 LM의 강력함 발견  
- GPT-3 → 초거대 LM 시대 개막, Few-shot 달성  
- GPT-4 이후: 멀티모달 + 추론 성능 강화

---

## 4.3 Encoder-Decoder 기반 모델

### BART
- Encoder + Decoder 통합 모델
- 다양한 **denoising objective**로 pre-training
- 강력한 seq2seq 성능(요약, 자연어 생성 등)

### T5
- NLP 문제를 전부 **Text-to-Text** 형태로 통합한 모델
- Span-masking 기반 pre-training
- Multi-task learning 기반으로 강력한 범용성 제공

---

# 5. 자연언어처리 속 언어모델의 역할

## 5.1 NLP Task 관점: NLU vs NLG

### NLU (Natural Language Understanding)
기계가 언어를 **이해**하는 영역  
예:
- 감정분석
- 자연어추론(NLI)
- 유사도 예측
- 의도 분류
- 기계독해(MRC)

### NLG (Natural Language Generation)
기계가 언어를 **생성**하는 영역  
예:
- 요약
- 대화 생성
- 스토리 텔링
- 번역
- QA 생성

### NLU + NLG 함께 필요한 작업
- 기계독해(MRC)
  - 지문 이해(NLU)
  - 정답 문장 생성(NLG)

---

# 6. LLM의 등장 이후 변화

## 6.1 From LM → LLM

- 초거대 모델 하나로 다양한 Task 수행 가능
  - Prompting
  - Instruction tuning
  - RLHF
  - RAG 등

## 6.2 벤치마크 변화

기존 벤치마크는 모델 구분이 어려울 정도로 성능 정체  
→ LLM 평가 위해 더 어려운 **인간 수준의 Task** 등장  
- reasoning benchmark
- instruction following
- complex QA
- math, code generation 등

---

# 7. 실사용(Application) 관점에서 언어모델의 역할

## 7.1 NLP Application 시나리오

Core NLP Tasks → General Applications → Domain-specific Systems

### 예시 분야
- 기계번역 (MT)
- 음성인식 (ASR)
- Meeting Summarization
- Writing Assistant
- Grammar Error Correction
- Domain QA (의학, 법률 등)
- 코드 생성
- 검색엔진 (bing 등)
- Personalized Chatbot
- Recommendation System
- RAG 기반 QA 시스템
- Text-to-Image Generation (멀티모달)

### 최신 트렌드
- Universal Speech Model (텍스트 외 멀티모달 처리)
- Whisper 기반 음성 인식
- GPT+RAG 기반 검색형 AI Assistant

---

# 8. 핵심 메시지 요약

- 언어모델은 단순히 LLM이 아니라 **자연언어를 수학적으로 모델링하는 모든 기법의 총칭**  
- 규칙 기반 → 통계 기반 → 신경망 기반 → Transformer → LLM으로 발전  
- NLP Task는 NLU·NLG·Hybrid로 구분  
- LLM 이후 NLP는 “하나의 초거대 모델로 여러 Task 수행” 패러다임으로 전환  
- 실제 산업 적용에서는 RAG, 멀티모달, 대규모 사전학습 모델이 핵심 역할 수행
