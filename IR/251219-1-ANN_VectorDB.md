# Embedding 생성과 ANN

## 1. Approximate Nearest Neighbor (ANN) 알고리즘

### 1.1 ANN 기본 개념

#### Nearest Neighbor (NN)

**정의**:
- **벡터 공간 모델**에서 원하는 쿼리 벡터와 **가장 유사한 벡터**를 찾는 알고리즘

**Brute Force KNN**:
- 가장 기본적인 NN 형태
- **모든 벡터와의 유사도**를 비교하는 방식

**문제점**:
```
❌ 높은 계산 비용을 필요로 함
❌ 대규모 데이터셋에서는 실시간 서빙에 적합하지 않음
```

---

#### Approximate Nearest Neighbor (ANN)

**정의**:
- **정확도를 어느 정도 포기**하고
- 모든 벡터와 유사도를 비교하지 않고 **탐색 범위를 좁혀**
- **일부 벡터와 유사도를 비교**해
- **가장 유사한 벡터를 찾는 방법**

**필요성**:
```
✅ 대규모의 데이터셋을 다루기 위해서는 필수
```

**Trade-off**:
```
정확도 ↓
속도 ↑
```

---

## 2. 주요 ANN 알고리즘 소개

### 2.1 LSH (Locality Sensitive Hashing)

#### 개념

**정의**:
- **LSH를 사용해 여러 벡터를 하나의 버켓으로 군집화**
- 벡터 검색 범위를 줄이는 방법

**원리**:
```
유사한 벡터들을 같은 해시 버킷에 매핑
→ 검색 시 해당 버킷 내에서만 탐색
```

---

#### 주요 특징

**사용성**:
```
✅ 다양한 유형의 데이터와 유사도 측정에 적용 가능
✅ 여러 분야에서 유용하게 활용
⚠️ 비교적 적은 데이터 규모에 적합
```

**메모리 효율**:
```
❌ 모든 데이터를 메모리에 해시테이블로 가지고 있어야 함
❌ 메모리 사용량이 많음
❌ 성능을 높이기 위해서는 여러 해시테이블 필요
```

**속도**:
```
✅ 신규 데이터에 대한 색인 속도가 매우 빠름
⚠️ 파라미터 설정에 따라 속도 편차가 큼
```

---

### 2.2 Tree/Space Partitioning

#### ANNOY (Approximate Nearest Neighbor Oh Yeah)

**작동 방식**:

**Record (색인)**:
```
1. Select two points randomly (두 점을 무작위로 선택)
2. Divide up the space (공간을 나눔)
3. Repeat hierarchically (계층적으로 반복)
```

**Search (검색)**:
```
1. Focus the cell that the query lives (쿼리가 있는 셀에 집중)
2. Compare the distances (거리 비교)
3. Can traverse the tree by log-times comparisons (로그 시간 내 트리 순회)
```

**핵심**:
- 빠른 탐색을 위해 **벡터 공간**을 **여러 개의 부분 공간(subspace)**으로 나눔
- 그 정보들을 **트리에 저장**

---

#### 주요 특징

**사용성**:
```
✅ 대규모 데이터에 사용할 수 있음
✅ 잘 관리되고 안정적 (Spotify에서 개발)
⚠️ 트리 구조에 따라 검색 결과의 일관성이 떨어질 수 있음
```

**메모리 효율**:
```
✅ 트리 구조로 효율적인 데이터 저장이 이루어짐
```

**속도**:
```
✅ 신규 데이터에 대한 색인 속도는 준수한 편
❌ 질의 처리 속도가 다른 알고리즘에 비해 느림
```

---

### 2.3 Graph-based Methods

#### NSW (Navigable Small World Graphs)

**개념**:
- 문서 데이터를 그래프로 나타냄
- 쿼리 데이터에 대해 **graph-traversal**을 통해
- **가장 가까운 노드를 찾는 방법**

**작동 방식**:
```
Given a query vector:
1. Start from a random point (랜덤 포인트에서 시작)
2. From the connected nodes, find the closest one to the query
   (연결된 노드 중 쿼리에 가장 가까운 것 찾기)
3. Traverse in a greedy manner (탐욕적으로 순회)
```

---

#### HNSW (Hierarchical NSW)

**개념**:
- **엣지의 길이별로 계층**을 나눔
- **엣지가 가장 긴 계층**부터 **그래프 탐색**을 **시작**
- 검색 복잡도를 줄이는 방법

**계층 구조**:
```
Layer 2 (최상위): 가장 긴 edge
  ↓
Layer 1 (중간): 중간 길이 edge
  ↓
Layer 0 (최하위): 짧은 길이 edge
```

---

#### 주요 특성

**사용성**:
```
✅ 대규모 데이터에 적합한 방법
✅ 데이터가 커질수록 성능상의 이점이 부각됨
✅ FAISS 등 다양한 라이브러리에 구현되어 있음
```

**메모리 효율**:
```
❌ 그래프를 구축해서 가지고 있어야 하기 때문에 메모리 사용량이 많음
```

**속도**:
```
❌ 데이터가 많을 때 새로운 노드를 그래프에 추가하는 작업이 느림
✅ 질의 처리 속도는 ANN 알고리즘 중 가장 빠름
```

---

### 2.4 Inverted File Index (IVF)

#### 개념

**정의**:
- **고차원 데이터를 클러스터**로 나눔
- 이 과정에서 **각 데이터 포인트는 가장 가까운 클러스터로 할당**

**클러스터링 방법**:
- **K-means 알고리즘**
- **벡터 양자화 (Vector Quantization)**

---

#### 작동 방식

**클러스터 생성**:
```
1. 각 중심점에서 모든 점들이 각 클러스터에 포함될 때까지
2. 동일한 길이로 각 클러스터의 반지름을 확장
3. 각 클러스터는 역색인(Inverted) 파일 구조를 사용하여 색인
```

---

#### 문제점 및 해결책

**문제점**:
```
❌ 각 클러스터의 경계를 엣지(edge)라고 하는데
❌ 쿼리 벡터가 경계 주변에 위치하게 되면 부정확한 검색 결과를 얻을 수 있음
```

**해결책**:
```
✅ 하나의 쿼리에 대해
✅ 쿼리를 포함하지 않는 여러 클러스터들에 대한 검색도 함께 수행
✅ 검색 정확도를 높일 수 있음
```

---

#### 주요 특성

**사용성**:
```
✅ 대규모 데이터셋을 효율적으로 처리할 수 있는 구조로 확장성이 뛰어남
⚠️ 데이터 분포에 따라 성능이 달라질 수 있음
✅ FAISS 등 다양한 라이브러리에 구현되어 있음
```

**메모리 효율**:
```
✅ 상대적으로 적은 메모리 사용
```

**속도**:
```
❌ 클러스터링 과정의 오버헤드로 색인 시간이 오래 걸림
✅ 다양한 파라미터 조정을 통해 검색의 정확도와 속도 사이의 균형을 잡을 수 있음
```

---

### 2.5 ANN 알고리즘 특성 비교

#### 성능 측정 결과

**테스트 환경**:
- 128차원의 100만 개의 데이터
- 10개의 검색 결과를 얻을 때의 결과
- FLAT은 문서 전체와 비교하는 NN (기준)

| Index | Memory (MB) | Query Time (ms) | Recall | Notes |
|-------|-------------|-----------------|--------|-------|
| **Flat (L2 or IP)** | ~500 | ~18 | 1.0 | 작은 데이터셋 또는 쿼리 시간이 중요하지 않을 때 적합 |
| **LSH** | 20-600 | 1.7-30 | 0.4-0.85 | 저차원 데이터 또는 작은 데이터셋에 최적 |
| **HNSW** | 600-1600 | 0.6-2.1 | 0.5-0.95 | 높은 품질, 빠른 속도, 하지만 메모리 사용량 큼 |
| **IVF** | ~520 | 1-9 | 0.7-0.95 | 확장 가능한 옵션, 높은 품질, 합리적인 속도와 메모리 |

---

#### 인덱싱 속도

**순위**:
```
가장 빠름: LSH
↓
IVF
↓
HNSW
↓
가장 느림: Graph 방법
```

---

#### 질의 처리 속도

**순위**:
```
가장 빠름: Graph 기반 ANN (HNSW)
↓
IVF
↓
LSH
↓
가장 느림: Tree 기반 ANN (ANNOY)
```

---

#### 선택 가이드

**결론**:
```
알고리즘별로 장단점이 있기 때문에
사용 데이터의 크기, 차원 등의 상황을 고려해서 선택해야 함
```

---

## 3. 상용 Vector DB 비교/분석

### 3.1 Vector DB 개요

#### Vector DB 특징

**정의**:
- **대규모 고차원의 데이터에 대한 효율적인 처리 기능을 가진 특화 DB**

---

#### 주요 기능

**1. 유사도 기반 검색**
```
- 고차원 벡터에 대한 빠른 벡터 유사도 계산 기능을 수행
- 실시간 처리를 위한 효율적인 ANN 알고리즘 지원
```

**2. 효율적인 데이터 관리**
```
- 대규모 데이터에 대한 최적화된 저장 공간 관리 기능 제공
- 데이터 추가/삭제 등을 위한 수평적 확장 지원
```

---

#### 기존 검색엔진과 Vector DB와의 차이

| 구분 | 기존 검색엔진 | Vector DB |
|------|--------------|-----------|
| **기본 원리** | 키워드 매칭 기반의 검색 | 고차원 벡터 공간에서 데이터를 표현하고 **벡터 유사도 기반**으로 검색 |
| **적용 분야** | 웹 검색, 텍스트 데이터 검색 | 텍스트 데이터 검색, 이미지/음성 검색 |
| **장단점** | 빠른 색인/검색 속도, 검색 성능 한계 있음 | **높은 성능, 속도가 상대적으로 느림** |
| **상용 솔루션** | Elasticsearch, Solr, Algolia 등 | Elasticsearch, Pinecone, Faiss, Weaviate, Milvus, Vespa, Qdrant 등 다수 |

---

### 3.2 Vector DB의 작동 방식

#### 핵심

**초점**:
- **고차원 데이터**에 대한 **색인과 검색**의 **효율적인 처리**에 초점

---

#### 색인 (Indexing)

**과정**:
1. 벡터 인코더를 통해 고차원 데이터로 변환된 문서 데이터(임베딩)를 입력
   - **대체로 Vector DB에서 벡터 인코더를 직접 제공하지는 않음**
2. 다양한 ANN 알고리즘 사용하여 색인

---

#### 검색 (질의 처리)

**과정**:
1. **질의어**와 **문서의 임베딩**을 이용하여 유사도 계산
2. **유사도가 높은 문서를 순서대로 반환**
3. 유사도 계산 시 **빠른 속도**를 위해 **ANN 알고리즘 활용**
4. **메타 필드**를 사용한 **필터링 기능 제공**

---

#### 색인 및 검색 방식 다이어그램
```
입력 데이터
(Images, Documents, Audio)
  ↓
Transform into embedding
  ↓
Vector representation (Dense vectors)
  ↓
Vector DB (Nearest neighbor 알고리즘)
  ↑
Vector representation
  ↑
Transform into embedding
  ↑
Query
```

---

## 4. 대표적인 상용 Vector DB 소개

### 4.1 Elasticsearch

#### 주요 특징

**서비스 제공 형태**:
```
- Self-hosted
- Managed service
→ 모두 제공
```

**ANN 알고리즘 지원**:
```
- HNSW 지원
```

**기타 주요 특징**:
```
✅ 기존 검색엔진 기능에 추가로 Vector DB 기능 제공
✅ 잘 알려져 있고 커뮤니티 활성화되어 있음
```

---

#### Elasticsearch 사용 예시
```python
# 설정
setting = {
    "mappings": {
        "properties": {
            "embeddings": {
                "type": "dense_vector",
                "dims": 768,
                "index": True,
                "similarity": "l2_norm"
            }
        }
    }
}

# 인덱스 생성
create_es_index("test", setting)

# 문서 추가 (각 문서는 'embedding' 필드를 가짐)
ret = bulk_add("test", index_docs)

# 검색
def dense_retrieve(query, index):
    # 벡터 유사성 검색에 사용할 쿼리 임베딩 가져오기
    query_embedding = get_embedding(query)
    
    # KNN을 사용한 벡터 유사성 검색을 위한 매개변수 설정
    knn = {
        "field": "embeddings",
        "query_vector": query_embedding.tolist(),
        "k": 10,
        "num_candidates": 100
    }
    
    # 지정된 인덱스에서 벡터 유사성 검색 수행
    return es.search(index=index, knn=knn)
```

---

### 4.2 Faiss

#### 주요 특징

**서비스 제공 형태**:
```
- Library 형태로 제공
```

**ANN 알고리즘 지원**:
```
- Flat
- IVF
- HNSW
- PQ (Product Quantization)
```

**기타 주요 특징**:
```
⚠️ 메타 데이터는 다루지 않음 (임베딩에 대한 벡터 유사도만 고려)
✅ Library 형태여서 다른 솔루션의 서브모듈로 활용되기도 함
   - Milvus, ColBERT 등에서 Faiss를 벡터 저장소로 사용
```

---

#### Faiss 사용 예시
```python
import faiss
import numpy as np

# 인덱스 생성 (Flat L2)
index = faiss.IndexFlatL2(768)

# 문서 추가
index.add(np.array(index_docs_for_faiss).astype('float32'))

# 검색
query_str = "서울 맛집 추천해줘"
query_emb = get_embedding([query_str])
scores, offsets = index.search(query_emb, 5)
```

---

### 4.3 Pinecone

#### 주요 특징

**서비스 제공 형태**:
```
- Managed service 형태로 제공
```

**ANN 알고리즘 지원**:
```
- Flat
- IVF
- HNSW
- PQ
```

**기타 주요 특징**:
```
✅ 클라우드 기반 서비스로 확장성이 뛰어남
✅ Sparse vector 지원으로 키워드 검색과 하이브리드로 사용 가능
✅ 메타 데이터로 필터링 작업을 쉽게 할 수 있음
```

---

#### Pinecone 색인 저장 구조

**Pinecone Record**:
```
- Record ID: 'vector-1'
- Dense vector: [.1, .2, .3, .4, ...]
- Sparse vector:
  - Indices
  - Values: [.5, .5, .2, ...]
- Metadata:
  - Key1: Value1
  - Key2: Value2
```

---

#### Pinecone 사용 예시
```python
from pinecone import Pinecone, PodSpec

# API Key 설정 (https://app.pinecone.io에서 발급)
pc = Pinecone(api_key="Your API Key")

# 인덱스 생성
pc.create_index(
    name="quickstart",
    dimension=768,
    metric="cosine",
    spec=PodSpec(environment="gcp-starter")
)

# 인덱스 연결
index = pc.Index("quickstart")

# 문서 추가
index.upsert(index_docs_for_pinecone, namespace='ns1')

# 검색
query_str = "서울 맛집 추천"
query_emb = get_embedding([query_str]).tolist()
topk = index.query(
    namespace='ns1',
    vector=query_emb[0],
    top_k=5,
    include_metadata=True
)
```

---

## 5. ColBERT 모델 이해

### 5.1 ColBERT 모델 개요

#### 배경

**기존 모델의 문제점**:

**Cross-Encoder**:
```
✅ 성능은 좋음
❌ 속도가 너무 느림
```

**Bi-Encoder**:
```
✅ 속도가 빠름
⚠️ 성능이 다소 아쉬움
```

---

#### ColBERT의 아이디어

**핵심 아이디어**:
- 질의와 문서 각각의 임베딩을 사용하는 대신
- **질의를 구성하는 토큰**과 **문서를 구성하는 토큰의 임베딩을 모두 사용해서 유사도 계산**
- **Late Interaction**

**Trade-off**:
```
연산량:
- Cross-encoder에 비해서는 훨씬 적음
- Bi-encoder에 비해서는 많음

이유:
- 질의를 구성하는 토큰과 문서를 구성하는 토큰 수의
  곱만큼의 cosine similarity 연산 필요
```

**최적화**:
```
✅ 벡터 차원 축소 기법을 적용하여 연산 및 저장 공간 비용 최적화
✅ 활용하는 임베딩의 수가 많아지는 만큼 차원 축소에 대한 성능 하락폭이 크지 않음
```

---

#### Poly-encoder

**유사한 시도**:
- 질의를 위한 Encoder의 Attention Layer를 추가 학습
- **질의**에 대해서는 더 풍부한 토큰 임베딩을 활용하는 방식

---

### 5.2 ColBERT 모델 구조

#### Late Interaction

**특징**:
1. 질의와 문서의 임베딩을 독립적으로 생성
2. 문서에 대해서는 Bi-Encoder처럼 **미리 임베딩을 생성**해 둘 수 있음
3. 모든 토큰들을 벡터 유사도 계산에 활용

---

#### ColBERT 유사도 계산 방식

**과정**:
1. Query-Document pair를 각각 **같은 파라미터**를 가지는 **BERT에 입력**
2. Query와 document 문장 레벨의 임베딩이 아니라 **토큰 레벨의 임베딩**을 가져옴
3. **MaxSim을 계산** (Late Interaction)
4. **Query 토큰별 MaxSim**을 **모두 합하여 최종 점수 계산**

---

#### Token Level Soft Interaction

**특징**:
- **Sparse vector의 TF-IDF 기반 score 계산과 유사한 형태**

**차이점**:
```
TF-IDF:
- Exact matching
- 맥락 정보 없음

ColBERT:
✅ 맥락 정보가 반영된 BERT의 토큰 임베딩을 사용
✅ Exact 매칭이 아니라 유사어 또는 연관된 토큰인 경우 최종 점수 결과에 반영됨
```

---

### 5.3 ColBERT 모델 학습

#### 학습 데이터 구조

**Triple 구조**:
```
<query, positive_document, negative_document>

- query: 문서 추출을 위해 사용할 질의
- positive_document: 질의에 적합한 문서
- negative_document: 질의에 적합하지 않은 문서
```

**Loss Function**:
- Positive와 negative 문서의 점수에 대해 **softmax cross-entropy loss** 적용

---

#### Weak-supervision을 통한 학습 데이터 생성

**개념**:
- **Iterative 방식**으로 학습 데이터의 품질을 높이면서 모델 성능을 개선하는 방식

**이유**:
```
처음부터 고품질의 학습 데이터를 대량으로 구축하는 것은 큰 비용이 듦
```

**과정**:
```
1. 낮은 성능의 모델로 후보군을 추출
2. Annotation 후 모델 학습
3. 개선된 성능의 모델로 반복적으로 동일한 작업 진행
```

---

#### LLM을 활용한 학습 데이터 생성

**개념**:
- LLM의 언어 이해 및 추론 능력을 활용
- **가상의 고품질 학습 데이터 생성**

**장점**:
```
✅ Prompt 엔지니어링을 통해 원하는 형태의 학습 데이터를 저비용으로 구축할 수 있음
```

**Prompt 예시**:
```python
"""
## Role
가상 데이터 생성기

## Instructions
- 주어진 레퍼런스 정보를 보고 이 정보가 도움이 될만한 질문을 가상으로 3개 생성해줘.
- 아래 JSON 포맷으로 생성해줘.

## Output format
{"question": [$question1, $question2, $question3]}
"""
```

---

## 전체 요약

### ANN 알고리즘 비교

| 알고리즘 | 메모리 | 인덱싱 속도 | 검색 속도 | Recall | 적합한 경우 |
|----------|--------|------------|----------|--------|------------|
| **LSH** | 많음 | ⚡ 매우 빠름 | 보통 | 낮음 | 저차원, 소규모 |
| **ANNOY** | 효율적 | 보통 | ❌ 느림 | 보통 | 안정성 중요 |
| **HNSW** | 많음 | ❌ 느림 | ⚡ 가장 빠름 | 높음 | 대규모, 고품질 |
| **IVF** | 적음 | 느림 | 빠름 | 높음 | 균형잡힌 선택 |

---

### Vector DB 비교

| DB | 형태 | ANN 지원 | 특징 | 적합한 경우 |
|----|------|---------|------|------------|
| **Elasticsearch** | Self-hosted / Managed | HNSW | 검색엔진 + Vector DB | 기존 ES 사용자 |
| **Faiss** | Library | Flat, IVF, HNSW, PQ | 메타데이터 미지원 | 서브모듈로 활용 |
| **Pinecone** | Managed | Flat, IVF, HNSW, PQ | Sparse vector 지원 | 클라우드 우선 |

---

### 검색 모델 비교

| 모델 | 구조 | 성능 | 속도 | 사전 계산 | 활용 |
|------|------|------|------|----------|------|
| **Cross-Encoder** | Query-Doc Pair | ⚡ 최고 | ❌ 매우 느림 | 불가 | Re-ranking |
| **Bi-Encoder** | 독립 인코딩 | 보통 | ⚡ 빠름 | 가능 | 초기 검색 |
| **ColBERT** | Token-level | 높음 | 보통 | 가능 | 균형잡힌 선택 |

---

### ColBERT의 장점
```
성능:
✅ Cross-Encoder보다는 낮지만 Bi-Encoder보다 높음

속도:
✅ Cross-Encoder보다는 빠르지만 Bi-Encoder보다 느림

유연성:
✅ 문서 임베딩 사전 계산 가능
✅ Token-level soft matching
✅ TF-IDF와 유사하지만 맥락 정보 반영
```

---

## 실전 활용 가이드

### ANN 알고리즘 선택

**소규모 데이터 (< 10,000)**:
```
→ LSH 또는 Flat
```

**중규모 데이터 (10,000 ~ 1,000,000)**:
```
→ IVF 또는 ANNOY
```

**대규모 데이터 (> 1,000,000)**:
```
→ HNSW (메모리 충분)
→ IVF (메모리 제한)
```

**속도 최우선**:
```
→ HNSW
```

**메모리 제한**:
```
→ IVF
```

---

### Vector DB 선택

**기존 Elasticsearch 사용**:
```
→ Elasticsearch Vector DB 기능 활용
```

**클라우드 우선, 관리 최소화**:
```
→ Pinecone
```

**커스터마이징 필요, 오픈소스**:
```
→ Faiss (+ 다른 DB 조합)
```

**하이브리드 검색 (키워드 + 벡터)**:
```
→ Elasticsearch 또는 Pinecone
```

---

### 검색 시스템 구성

**3-Stage Retrieval**:
```
1. First Stage (Sparse):
   - BM25 등
   - 빠른 후보 추출 (Top 10,000)

2. Second Stage (Dense):
   - Bi-Encoder 또는 ColBERT
   - 의미 기반 검색 (Top 100)

3. Third Stage (Re-ranking):
   - Cross-Encoder
   - 정밀 순위 (Top 10)
```

---

## 주요 개념 정리

### ANN (Approximate Nearest Neighbor)
```
정의: 근사 최근접 이웃
목적: 정확도를 약간 포기하고 속도 향상
필요성: 대규모 데이터 실시간 처리
```

### HNSW (Hierarchical Navigable Small World)
```
정의: 계층적 탐색 가능한 작은 세상 그래프
특징: 가장 빠른 검색 속도
단점: 메모리 사용량 많음
```

### IVF (Inverted File Index)
```
정의: 역파일 인덱스
방법: 클러스터링 기반
특징: 균형잡힌 성능
```

### Late Interaction
```
정의: ColBERT의 핵심 아이디어
방법: Token-level 유사도 계산
효과: Cross와 Bi의 중간 성능
```

### Vector DB
```
정의: 벡터 데이터 특화 데이터베이스
기능: ANN 알고리즘, 유사도 검색
활용: 의미 기반 검색, 추천 시스템
```

---

## 트렌드 및 미래 방향

### 현재 트렌드
```
1. HNSW가 표준
2. Hybrid Search (Sparse + Dense)
3. ColBERT와 같은 Token-level 방법
4. Managed Vector DB 서비스 증가
```

### 미래 방향
```
1. 더 효율적인 ANN 알고리즘
2. 하드웨어 가속 (GPU, TPU)
3. 멀티모달 벡터 검색
4. 실시간 업데이트 최적화
```

---

## 핵심 Takeaway
```
🎯 ANN: 대규모 데이터 필수 기술

⚡ HNSW: 가장 빠른 검색 속도

💾 IVF: 균형잡힌 선택

🗄️ Vector DB: ANN + 데이터 관리

🔍 ColBERT: Token-level Late Interaction

🎨 Trade-off: 정확도 vs 속도

📊 선택: 데이터 크기, 메모리, 속도 요구사항 고려

🔄 하이브리드: Sparse + Dense가 최선

🚀 미래: 더 빠르고 효율적인 알고리즘
```
