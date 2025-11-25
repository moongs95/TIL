# 🌟 Encoder Model (BERT) 완전 정리

---

# 1. Transfer Learning이란?

## 1.1 출현 배경

### 딥러닝의 발전
- Word2Vec, GloVe 등 단어 임베딩 기법으로 단어를 벡터로 표현  
- CNN, RNN, LSTM 기반 자연어 처리 모델 급성장  

### 기존 단어 임베딩의 한계 — 언어의 모호성
- 단어가 어디에서 등장하든 동일 벡터(문맥 고려 불가)  
- 다의어(예: "bank") 의미 구분 불가능  
- 문맥 기반 임베딩 필요성 증가 → context vector 중요  

### 대용량 학습 데이터 필요 → Transfer Learning 등장

### Transfer Learning
- 한 task에서 학습된 모델을 **다른 task에 재사용**하는 기술

### Transfer Learning in NLP
- 대량의 비라벨 코퍼스로 언어 모델 사전 학습  
- 학습된 PLM(Pretrained Language Model)을 다양한 NLP task에 활용  

---

## 1.2 Pre-training & Fine-tuning

### Pre-training
- Downstream task 학습을 위한 파라미터 초기화  
- 대규모 unlabeled corpus로 학습  
- 언어적 특징을 폭넓게 습득  

### Fine-tuning
- 특정 task(SA, QA, NER 등)에 맞게 파라미터 미세 조정  

### Transfer Learning의 효율성
- 풍부한 언어 지식을 사전학습으로 확보  
- unlabeled 데이터 활용 → 무한 확장성  
- downstream task에서 빠른 수렴, 적은 리소스 요구  

결론: **빠름 + 효율적 + 성능 좋음**

---

## 1.3 ELMo

### ELMo 개념
- 문맥 정보를 반영한 contextual embedding  
- 문장 전체를 보고 단어 임베딩 생성  
- bi-LSTM 기반 언어 모델  

### 구조
- 순방향 LSTM + 역방향 LSTM(독립적 구성)  
- 상단 LSTM → 문맥적 의미  
- 하단 LSTM → 문법적 형태  

### Pre-training 방식
- 다음 단어 예측(Language Modeling)으로 사전학습  
- 문맥에 따라 단어 임베딩이 달라짐  

### Contextualized Word Embedding
- 순방향 hidden vector + 역방향 hidden vector + 토큰 embedding 조합  
- task 별 가중치를 달리하여 embedding 구성  

### 기존 방식 대비 강점
- 다의어 의미 표현 가능  
- 문맥 변화 반영 가능  
- 적은 데이터에서 큰 성능 향상  

### 한계점
- forward/backward LM이 **독립 학습**됨  
- 두 방향 정보를 완전히 통합하지 못함  
- 양방향 문맥을 **동시에 학습하지 못함**  

---

# 2. BERT 이해하기

## 2.1 BERT 개요

BERT: Bidirectional Encoder Representations from Transformers

### 핵심 특징
- Transformer의 **Encoder만** 사용  
- MLM(Masked Language Model)으로 **양방향 학습**  
- NSP(Next Sentence Prediction)으로 문장 관계까지 학습  
- Wikipedia + BooksCorpus 기반 대규모 Pre-training  

### ELMo vs BERT
- ELMo: LSTM 기반, 양방향 LM이 분리  
- BERT: self-attention 기반, 양방향 문맥을 **동시에** 반영  
- Attention으로 단어 간 관계를 더 정교하게 파악  

### 모델 크기
- BERT Base  
- BERT Large  

---

## 2.2 BERT 모델 구조

### 인코더 구조
- 12-layer encoder  
- hidden size = 768  
- 12 attention heads  
- 최종 layer 위에 classifier layer 추가해 downstream task 수행  

### 입력 구성요소

#### [CLS] 토큰
- 문장 첫 토큰  
- 마지막 encoder output을 가지고 classification 수행  

#### [SEP] 토큰
- 문장 구분용  
- QA, NLI에서 문장 A와 B를 나누는 기준  

#### Segment Embedding
- 문장 A / 문장 B 구분 정보  

#### Position Embedding
- Transformer는 순서를 직접 처리하지 않기 때문에  
- 위치 정보를 embedding으로 학습  

---

## 2.3 BERT 학습 방법

### Pre-training = MLM + NSP

---

### 1) Masked Language Model (MLM)
- 입력 토큰 15%를 선택  
- 80% → [MASK]로 변경  
- 10% → 랜덤 단어로 변경  
- 10% → 그대로 둠  
- 마스킹된 단어를 맞추는 방식  

→ 주변 단어 기반으로 단어 의미 학습  
→ 양방향 문맥 반영 가능  

단, 직접적으로 정답 단어를 참조 못하도록 구조 설계 필요  

---

### 2) Next Sentence Prediction (NSP)
- 두 문장이 실제 연속인지 예측  
- 50%: 실제 이어지는 문장  
- 50%: 랜덤 문장  

→ 문장 간 관계 이해(QA, NLI에 매우 중요)  

---

# 2.4 Downstream Tasks

### 1) Single Sentence Classification
예: 감성 분석  
- [CLS] 벡터 → classifier  

### 2) Sentence Pair Classification
예: NLI, Paraphrase  
- [CLS] → 관계 예측  

### 3) Question Answering
예: SQuAD  
- Start/End token 위치를 예측  

### 4) Single Sentence Tagging
예: NER, POS  
- 각 토큰 hidden vector → classifier  

### BERT를 임베딩만 사용하는 방법
- Feature Extraction 방식  
- BERT의 contextual embedding을 다른 모델 입력으로 활용  

---

# 3. Tokenizer 이해하기

## 3.1 Tokenizer 개념

Tokenization
- 문장을 토큰(subword) 단위로 분해  
- 각 토큰을 vocabulary ID에 매핑  
- tokenizer 품질이 pre-training 품질에 큰 영향  

### Subword Tokenizer 개념
- 단어를 더 작은 단위로 분리  
- 희귀 단어, 신조어에도 강함  
- 단어 의미 유추 가능  

---

## 3.2 Byte Pair Encoding (BPE)

- 가장 많이 등장하는 문자 쌍을 병합  
- bottom-up 방식  
- subword 단위 vocabulary 구성  

---

## 3.3 WordPiece (BERT Tokenizer)

- BERT에서 사용  
- 코퍼스의 likelihood를 최대로 하는 쌍을 병합  
- 가장 자주 등장하는 문자열을 우선적으로 병합  
- Language-specific 환경에 맞게 최적화
