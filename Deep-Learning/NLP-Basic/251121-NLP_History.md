# 🌟 자연언어처리의 역사 A to Z  
_규칙기반 → 통계기반 → ML/DL → 뉴럴심볼릭 → Pretrain-Finetuning → LLM 시대_

---

# 1. 규칙기반 및 통계기반 자연언어처리

---

# 1.1 규칙기반 NLP

### 특징
- 전문가(언어학자)가 만든 **규칙(rule)** 에 따라 처리
- Rule 생성을 위해 **전문 지식** 필요
- 자연어 문장 → 형태소 분석 → 구문 분석 → 의미 분석 → 담화 분석 → 결과

➡️ 이 시기에는 NLP 시스템이 **전문가 지식**에 크게 의존  
➡️ 소량의 고품질 규칙 기반

---

# 1.2 통계기반 NLP

### 특징
- **대량의 텍스트(빅데이터)** 기반 통계적 처리
- “모두(군중)”이 만든 데이터를 활용
- 단어 주변 등장 빈도 기반 의미 분석(분산 표현)

### 통계 기반 방법론
- 특정 단어 주변에 어떤 단어들이 **몇 번 등장하는지 카운트**
- 사람의 지식이 담긴 말뭉치에서 핵심적 규칙을 **자동 추출**
- 의미를 **벡터(분산 표현)** 로 표현 → 3차원 표현으로 설명되던 초기 시절

---

# 1.3 통계적 언어모델(SLM)

### 특징
- 이전 단어로부터 다음 단어의 **확률을 계산**
- 코퍼스에 등장하지 않은 단어 조합은 **예측 불가**
- Sparsity Problem(희소성 문제) 존재  
  → 데이터가 충분하지 않아 정확한 모델링 불가

---

# 1.4 규칙 기반 vs 통계 기반

| 규칙 기반 | 통계 기반 |
|----------|-----------|
| 전문가 중심 | 데이터 중심 |
| 적은 데이터로 동작 | 많은 데이터 필요 |
| 개발 복잡 | 개발 간단 |
| 논리적 추론 가능 | 경험 기반 확률적 접근 |

➡️ 결국은 **합리주의(rule)** vs **경험주의(데이터 학습 → ML/DL)**

---

# 2. 기계학습 및 딥러닝 기반 자연언어처리

---

# 2.1 ML & DL in NLP

### 시대 변화
- 전문가(rule) + 군중(빅데이터) 공존  
- GPU·컴퓨팅 파워 증가  
- 딥러닝 알고리즘 발전  

---

# 2.2 규칙 기반 vs ML/DL 기반

## 규칙 기반
- 적은 데이터로 일반화  
- 결론 도출 과정이 논리적·설명 가능  
- **전문가의 실력 이상으로 갈 수 없음**  
- 오류는 동일하게 반복  
- 구축 비용·시간 많이 듦  
- Toy task에 적합  

## 머신러닝/딥러닝 기반
- 데이터 양과 질이 높으면 **전문가 능력 초월**  
- 인간이 생각 못한 해결법(알파고 37·78수) 가능  
- Data hungry  
- 결과 해석 어려움  
- 귀납적 근사 기반  

### 구조 차이
- **ML:** input → feature extraction(사람) → 분류  
- **DL:** input → feature extraction+classification(기계) → output

---

# 2.3 Neural Machine Translation(NMT)

규칙 기반에서 형태소/구문 분석 필수  
→ NMT에서는 **병렬 말뭉치만 있으면 모델이 스스로 학습**

---

# 2.4 Supervised Learning Examples (전문가 데이터 기반)

- NER / RE: 문장 내 entity & relation 분류  
- NLI: Hypothesis가 premise와 일치?  
- QA: 질문에 맞는 답 생성 또는 선택  

---

# 2.5 Unsupervised Learning Examples (모두가 만든 데이터 기반)

### Language Model (LM)
- 단어 시퀀스에 확률 할당  
- 언어 자체를 모델링

### 지식 표현의 진화
Human text → NN → Numbers  
→ 기계가 이해할 수 있도록 인코딩 필요

- One-hot → word2vec(의미) → Context-LM(문맥) → BERT → GPT

---

# 3. 뉴럴심볼릭 기반 자연언어처리

딥러닝(연속) + 규칙/지식(이산) 결합

---

# 3.1 Neural-Symbolic 개념

딥러닝 + 지식베이스(Knowledge Graph)  
→ 딥러닝의 “추론 부족” 문제를 보완

### 방식
지식그래프(KG) → 임베딩 → 벡터 → 딥러닝 모델과 결합

---

# 3.2 뉴럴심볼릭 기술들

## Knowledge Base Question Answering  
지식베이스 기반 QA

## KGBERT
- KG triples(entity–relation–entity)을 텍스트처럼 인식  
- triple scoring  
- triple classification / link prediction 등 SOTA 달성

## Common Sense Knowledge Graph
- 상식 기반 추론  
- 작은 데이터로도 강력한 성능  

## Multi-hop QA
- 복수 개의 노드를 따라 추론해야 하는 QA  
- entity-relation graph 기반  
- 다중 reasoning 점프(홉)

---

# 4. Pretrain → Finetuning 기반 자연언어처리

좋은 언어모델(지식 표현) → 하위 task에 전이학습

---

# 4.1 Language Model 개념

- Pre-train(대중 unsupervised) + Fine-tune(전문가 supervised)
- 대량 말뭉치로 general language ability 습득  
- 이후 task-specific fine-tuning

---

# 4.2 Pretraining vs Finetuning

### Pretraining
- 목표 task와 관계 없는 대량 데이터로 사전 학습

### Finetuning
- 특정 task 데이터로 추가 학습

---

# 4.3 벤치마크 시대 등장
- 각 Task-specific dataset 출시  
- Leaderboard 성능 경쟁 증가  

---

# 4.4 Transformer 이후 발전

Transformer → NLP 연구의 중심

### Variants
- Encoder-only: BERT  
- Decoder-only: GPT  
- Encoder–Decoder: BART, T5  
- Transformer-XL 등  
- 다양한 pre-training task 등장(mask, denoise 등)

---

# 4.5 Language Model 계보 요약

Seq2Seq → Attention Seq2Seq → Transformer → GPT-1 → BERT → GPT-2 → XLNet → RoBERTa → MASS → BART → MT-DNN → T5 → GPT-3 → GPT-4 …

➡️ 점점 더 언어 능력을 잘 이해하고 생성하는 방향으로 진화

---

# 5. LLM 기반 자연언어처리

규칙 → 통계 → ML → DL → 뉴럴심볼릭/프리트레인 → Transformer → LLM

---

# 5.1 Large Language Models

### Scaling Laws (OpenAI)
- 모델 크기 ↑ → 성능 ↑  
- Model size > Batch size > Steps  
- 모델 크기가 **성능에 가장 큰 영향**  
→ Upscaling 중요

---

# 5.2 Foundation Models

과거: task마다 모델 1개씩 필요  
현재: 하나의 foundation model → 모든 task 수행 가능  

---

# 5.3 Few-shot & Prompt Learning
모델이 너무 커서 가중치 업데이트가 어려움  
→ 예시(prompt)만 주면 학습 없이도 수행

---

# 5.4 주요 LLM 예시

## OpenAI GPT-3
- Transformer Decoder  
- 175B parameters  
- 45TB 학습  
  - Common Crawl  
  - WebText2  
  - Books1/2  
  - Wikipedia  

## Google PaLM  
## Meta LLaMA, LLaMA2 (코드 생성 능력 강화)  
## OpenAI DALL·E (Text → Image)  
## Kakao KoGPT (한국어 특화)  
## Kakao MinDALL·E  
## Naver HyperCLOVA  
- 204B  
- 560B tokens  
- 블로그, 카페, 뉴스, 댓글, 지식인 등 한국어 대규모 데이터  

## LG EXAONE  
- 300B parameters  
- 6천억 말뭉치 + 2.5억 이미지-텍스트 페어  

## ChatGPT
- 사람의 피드백 데이터 기반  
- SFT + RLHF  
- 사람의 지시(instruction)에 최적화  
- 검색을 “탐색”에서 “생성”으로 바꾼 혁신

---

# 5.5 Prompt Engineering
모델에게 **지시를 잘하는 기술**  
→ 새로운 직군으로 등장

---

# 6. Continual Learning

기업은 특정 모델을 지속적으로 업데이트해야 함  
→ 로그 기반 지속적 학습  
→ 실제 비즈니스 환경에서 중요

---

# 7. Ethics & Fairness

기술이 아무리 좋아도 **윤리 문제**가 있으면 사용 안 됨  
ChatGPT 포함 LLM → 완전한 무결성 없음(편향 존재)

### Fairness NLP
현실의 데이터 편향을 최소화하는 연구  
- 사회적 편향  
- 문화적 차이  
- 언어적 편향

### NMT의 위험성
- 오역은 경제적·법적 문제로 연결  
- 안전 관련 심각한 오류 가능  
- 성·인종적 발언 확대 가능  
→ 치명적 오류 감지(CED) 연구 진행 중
