# LLM 기반 Data-Centric NLP 연구

## 1. LLM 학습 데이터 종류

### 1.1 사전 학습을 위한 학습 데이터

#### LLM 학습 파이프라인
```
Pre-Training → SFT → RLHF → Downstream Application
```

---

#### 사전 학습 데이터 (Pre-training Data)

**데이터 소스**:
- 웹 데이터: Wikipedia, News, Reviews 등
- **데이터의 품질 및 다양성이 모델의 성능에 큰 영향을 줌**
- ⇒ **데이터 전처리 작업이 중요**

**전처리 작업**:
- 품질 및 성능 보장을 위한 필터링
- 중복 제거 (De-duplication)
- **영어의 경우**: Common Crawl, WebText2, BookCorpus, Wikipedia 등 활용

---

#### 사전 학습 데이터의 품질 및 다양성

**핵심 요소**:
- **"Age" (데이터의 최신성)**
- **"Quality" (데이터의 품질)**
- **"Composition (Domain)" (데이터의 구성 및 도메인)**

**가장 중요한 요소**:
- **다양한 Data sources에 대한 coverage가 가장 큰 영향을 줌**

---

#### 사전 학습 데이터 구성의 예

**GPT-3**:
```
- Common Crawl (filtered)
- WebText2
- Books1
- Books2
- Wikipedia
→ Total: 300 billion tokens
```

**LLaMA 1**:
```
- Common Crawl
- C4
- Github
- Wikipedia
- Books
- ArXiv
- StackExchange
→ Total: 1.4T tokens
```

---

#### 태스크 특화 사전 학습 (Task-Specialized Pre-training)

**개념**:
- 특정 작업에 특화된 언어 모델을 구축하는 방법
- **사전 학습 단계에서 특정 도메인의 데이터를 높은 비율로 구성하여 모델을 학습**

**대표 사례**:

**1. LaMDA (Language Models for Dialog Applications)**
```
목적: 대화 어플리케이션 구축
데이터 구성: 전체 사전학습 데이터 중 약 50%를 대화 데이터로 할당
```

**2. BLOOM, PaLM**
```
목적: 다국어 특화 LLM 구축
데이터 구성: 다양한 언어권의 텍스트를 사전 학습에 함께 활용
```

**3. Galactica**
```
목적: 과학 도메인 특화 LLM 구축
데이터 구성: 사전학습 데이터의 약 86%를 과학 데이터로 사용
```

**4. AlphaCode**
```
목적: 코드 생성 특화 LLM 구축
데이터 구성: 사전학습 데이터를 전부 코드 데이터로 사용
```

---

### 1.2 미세 조정을 위한 학습 데이터

#### 미세 조정 데이터 (Fine-tuning Data)

**정의**:
- 사전 학습된 모델을 특정 작업에 특화된 데이터셋으로 튜닝하여 활용할 때 사용되는 데이터

**사전 학습 데이터와의 차이점**:
- **입력에 대응하는 정답(출력 또는 선호하는 결과)이 존재**

**두 종류의 미세 조정 방법론**:

1. **Instruction Tuning (지시어 튜닝)**
   - 지시어(Instruction)와 대응하는 출력(Answer)로 구성된 데이터로 모델 학습
   - 언어 모델의 자연어 지시에 대한 일반화 성능을 높임

2. **Alignment Tuning (정렬 튜닝)**
   - 사람의 선호도(Human preferences)가 반영된 데이터로 모델을 학습

**데이터 변환**:
- LLM 이전에 활용되던 비-자연어 형식의 데이터는 Instruction과 같은 자연어 형태로 변환하여 LLMs 미세 조정에 활용

---

#### 사전 학습과 미세 조정: InstructGPT 예시

**과정**:
```
사전 학습된 모델
  ↓
Instruction Tuning
  ↓
Preference Tuning (RLHF)
  ↓
InstructGPT
```

---

#### Instruction Dataset (지시어 데이터셋)

**Instruction Tuning**:
- **언어 모델이 자연어 형태의 지시사항(Instruction)을 이해할 수 있도록 하는 미세조정 방법론**

**Instruction Dataset 구성**:
1. **지시어 (Instruction)**: 해결하고자 하는 작업을 LLM이 이해할 수 있도록 하는 자연어 설명
2. **출력 (Answer)**: 지시사항에 대응하는 정답 생성 결과

**특징**:
- 기존의 지도학습 패러다임과 유사
- **비교적 적은 수의 예제만으로 높은 성능 및 새로운 태스크에 대한 일반화가 가능**
- 더욱 효율적인 학습 패러다임
- **데이터셋의 형식 및 품질이 중요함**

**목표**:
- 다양한 분야에 대한 지시어로 학습한 모델을 Unseen task에 대한 일반화

---

#### Alignment Tuning (정렬 튜닝)

**정의**:
- **언어 모델을 특정 작업이나 대상(인간 등)의 preferences에 따라 튜닝하는 것**
- 일반적으로 Instruction Tuning이 Alignment Tuning에 포함
- 여기서는 Preference learning의 관점으로 언급

**발전 과정**:
```
RLHF → DPO
(Reinforcement Learning from Human Feedback → Direct Preference Optimization)
```

---

#### RLHF 관련 연구

**1. Training language models to follow instructions with human feedback**
```
방법:
1. Fine-tuned GPT-3를 활용
2. 다양한 결과를 생성
3. Human preference annotation에 기반한 데이터셋 구축
4. Preference 데이터 기반 RLHF 학습
```

**2. Constitutional AI: Harmlessness from AI Feedback**
```
문제점: RLHF가 효과적이나, 고품질 human preference annotations를 수집하는 비용/시간이 큼

해결책: Human labels 없이 Harmful output 식별을 위한 AI assistant를 학습/활용
```

**3. RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback**
```
연구 내용: Aligned AI preference를 생성하는 기술에 대한 광범위한 연구 수행

결과: RLAIF가 인간 수준의 성능을 달성
```

**4. DPO: Direct Preference Optimization**
```
문제점:
- Preference data 구축도 문제
- RLHF는 학습 프로세스 자체가 불안정
- Human preferences를 학습하면서 기존의 분포에서 너무 크게 벗어나지 않도록 유지하는 등의 복잡한 학습 과정 요구

해결책: Preference data로부터 "directly" LM을 학습하는 방법론 제안
```

---

## 2. LLM 데이터 전처리

### 2.1 LLM 데이터 전처리

#### 자연어 처리에서의 데이터 품질의 중요성

**핵심**:
- **데이터 양 vs. 품질**: 양도 중요하지만, **품질 및 다양성이 더 중요!**
- Robust (견고성)
- 중복 제거 (De-duplication)

---

#### 기존 LLM의 데이터 전처리: GPT-3

**1. Data Filtering (데이터 필터링)**
```
방법: CommonCrawl 데이터에 대하여 Similarity 기반 filtering 작업 수행
- High quality document를 분류하는 classifier를 학습하여 활용
```

**2. Deduplication (중복 제거)**
```
방법: Fuzzy deduplication을 document level로 수행
- 문서의 특징에 기반한 Hashing 방법론 활용
- Spark's MinHashLSH 구현체 활용

효과:
- 전체 데이터 집합의 크기를 10% 줄임
- 과적합을 방지 (모델의 스케일이 커질수록 더 중요)
```

**3. Diversify (다양화)**
```
방법: WebText, Books1, Books2, Wikipedia 등의 이미 알려진 high-quality corpora를 추가로 활용
```

---

#### 기존 LLM의 데이터 전처리: LLaMA

**1. Data Filtering (데이터 필터링)**

**a. 언어 식별**
```
- FastText 선형 분류기를 활용한 언어 식별
- 비영어 페이지 제거
```

**b. 품질 필터링**
```
- N-gram 언어 모델을 활용한 low-quality filtering
- Wikipedia에 대하여 참조된 페이지 분류 모델을 구축
  → 참조로 분류되지 않은 페이지 제거
```

**c. 휴리스틱 기반 필터링**
```
- 구두점의 존재 유무
- 웹 페이지의 단어 및 문장 수
- 기타 휴리스틱 기반 품질 필터링 수행
```

**d. 형식 정리**
```
- Github and Wikipedia: 정규 표현식 등을 활용하여 하이퍼링크/주석/헤더 등 기타 형식화된 부분 제거
```

**2. Deduplication (중복 제거)**
```
- Line-level 중복 제거 수행
- Books의 경우 내용이 90% 이상 겹치는 책 제거
```

**3. Diversify (다양화)**
```
데이터 소스:
- CommonCrawl
- C4
- GitHub
- Wikipedia
- Books3
- ArXiv
→ 다양한 소스를 혼합
```

---

## 3. LLM 기반 라벨링 연구

### 3.1 LLM 기반 데이터 라벨링

#### LLM 기반 데이터 라벨링

**정의**:
- 새로운 데이터를 구축하거나 기존의 데이터를 **증강(Augmentation)**하는 데 LLM을 활용하는 연구 분야

**두 가지 방법**:

**1. LLM 기반 데이터 합성 (Data Synthesis)**
```
- 라벨링 정보가 존재하지 않는 데이터를 입력
- LLM을 활용하여 라벨링
```

**2. LLM 기반 데이터 증강 (Data Augmentation)**
```
- 라벨링 정보가 존재하는 데이터를 입력
- LLM을 활용하여 데이터의 양/품질을 개선
```

---

# LLM 기반 Model-Centric NLP

## 1. LLM Tuning

### 1.1 Fine-Tuning

#### LLM Fine-Tuning

**정의**:
- Fine-Tuning은 LLM 이전 세대부터 사용되던 용어
- **사전학습된 모델을 특정 작업에 특화 학습하는 과정**을 칭함

**LLM Fine-tuning**:
- 일반적으로 **Instruction Tuning을 지칭**

**문제점**:
- LLM은 **방대한 수의 파라미터**를 가짐
- **Tuning에 많은 Computation resources가 요구됨**
- ⇒ **Parameter Efficient Tuning 필요**

---

#### General Pipeline of Instruction Tuning

**Step 1: Instruction Dataset Construction (지시어 데이터셋 구축)**
- 다양한 태스크에 대한 지시어-답변 쌍 수집

**Step 2: Instruction Tuning (지시어 튜닝)**
- 구축된 데이터셋으로 모델 학습

---

### 1.2 Parameter Efficient Tuning

#### Parameter Efficient Tuning (파라미터 효율적 튜닝)

**정의**:
- **LLM 전체가 아닌 일부분만을 튜닝하는 방법론**

**주요 방법**:
- Adapter-based Fine-tuning
- Prefix-tuning
- 등등

---

#### 튜닝 방법의 분류

**1. Weight Tuning (가중치 튜닝)**
```
- Fine-Tuning
- Adapter Tuning
```

**2. Input Engineering (입력 엔지니어링)**
```
- Prompt Tuning
- Instruction Tuning
```

**3. Database Augmentation (데이터베이스 증강)**
```
- Language Model Augmentation
- Multimodal Model Augmentation
```

---

#### Adapter-based Tuning

**개념**:
- **기존 모델과 별도의 파라미터를 가진 Adapter module을 기존 model에 추가하여 학습**

**방법**:
- 일반적으로 기존 모델의 파라미터는 freeze
- Adapter만을 학습

---

#### LoRA (Low-Rank Adaptation of Large Language Models)

**개념**:
- **Gradient values (ΔW)를 low-rank r로 mapping 해주는 행렬 A, B를 학습**

**장점**:

**1. Memory and Storage Usage 절약**
```
GPT-3 175B의 경우:
- 1.2TB → 350GB VRAM으로 감소
- Checkpoint size: 350GB → 35MB로 감소 (r=4)
```

**2. Training Speed 향상**
```
- 약 25% 증가 (GPT-3 175B 기준)
```

**3. Fast Task Switching**
```
- LoRA weights만 교체하여 Task 사이의 빠른 전환 가능
```

---

#### QLoRA (Efficient Finetuning of Quantized LLMs)

**3가지 핵심 Components**:

**1. 4-bit NormalFloat (NF4)**
```
- 입력 텐서의 분포가 고정되어 있을 때
- 각 분위 구간에 동일한 수의 값을 할당
- 신경망의 가중치를 효율적으로 표현
- 메모리 사용량을 줄이면서 성능 손실을 최소화
```

**2. Double Quantization (이중 양자화)**
```
- 입력 값의 비트 수를 양자화할 때 사용되는 Quantization constants를 다시 양자화
- 메모리 사용량: 평균 0.5비트 → 0.127비트로 감소
- 파라미터당 0.373비트의 메모리 절감
```

**3. Paged Optimizer (페이징 옵티마이저)**
```
- NVIDIA unified memory feature 기반
- GPU 메모리 부족 상태가 되면:
  → Optimizer state에 대한 페이징 메모리를 CPU RAM으로 이동
  → State update가 필요할 때 다시 GPU로 페이지를 되돌림
```

---

#### Prefix-Tuning

**개념**:
- **Transformer layer에 입력되는 input token의 앞에 trainable parameters를 추가**
- **해당 parameters만 튜닝하는 방법론**

**방법**:
- 입력의 prefix에 matrices (Soft-Prompt 형태)를 각 Layer마다 추가
- 기존 모델의 Parameters는 freeze
- Prefixes만을 학습

**성능**:
- **0.1%만의 파라미터로, full data fine-tuning과 비슷한 성능 달성**

---

#### LLaMA-Adapter

**특징**:
- **LLaMA를 Freeze, 1.2M의 Adapter만을 학습**
- Zero-initialized gating 방법론 적용
- Randomly Initialized Prompt의 학습을 최적화
- **Plug and Play! Multi-Modal Instruction!**

**Multimodality (멀티모달리티)**:
```
- CLIP과 같은 Pre-trained Vision Models를 결합
- 이미지의 Global Features를 추출
- Adapter Prompt에 결합을 통해 Multimodal 모델링 가능!
```

---

## 2. Domain Specialization (도메인 특화)

### 2.1 Domain Specialization

#### Domain Specialization이란?

**문제점**:
- **General Domain의 데이터로 사전학습된 언어 모델은 특정 Domain에 대한 이해력이 부족함**

**정의**:
- **Domain Specialization은 언어 모델을 특정 Domain에 대한 데이터로 특화 학습시키는 과정**

---

#### Domain Specialization의 4가지 방법

**1. Deploying LLM without Domain Specialization**
```
LLM → General Text → Domain Task
(도메인 특화 없이 그냥 사용)
```

**2. Retrieval Augmented Domain Specialization**
```
LLM → General → External Knowledge → Domain Task
(외부 지식 검색을 통한 특화)
```

**3. Instruction-crafting-based Domain Specialization**
```
LLM → General Text → Instructions → Domain Task
(지시어 기반 특화)
```

**4. Knowledge-updated Domain Specialization**
```
LLM → General text → Fine-tune → Domain-specific Knowledge/Task → Domain Task
(지식 업데이트를 통한 특화)
```

---

### 2.2 Knowledge Augmentation (지식 증강)

#### External Augmentation (외부 증강)

**정의**:
- **외부 소스에서 관련 정보를 검색하여 모델의 파라미터를 미세 조정하지 않고 도메인 지식을 향상시키는 Retrieval Augmentation**

---

#### Retrieval-Augmented Generation with LLMs

**방법**:
- 검색 모듈 (Dense Retriever 또는 Search API)를 활용
- 검색된 Domain Context를 Prompt에 포함
- **Domain Knowledge를 Model Tuning 없이 In-Context Learning을 통해 학습**

---

#### Verify-and-Edit: A Knowledge-Enhanced Chain-of-Thought Framework

**개념**:
- **Chain-of-Thought (CoT) prompting에 External Augmented Knowledge에 기반한 Verification process 제안**

**과정**:
1. Reasoning Step의 각 단계를 검색된 지식에 기반하여 Editing
2. Edited reasoning step에 기반하여 새롭게 정답 예측

---

### 2.3 Domain Tuning

#### Knowledge-updated Domain Specialization

**방법**:
- **General Text에 사전 학습된 LLM을 Domain-specific corpus로 Tuning**

---

# LLM 기반 Evaluation-Centric NLP

## 1. LLM Evaluation

### 1.1 Evaluation (평가)

#### 언어모델에서의 평가

**패러다임 변화**:
```
기존: 사람이 평가
현재: LLM이 평가
```

---

### 1.2 Interpretability (해석 가능성)

#### LLM의 평가 방법

**문제점**:
- LLMs의 엄청난 생성 능력
- 그러나 Interpretability는?

**해결책**:
- **LLMs를 평가할 때 작업의 특성을 고려하여 세분화하여 평가해야 함**
- ⇒ **인간 평가와 더 높은 상관 관계**

---

#### 주요 연구 사례

**1. 모델 지식과 검색된 지식의 충돌 분석**
```
방법: Counter-Memory 구축

결과:
- LLM이 parametric knowledge에 의존하는 경향
- Counter-memory가 높은 일관성을 보이는 경우 잘 수용
- 문제: Counter-memory가 잘못된 정보이므로, LLM이 이러한 오류에 속아 잘못된 정보 제공 가능
```

**2. Evidence의 순서가 성능에 영향**
```
발견: Evidence(증거)의 순서조차도 성능에 영향을 줌
```

**3. LLMs를 Examiner로 활용**
```
결과: LLM as Examiner? 인간 선호도와 80% 이상 일치하는 결과
```

**4. 새로운 지식 처리 능력 평가**
```
목적: 빠르게 진화하는 세계에서 중요하고 어려운 측면인 새로운 지식을 처리하는 LLM의 능력을 평가
```

**5. LLM의 Factual Knowledge 평가**
```
목적: LLM's factual knowledge의 정도와 범위를 종합적으로 평가
```

**6. Knowledge-intensive Tasks 분석**
```
방법: Knowledge-intensive tasks에 대하여 심층 분석 수행
```

**7. Hallucination 평가**
```
방법: LLMs의 Hallucination(환각)을 평가하기 위한 benchmark dataset 제안

결과:
- 기존 LLMs는 hallucinated contents에 대한 구분 능력이 부족
- 완화를 위해 retrieval augmentation이 효과적
```

---

### 1.3 Ethics/Trustworthiness (윤리/신뢰성)

#### 주요 연구 사례

**1. ChatGPT의 Toxicity 평가**
```
결과: 특정 persona가 할당된 경우, Toxicity(독성) 최대 6배 증가
```

**2. LLMs의 편향성 분석**
```
목적: LLMs의 편향성에 대한 분석 수행
강조: 개발자로서의 책임감 강조
```

**3. ChatGPT의 MBTI 및 정치 편향성**
```
결과: ENFJ
```

**4. Sycophancy (아첨) 이해도**
```
질문:
- Can LLMs understand "Sycophancy"? (LLMs가 "아첨"을 이해할 수 있는가?)
- How much does "Sycophancy" affect the behaviors of LLMs? (아첨이 LLMs의 행동에 얼마나 영향을 미치는가?)

참고: Sycophancy = 아첨, 아부
```

**5. Positional Bias (위치 편향)**
```
발견: Candidate responses의 순서만 바꿔도 성능이 변화함!

해결책: Calibration framework 제안
- Multiple Evidence Calibration (MEC)
- Balanced Position Calibration (BPC)
```

---

## 2. LLM Leaderboard

### 2.1 LLM Leaderboard

#### Open LLM Leaderboard

**운영**:
- 세계 최대 머신러닝 플랫폼 Hugging Face에서 운영

**기능**:
- 전 세계 테크 기업과 연구기관이 개발하여 업데이트한 AI 모델을 평가
- 순위를 매겨 Open LLM의 성능을 비교

---

# LLM 기반 Application 연구

## 1. LLMOps

### 1.1 LLMOps

#### LLMOps의 개념

**정의**:
- **LLMOps (Large Language Model Operations)**
- LLMs 운영 관리(학습/배포)에 활용되는 사례, 기술 및 도구 등을 포괄하는 개념

---

#### LLMOps and MLOps

**유사점**:
- MLOps와 유사한 기술로 구성
- 데이터, 모델 학습 및 서빙

**차이점**:
- **모델의 규모가 다름**

---

#### LLMOps의 특수성

**1. 모델 사이즈 (Model Size)**
```
문제:
- 모델의 크기가 매우 큼
- High Computational Resources 필요

요구사항:
- 최적화 및 병렬 처리와 같은 시스템 요구
```

**2. 데이터의 특수성 - 데이터 크기 및 형식**
```
고려사항:
- LLMs를 학습하는 데 필요한 데이터의 크기
- 데이터의 형태 (Prompt Engineering 등)
```

**3. 데이터의 특수성 - Prompt Engineering**
```
목적:
- LLM의 창발 능력을 위한 In-Context Learning을 극대화

특징:
- LLM은 특정 작업 특화하도록 구축할 수도 있음
- 여러 작업에 일반화되도록 구축되는 경우가 다수
- 특정 작업에 대한 능력을 향상시키기 위하여 적합한 지시어 및 예제 제공
```

**4. Generative Models (생성형 모델)**
```
고려사항:
- 생성형 모델의 특성으로 인한 출력 결과의 다양성
- 성능 평가/인간 평가 세분화
- 윤리적 문제, 편향성 및 환각 현상 고려한 Post-processor 고려 필요
```

**5. Serving (서빙)**
```
배포 형식:
- API 앱 형식의 배포
- 대화형 챗봇, 어시스턴트, 작업 특화 파이프라인 등

원인:
- 모델의 크기나 전/후처리의 방대함
```

---

## 2. Augmented LLMs (증강 LLMs)

### 2.1 Augmented LLMs

#### Augmented LLMs?

**정의**:
- **LLM을 서비스에서 활용하는 방식**

---

#### 주요 방법

**1. RAG + LLM**
```
RAG (Retrieval-Augmented Generation) + LLM
```

**2. Self-Improvement**
```
방법: LLM 자체의 능력에 기반한 Self-Improvement로 데이터 증강
결과: 추가 튜닝

예시: Self-debug
```

**3. LM vs LM**
```
방법: 언어 모델끼리의 상호작용
목적: 사실적 오류 탐지
```

**4. LLM + 외부 plugin, tool**
```
방법: 외부 plugin, tool을 활용해서 모든 것 패키징, 서비스화
결과: LLMOps
```

---

# LLM 기반 Prompt Engineering 연구

## 1. Prompt Engineering

### 1.1 Overview

#### Prompt Engineering

**목적**:
- **Prompt Engineering의 종류를 유형화하고 연구**

**핵심 개념**:
- **LLM의 In-Context Learning (ICL) 능력을 활용하기 위함**

---

#### Prompt Engineering이란?

**정의**:
- **요구하는 작업을 지시하기 위한 작업!**
- 예: 요약? 분류? 추출?

**LLM 시대의 Prompt Engineering**:
- Task 수행을 위한 Template, Task Example, Answer Engineering 등의 **Hard Prompt**를 구성하는 방법을 주로 칭함

---

#### LLM Prompt의 구성 요소

**3가지 핵심 요소**:
1. **Task Instruction (작업 지시)**
2. **Demonstrations (Examples) (예시)**
3. **Query (질의)**

**고려사항**:
- 수학적 추론, 데이터 추론, 상식 추론 등
- **수행하고자 하는 작업에 맞는 특성을 고려해야 함**

---

### 1.2 Related Study (관련 연구)

#### Chain-of-Thought Prompting

**배경**:
- **수학적 추론에 특히 약한 LLMs**

**해결책**:
- **단계적 사고를 하도록 유도**

**방법**:
- Diverse tasks에 대한 Human-crafted examples를 LLMs에 제공

---

#### Least-to-Most Prompting

**배경**:
- CoT Prompting의 More complex problems에 대한 한계점

**해결책**:
- **복잡한 문제를 하위 문제로 분해 및 순차적 해결**
- **분할 정복 (Divide and Conquer) 방식**

---

#### Automatic Chain of Thought Prompting

**문제점**:
- CoT는 Manually-crafted CoT Examples에 의해서 고품질 추론을 유도
- ⇒ **Human effort가 많이 듦**

**발견**:
- Query와의 Similarity 기반 Example Retriever를 활용이 Random Retriever보다 낮은 성능!??
- ⇒ **Diversity 문제, random이 더 나음**

**해결책**:
- **유사도로 Clusters 구축한 뒤, 각 Cluster에서 예제 선정**
- Cluster를 문제 해결에 대한 다양성의 척도로 활용

---

#### Plan-and-Solve Prompting

**방법**:
- **Planning First and Solving**
- 먼저 계획을 세우고 해결

**성능**:
- **Zero-Shot에서도 Few-shot Manual-CoT와 유사한 성능!**

---

#### Self-Instruct

**배경**:
- "Instruction-tuned" LLM의 높은 일반화 성능
- ⇒ **고품질의 human-crafted Instruction에 의존적**

**해결책**:
- **LM을 활용하여 고품질의 Instruction dataset을 자동으로 구축하는 방법론 제안**

---

#### 그 외 연구

**1. 입력 예제의 순서에 따라 성능의 편차 발생**

**2. 여러 tasks의 데이터를 활용**
- Retriever 스스로 high-quality candidates를 찾아내도록 학습

---

## 2. LLM Tools

### 2.1 LangChain

#### LangChain: LLM 밀키트

**특징**:
- **단 코드 몇 줄로 LLM 사용**

---

#### LangChain의 주요 기능

**지원 기능**:
- 임베딩 (Embeddings)
- 문서 검색 (Document Retrieval)
- Prompt Engineering
- Chains
- Agent
- 등의 다양한 기능 지원

---

#### LangChain Components

**모듈 구성**:
- LangChain Components는 모듈화되어 있음
- Chains를 활용하여 조합하여 활용

**주요 Components**:

**1. 📃 Model I/O**
```
포함 내용:
- 프롬프트 관리
- 프롬프트 최적화
- 모든 LLM에 대한 일반적인 인터페이스
- LLM과 작업하기 위한 유틸리티
```

**2. 📚 Retrieval**
```
포함 내용:
- 외부 데이터 소스와 상호 작용
- 생성 단계에서 사용할 데이터를 가져와서 활용할 수 있도록 하는 기능
```

**3. 🤖 Agents**
```
포함 내용:
- LLM이 어떤 작업을 수행할지 결정
- 해당 작업을 수행하도록 하는 요소
```

---

### 2.2 Auto GPT

**정의**:
- **사용자가 설정한 목표를 GPT끼리의 상호작용을 통해 자율적으로 달성하도록 하는 Open-source project**

---

### 2.3 Scikit LLM

**기능**:
- **LLMs을 Scikit-learn 방식으로 활용할 수 있는 인터페이스 제공**
- ⇒ **접근성 향상**

---

## 전체 요약

### Data-Centric NLP 핵심 요약

| 단계 | 핵심 내용 |
|------|----------|
| **Pre-training Data** | 품질, 다양성, 최신성이 중요 |
| **Fine-tuning Data** | Instruction & Preference 데이터 |
| **Data Preprocessing** | Filtering, Deduplication, Diversification |
| **LLM-based Labeling** | 데이터 합성 및 증강 |

---

### Model-Centric NLP 핵심 요약

| 방법 | 설명 | 파라미터 비율 |
|------|------|-------------|
| **Full Fine-tuning** | 전체 모델 학습 | 100% |
| **LoRA** | 저차원 분해 행렬 학습 | 0.1% |
| **QLoRA** | 양자화 + LoRA | 0.01% |
| **Prefix-Tuning** | Prefix만 학습 | 0.1% |

---

### Evaluation-Centric NLP 핵심 요약

**평가 영역**:
1. **Interpretability**: 해석 가능성
2. **Ethics**: 윤리성, 편향성
3. **Trustworthiness**: 신뢰성, Hallucination
4. **LLM as Evaluator**: LLM이 평가자 역할

---

### Application 핵심 요약

**LLMOps 특수성**:
1. 모델 사이즈
2. 데이터 특수성
3. Prompt Engineering
4. 생성형 모델 특성
5. 서빙 방식

**Augmented LLMs**:
1. RAG (검색 증강)
2. Self-Improvement (자가 개선)
3. LM vs LM (모델 간 상호작용)
4. External Tools (외부 도구 연동)

---

### Prompt Engineering 핵심 요약

| 기법 | 설명 | 특징 |
|------|------|------|
| **Chain-of-Thought** | 단계적 사고 유도 | 추론 능력 향상 |
| **Least-to-Most** | 문제 분해 후 해결 | 복잡한 문제 해결 |
| **Auto-CoT** | 자동으로 예제 선정 | Human effort 감소 |
| **Plan-and-Solve** | 계획 후 실행 | Zero-shot 성능 우수 |
| **Self-Instruct** | 자동으로 Instruction 생성 | 데이터 의존성 감소 |

---

### 주요 도구

**1. LangChain**
```
특징: LLM 밀키트
구성: Model I/O, Retrieval, Agents
```

**2. Auto GPT**
```
특징: GPT끼리 상호작용하여 목표 자율 달성
```

**3. Scikit LLM**
```
특징: Scikit-learn 방식으로 LLM 사용
```

---

## 핵심 Takeaway
```
📊 Data-Centric: 품질 > 양, 전처리가 핵심

🔧 Model-Centric: PEFT로 효율적인 학습, LoRA/QLoRA 활용

📈 Evaluation: 다각도 평가, LLM이 평가자 역할

🚀 Application: LLMOps, RAG, 외부 도구 연동

✍️ Prompt Engineering: CoT, 자동화, 다양성 확보

🛠️ Tools: LangChain, Auto GPT, Scikit LLM
```
