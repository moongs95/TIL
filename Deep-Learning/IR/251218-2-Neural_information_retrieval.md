# 신경망 기반 정보 추출

## 1. Vector Similarity (벡터 유사도)

### 1.1 임베딩 방식의 진화 과정

#### 임베딩 개념

**정의**:
- **단어나 문장을 고차원 벡터로 표현**

**특징**:
- 산술 연산이 가능
- 단어나 문장 사이의 유사도 측정에 활용

**참고**:
```
반대 의미를 갖는 단어의 경우:
- 오히려 1(유사)과 가까워짐
- 무관할 때만 0
```

---

#### Word2Vec

**특징**:
- **학습 기반 방식 중 초기 성공 모델**
- 동시에 등장하는 단어들을 벡터 공간에서 가깝게 위치하도록 학습

**방법**:
- **CBOW (Continuous Bag of Words)**: 주변 단어로 중심 단어 예측
- **Skip-gram**: 중심 단어로 주변 단어 예측

---

#### Word2Vec - Extensions

**Word2Vec의 성공 이후 다양 영역으로 확장**

**1. Doc2Vec**
```
목적: 다양한 길이의 텍스트를 벡터로 표현
범위: 문장, 문단, 전체 문서
방법: Word2Vec에 문서 ID를 추가적인 context로 넣어줌
```

**2. Top2Vec**
```
목적: 특정 토픽에 대한 임베딩 획득
방법:
1. Doc2Vec으로 임베딩 생성
2. 낮은 차원으로 축소
3. Clustering 수행
4. Cluster의 중심을 토픽 벡터로 사용
```

**3. BioVectors**
```
목적: 생물학 분야 적용
방법: Word2Vec의 n-gram을 단백질, DNA 등 biological sequence에 적용
종류: BioVec, ProtVec, GeneVec 등
```

---

#### Context에 대한 고려

**개념**:
- 특정 단어나 문서의 고정된 vector representation이 아님
- **주변 맥락에 따라 최적화된 임베딩 생성 가능**

---

#### Context 고려한 임베딩 모델

**1. ELMo (Embeddings from Language Models)**
```
특징:
- 컨텍스트를 고려한 최초의 임베딩 생성 방식
- LSTM 기반
```

**2. ULMFiT (Universal Language Model Fine-tuning)**
```
특징:
- 컨텍스트 기반 임베딩
- Pre-training, Fine-tuning 개념 정립
- 다양한 downstream task에 pre-trained 모델을 활용할 수 있는 기반 마련
```

**3. OpenAI Transformer (GPT)**
```
특징:
- Transformer decoder만 사용
- 다음 나올 토큰을 예측하는 language model의 자연스러움을 그대로 활용
```

**4. BERT (Bidirectional Encoder Representations from Transformers)**
```
특징:
- Transformer decoder 대신 encoder 사용
- 높은 성능으로 embedding, pre-training의 대표적인 모델로 활용
```

---

#### 임베딩 방식 진화 과정
```
Word2Vec (고정 벡터)
  ↓
Doc2Vec, Top2Vec (문서/토픽 확장)
  ↓
ELMo (Context 고려, LSTM)
  ↓
ULMFiT (Pre-training 개념)
  ↓
GPT (Transformer Decoder)
  ↓
BERT (Transformer Encoder)
```

---

### 1.2 Pre-trained 모델 활용

#### BERT 활용

**특징**:
- **임베딩 생성뿐만 아니라 다양한 NLP task에 활용**

**활용 Task**:
1. **두 문장 관계**: 문장 간 관계 파악
2. **한 문장 분류**: 감성 분류 등
3. **QA (Question Answering)**: Paragraph 정보로 span 추출해서 답변
4. **NER (Named Entity Recognition)**: 개체명 인식

---

## 2. IR을 위한 임베딩 활용

### 2.1 Pre-trained BERT 모델 활용

#### 기본 사용 방법

**방법**:
- BERT 모델을 통해 나오는 **[CLS] 토큰의 임베딩**
- 또는 **개별 토큰들의 출력 임베딩에 대한 평균** 사용
- 벡터 유사도 계산에 사용

**구조**:
```
질의와 문서를 각각 모델에 입력
  ↓
임베딩을 생성
  ↓
벡터 유사도 계산
```

---

#### 문제점

**한계**:
```
질의와 문서의 벡터 공간이 둘 사이의 유사도 기준으로 학습되지 않았기 때문에
성능의 한계가 있음
```

---

#### 개선 방법: Fine-tuning

**질의-문서 Pair 데이터로 BERT를 Fine-tuning**

**방법**:
1. 질의와 문서의 관련도 점수를 구하기 위해
2. BERT의 입력으로 질의 단어들과 문서의 단어들을 넣어줌
3. 예: `[[CLS], q, [SEP], d, [SEP]]`
4. **[CLS] 토큰의 임베딩을 활용하여 점수 산출**

**효과**:
- **유사도 성능을 높일 수 있음**

---

### 2.2 기본 모델의 한계

#### BERT 기본 모델을 IR에 적용하기에는 현실적인 한계

**1. 학습 데이터 구축의 어려움**
```
❌ 품질 좋은 학습 데이터를 대량으로 구축하려면 많은 비용이 필요
```

**2. 느린 속도**
```
❌ 유사도 계산을 위한 속도가 느림
❌ Inference 시간과 비용이 너무 큼
❌ 문서 수가 수천 이상인 경우는 사용하기 힘듦
```

**3. 실제 서비스 활용 제한**
```
❌ 실제 서비스에서 활용되는 경우는 거의 없음
```

---

#### 용어 정리

**Cross-Encoder**:
```
정의: 하나의 모델에 질의-문서 pair를 입력으로 score를 출력하는 모델
```

**Bi-Encoder**:
```
정의: 질의와 문서를 각각 다른 모델에 입력
예시: DPR, SentenceBERT 등
특징: 실제 서비스에서 더 효율적인 알고리즘
```

---

## 3. Query-Document 매칭 알고리즘

### 3.1 Cross-Encoder 모델

#### 구조

**개념**:
- **하나의 모델에 query-document 쌍 입력**

**기본 구조**:
1. BERT 기본 모델을 그대로 활용
2. **두 개의 문장을 모델 입력**으로 사용하여 fine-tuning
3. 문장 간의 관계에 대한 정보를 담은 **[CLS] 토큰 임베딩**
4. 또는 **각 토큰 임베딩의 평균값 등을 활용**
5. **유사도가 계산**되도록 하는 방식

---

#### IR을 위한 적용

**방법**:
```
1. Query-Document pair를 하나의 스트림으로 BERT에 입력
   - Examples: <qi, doc+, {doc-}>

2. 학습 목표:
   - Positive pair 간의 score는 높아지도록
   - Negative pair 간의 score는 낮아지도록

3. 각 pair의 [CLS] token의 임베딩을 가져와
   MLP를 통해 relevance score를 계산
```

---

#### 특징: 성능과 속도의 Trade-off

**장점: 높은 성능**
```
✅ 학습 데이터만 충분하다면 성능은 최대로 높일 수 있음
```

**단점: 느린 속도**
```
❌ 질의가 들어올 때마다 문서 수만큼의 모델 inference가 필요
❌ Response time은 문서 수에 linear하게 증가
❌ 연산 비용과 속도 때문에 현실적으로 적용하기 힘듦
```

---

### 3.2 Bi-Encoder 모델

#### 구조

**개념**:
- **Query와 document를 각각 다른 모델에 입력**

**특징**:
1. 기본 BERT 모델을 사용
2. 질의와 문서를 인코딩하기 위한 **각각의 모델을 fine-tuning**하는 구조
3. Fine-tuning 단계에서 질의와 문서 토큰 사이의 직접적인 연결은 없음
4. **최종 score만으로 각 모델이 업데이트됨**

**구현**:
```
Bi-encoder는 논리적으로는 각각의 모델이지만
실제로는 하나의 물리적인 모델이 되게 할 수도 있음
```

---

#### 특징: 성능과 속도의 Trade-off

**장점: 빠른 속도**
```
✅ 문서 임베딩을 미리 계산해 둘 수 있음
✅ 검색 요청 시 질의에 대한 임베딩만 계산
✅ 이후는 cosine similarity 계산을 통해 점수화
✅ Cross-encoder에 비해 매우 빠른 속도
```

**단점: 낮은 성능**
```
⚠️ Cross-encoder보다는 성능이 낮음

하지만:
✅ 학습이 잘 된 경우 sparse retrieval보다 대체로 성능이 높음
✅ 연산 비용과 속도 고려하여 현실적으로 적용 가능
```

---

#### DPR (Dense Passage Retrieval)

**정의**:
- **대표적인 Bi-Encoder 모델**

**구조**:
```
1. Query-Document pair를 각각 독립적 파라미터를 가지는 BERT에 입력
   - Examples: <qi, doc+, {doc-}>

2. Query와 document 입력의 [CLS] token의 임베딩을 가져와
   임베딩 간의 유사도 계산

3. 학습:
   - Positive pair 간의 score는 높아지도록
   - Negative pair 간의 score는 낮아지도록
   - 두 모델을 동시에 학습
```

---

## 4. 상용 벡터 인코더

### 4.1 Sentence Transformers

#### Sentence-BERT 모델

**정의**:
- **Sentence Embeddings using Siamese BERT-Network**

**구조**:
- Siamese BERT-Network을 활용하여 모델 학습
- **두 개의 BERT network을 사용하지만 weight는 공유**
- Pre-trained BERT 모델을 활용

---

#### 학습 방법

**Fine-tuning**:
- 기존 BERT(BERT/RoBERTa)를 **유사도 기반 loss functions을 활용**해 fine-tuning 수행

**Objective Functions**:
1. **Classification objective function**: 분류 목적 함수
2. **Regression objective function**: 회귀 목적 함수
3. **Triplet objective function**: 삼중 목적 함수

**임베딩 방법**:
- **[CLS] 토큰의 임베딩**
- **전체 토큰 임베딩의 평균**
- 두 가지 방식 모두 실험

---

#### 학습 데이터

**데이터셋**:
1. **SNLI**: 두 문장 간의 관계를 추론 (함의/모순/중립), 570,000 문장
2. **MultiNLI**: 430,000 문장

**특징**:
- 소규모 데이터셋

---

#### 성능

**강점**:
- 기존 모델들보다 **문장 간의 비교가 필요한** task에서 더 좋은 성능
- **NER (Named Entity Recognition)**
- **STS (Semantic Textual Similarity)**

---

#### 사용 방법

**Python Framework 제공**:
```python
# 설치
pip install -U sentence-transformers

# 사용
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# Our sentences we like to encode
sentences = ["This is an example sentence", "Each sentence is converted"]

# Sentences are encoded by calling model.encode()
embeddings = model.encode(sentences)
```

---

#### Hugging Face 통합

**특징**:
- Hugging Face를 통해 학습된 모델을 공유하고 다운로드 받을 수 있음
- **이미 500개 이상의 학습된 모델이 공유**되고 있음
- **100개 이상의 언어에 대해 임베딩 생성 가능**

**활용**:
- 공유된 모델을 그대로 사용
- 또는 pre-trained 모델로 사용하여 도메인에 적합하게 fine-tuning

---

### 4.2 OpenAI Embeddings

#### 인코딩 모델

**Text and Code Embeddings by Contrastive Pre-Training**

**학습 방법**:
1. **Unsupervised Contrastive Learning**을 활용해 Transformer encoder를 학습
2. 짝지어진 문장들로 구성된 배치를 만듦
3. 짝지어진 문장 간의 유사도는 높게
4. 그렇지 않은 문장 간의 유사도는 낮아지도록 학습
5. **웹상의 대규모 데이터를 활용** - 연속되는 문장을 positive pair로 사용

---

#### OpenAI Embedding Model

**특징**:
- Sentence-BERT와 유사한 형태의 **Bi-Encoder 구조**
- **모델 크기를 늘리고 데이터의 양을 더 늘림**
- 기존 모델들보다 **더 좋은 성능의 모델**을 얻음

---

#### 사용 방법

**Client 제공**:
- Python, Node.js Client
- HTTPS Request로 사용 가능
```python
# 설치
pip install openai

# 사용
from openai import OpenAI

client = OpenAI(
    organization="YOUR_ORG_ID",
)

# 임베딩 생성
client.embeddings.create(
    model="text-embedding-ada-002",
    input="The food was delicious and the waiter...",
    encoding_format="float"
)
```

---

#### OpenAI 임베딩 특징

**1. API 형태로만 사용 가능**
```
⚠️ 결과 생성을 위해 네트워크 통신 필요
❌ 인코더 모델을 다운로드 받거나 fine-tuning 할 수는 없음
```

**2. Vector dimension이 큰 편**
```
- Vector의 dimension: 1536
⚠️ 속도가 상대적으로 느림
✅ 대신 긴 입력 처리에 유리 (8K까지 가능)
```

**3. 다국어 지원**
```
✅ 다국어 지원
⚠️ 하지만 영어에 최적화된 성능
```

**4. 유료 서비스**
```
💰 유료로 사용할 수 있음
```

---

## 전체 요약

### 임베딩 발전 과정
```
Word2Vec (2013)
  ↓ 고정 벡터, Context 미고려
Doc2Vec, Top2Vec
  ↓ 문서/토픽 확장
ELMo (2018)
  ↓ Context 고려 시작
ULMFiT (2018)
  ↓ Pre-training 개념
GPT (2018)
  ↓ Transformer Decoder
BERT (2019)
  ↓ Transformer Encoder, 양방향
Sentence-BERT (2019)
  ↓ 효율적인 문장 임베딩
OpenAI Embeddings (2022+)
  ↓ 대규모 데이터, 높은 성능
```

---

### Cross-Encoder vs Bi-Encoder

| 구분 | Cross-Encoder | Bi-Encoder |
|------|---------------|------------|
| **입력** | Query-Doc Pair (하나의 모델) | Query, Doc 각각 |
| **성능** | ✅ 높음 | ⚠️ 상대적으로 낮음 |
| **속도** | ❌ 느림 (문서 수에 비례) | ✅ 빠름 (사전 계산 가능) |
| **실용성** | ❌ 현실적으로 어려움 | ✅ 현실적으로 가능 |
| **활용** | Re-ranking | 초기 검색 |

---

### 상용 임베딩 모델 비교

| 특징 | Sentence-BERT | OpenAI Embeddings |
|------|---------------|-------------------|
| **구조** | Siamese BERT | Contrastive Learning |
| **데이터** | SNLI, MultiNLI (~1M) | 웹 데이터 (대규모) |
| **사용** | 로컬 모델 | API 전용 |
| **Fine-tuning** | ✅ 가능 | ❌ 불가 |
| **언어** | 100개 이상 | 다국어 (영어 최적) |
| **비용** | 무료 (오픈소스) | 유료 |
| **Dimension** | 모델에 따라 다름 | 1536 (고정) |
| **최대 입력** | 모델에 따라 다름 | 8K 토큰 |

---

### IR 시스템 구성

**Two-Stage Retrieval**:
```
1. First Stage (Retrieval):
   - Bi-Encoder (DPR, Sentence-BERT)
   - 빠른 속도로 후보 문서 추출 (Top 100~1000)

2. Second Stage (Re-ranking):
   - Cross-Encoder
   - 정확한 순위 재조정 (Top 10~100)
```

---

### 임베딩 활용 방법

**1. Pre-computed Embeddings (Bi-Encoder)**
```
오프라인:
1. 모든 문서를 임베딩으로 변환
2. Vector DB에 저장

온라인:
1. 질의를 임베딩으로 변환
2. Vector DB에서 유사도 계산
3. Top-k 반환
```

**2. On-the-fly Computation (Cross-Encoder)**
```
온라인:
1. 질의-문서 pair를 모델에 입력
2. 관련도 점수 계산
3. 순위 매김
```

---

## 실전 활용 가이드

### 시나리오별 선택

**소규모 문서 (< 10,000개)**:
```
→ Cross-Encoder 단독 사용 가능
```

**중규모 문서 (10,000 ~ 1,000,000개)**:
```
→ Bi-Encoder (1st stage) + Cross-Encoder (2nd stage)
```

**대규모 문서 (> 1,000,000개)**:
```
→ Sparse Retrieval (BM25) → Bi-Encoder → Cross-Encoder
   (3단계 구성)
```

---

### 모델 선택 가이드

**오픈소스 선호 + Fine-tuning 필요**:
```
→ Sentence-BERT
✅ 무료
✅ Fine-tuning 가능
✅ 로컬 실행
```

**최고 성능 필요 + 예산 있음**:
```
→ OpenAI Embeddings
✅ 높은 성능
✅ 긴 입력 처리
⚠️ 유료
❌ Fine-tuning 불가
```

**한국어 특화**:
```
→ 한국어 Sentence-BERT 모델
   (예: jhgan/ko-sroberta-multitask)
```

---

### 성능 최적화 팁

**1. Negative Sampling**
```
- Hard negative 사용
- In-batch negative 활용
```

**2. Data Augmentation**
```
- Paraphrasing
- Back-translation
```

**3. Loss Function 선택**
```
- Contrastive Loss
- Triplet Loss
- MultipleNegativesRankingLoss
```

**4. Hyperparameter Tuning**
```
- Learning rate
- Batch size
- Negative samples 수
```

---

## 주요 개념 정리

### Embedding
```
정의: 텍스트를 고차원 벡터로 표현
목적: 유사도 계산, 산술 연산
방법: Word2Vec → BERT → Sentence-BERT
```

### Cross-Encoder
```
정의: Query-Doc pair를 하나의 모델에 입력
장점: 높은 성능
단점: 느린 속도
용도: Re-ranking
```

### Bi-Encoder
```
정의: Query와 Doc을 각각 인코딩
장점: 빠른 속도 (사전 계산)
단점: 상대적으로 낮은 성능
용도: 초기 검색
```

### Contrastive Learning
```
정의: Positive pair는 가깝게, Negative pair는 멀게
방법: Loss function으로 학습
활용: Sentence-BERT, OpenAI Embeddings
```

### Siamese Network
```
정의: 같은 weight를 공유하는 두 개의 네트워크
목적: 두 입력의 유사도 계산
활용: Sentence-BERT
```

---

## 트렌드 및 미래 방향

### 현재 트렌드
```
1. Large-scale Pre-training
2. Contrastive Learning
3. Two-stage Retrieval
4. Hybrid Search (Sparse + Dense)
```

### 미래 방향
```
1. 더 큰 모델, 더 많은 데이터
2. Multi-lingual, Multi-modal
3. 효율적인 Fine-tuning (LoRA 등)
4. Domain-specific Embeddings
```

---

## 핵심 Takeaway
```
📊 임베딩: 텍스트를 벡터로 표현

🔄 발전: Word2Vec → BERT → Sentence-BERT

🎯 Cross-Encoder: 높은 성능, 느린 속도

⚡ Bi-Encoder: 빠른 속도, 실용적

📈 Two-Stage: Bi-Encoder (검색) + Cross-Encoder (재순위)

🤗 Sentence-BERT: 오픈소스, Fine-tuning 가능

🔐 OpenAI: API 전용, 높은 성능, 유료

💡 실전: 시나리오에 맞는 모델 선택 중요

🚀 미래: 더 크고, 빠르고, 효율적인 모델
```
