# 상용 검색엔진 분석 (Elasticsearch)

## 1. Elasticsearch 기본 개념

### 1.1 Elasticsearch 주요 특징

#### 정의

**Elasticsearch**:
- **실시간으로 대규모 데이터셋을 분석하고 검색할 수 있는 분산형 검색 및 분석 엔진**

---

#### 주요 특징

**1. 분산형 아키텍처 (Distributed Architecture)**

**데이터 분산**:
```
- 데이터를 자동으로 여러 노드에 분산하여 저장
- 높은 가용성(High Availability) 보장
```

**데이터 복제**:
```
- 데이터의 복제본을 여러 노드에 저장
- 시스템 장애가 발생해도 데이터 손실을 방지
```

---

**2. 실시간 검색 및 분석 (Real-time Search & Analytics)**

**실시간 성능**:
```
- 실시간 색인(Indexing)과 검색을 지원
- 대규모 데이터셋에서도 빠른 응답 시간을 제공
```

**강력한 검색 기능**:
```
- 풀 텍스트 검색(Full Text Search) 기능 제공
- 다양한 쿼리 언어를 사용하여 복잡한 검색 가능
```

---

**3. 확장성 및 유연성 (Scalability & Flexibility)**

**수평적 확장**:
```
- 트래픽이나 데이터가 늘어날 경우
- 노드를 추가함으로써 쉽게 시스템을 확장 가능
```

**스키마리스 (Schema-less)**:
```
- 다양한 유형의 데이터 처리 가능
- JSON, Text 등 유연하게 처리
```

---

**4. 통합 솔루션 (Integrated Solution)**

**Elastic Stack**:
```
Logstash + Elasticsearch + Kibana

기능:
- 로깅 (Logging)
- 모니터링 (Monitoring)
- 데이터 시각화 (Data Visualization)
```

**Full-stack 지원**:
```
문서의 수집 및 서비스 운영까지 고려한 full-stack 지원

Integrations (자동 수집) → Elasticsearch → Kibana (시각화)
```

---

#### 용어 비교

| RDBMS | Elasticsearch |
|-------|---------------|
| **Database** | **Search Engine** |
| **Table** | **Index** |
| **Row** | **Document** |
| **Column** | **Field** |
| **Schema** | **Mapping (type)** |
| **SQL** | **Query DSL** |

---

#### Schema-less 특징

**Dynamic Mapping**:
```
Custom mapping이 생략되는 경우:
- 유입되는 데이터를 보고 동적으로 기본 스키마 생성
- Schema-less 방식
```

**DSL**:
```
DSL = Domain Specific Language
```

---

### 1.2 Elasticsearch 데이터 구조

#### 데이터 구조 계층

**구조**:
```
Search Engine
  ↓
Index (인덱스)
  ↓
Type (타입)
  ↓
Document (문서)
  ↓
Field (필드)
```

---

#### 주요 구성 요소

**1. Index (인덱스)**
```
정의: 하나의 독립적인 문서 구조를 가진 문서 집합의 저장 단위
특징: Index 단위로 API 호출
비유: RDBMS의 Table과 유사
```

**2. Type (타입)**
```
정의: 문서의 각 필드의 구조(타입)
예시: string, integer, date 등
```

**3. Mapping (매핑)**
```
정의: 문서를 구성하는 각 필드별 타입의 전체적인 매핑 구조에 대한 설정
비유: RDBMS의 Schema와 유사
```

**4. Document (문서)**
```
정의: 필드로 이루어진 색인의 단위 정보
형식: JSON 형태
비유: RDBMS의 Row와 유사
```

---

### 1.3 Elasticsearch 분산 컴포넌트 구조

#### Shard (샤드)

**정의**:
- **인덱스를 구성하는 물리적인 단위**

**특징**:
- 검색 속도를 위해 샤드 개수 조정
- 인덱스가 샤드 단위로 분리 후 노드에 분산되어 저장

**목적**:
- 데이터 분산 저장
- 병렬 처리로 검색 속도 향상

---

#### Replica (복제본)

**정의**:
- **Shard를 복제한 것**

**목적**:
1. **Throughput 증가**
2. **노드를 손실했을 경우 데이터의 신뢰성 보장**

**특징**:
- 서로 다른 노드에 골고루 분배되어 저장
- Primary Shard와 다른 노드에 배치

---

#### 분산 구조 예시
```
Cluster (클러스터)
  ↓
Node 1, Node 2, Node 3 (노드들)
  ↓
Index A
  ↓
Shard 0 (Primary) → Replica 0 (다른 노드)
Shard 1 (Primary) → Replica 1 (다른 노드)
Shard 2 (Primary) → Replica 2 (다른 노드)
```

---

## 2. 문서 색인 (Indexing)

### 2.1 색인 설정과 매핑

#### Elasticsearch의 색인 설정

**1. Dynamic Mapping (동적 매핑)**

**특징**:
```
- Elasticsearch는 기본적으로 schema-less
- 별도의 설정 없이 색인 가능
- 자동으로 필드 타입 추론
```

**장점**:
```
✅ 빠른 프로토타이핑
✅ 유연한 데이터 처리
```

**단점**:
```
❌ 예상치 못한 타입 매핑
❌ 최적화되지 않은 성능
```

---

**2. Explicit Mapping (명시적 매핑)**

**특징**:
```
- 필드별로 원하는 type을 설정하여 색인
- 정확한 데이터 타입 지정
```

**예시**:
```python
PUT /my-index-000001
{
    "mappings": {
        "properties": {
            "age": {"type": "integer"},
            "email": {"type": "keyword"},
            "name": {"type": "text"}
        }
    }
}
```

**필드 타입**:
```
text: 전문 검색용 (형태소 분석 적용)
keyword: 정확한 매칭용 (형태소 분석 미적용)
integer: 정수
date: 날짜
boolean: 불린
```

---

### 2.2 형태소 분석기 활용

#### 한국어 형태소 분석기의 필요성

**이유**:
```
한국어의 경우 형태소 분석기를 사용해야 원하는 성능을 얻을 수 있음
```

**한국어의 특성**:
```
- 교착어
- 띄어쓰기만으로는 단어 분리 불가
- 조사, 어미 등 처리 필요
```

---

#### Nori 형태소 분석기

**정의**:
- Elasticsearch에서 공식 지원하는 **한국어 형태소 분석기**

**특징**:
```
- Mecab-ko-dic 기반
- Elasticsearch에 내장
- 빠른 분석 속도
```

**설정 예시**:
```python
PUT /korean-index
{
    "settings": {
        "analysis": {
            "analyzer": {
                "nori_analyzer": {
                    "type": "custom",
                    "tokenizer": "nori_tokenizer"
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "content": {
                "type": "text",
                "analyzer": "nori_analyzer"
            }
        }
    }
}
```

---

## 3. 문서 검색 (Search)

### 3.1 Query DSL

#### Query DSL 개념

**정의**:
- Elasticsearch는 **쿼리를 정의하기 위해 JSON 기반의 Query DSL (Domain Specific Language)를 제공**

---

#### 두 가지 타입의 구문

**구조**:
- **트리 형태**로 구성될 수 있음

**1. Leaf Query Clauses (리프 쿼리 절)**
```
정의: 문서의 특정 필드로부터 원하는 조건으로 retrieval 수행

예시:
- match
- term
- range
```

**2. Compound Query Clauses (복합 쿼리 절)**
```
정의: Leaf query clause 또는 다른 compound query clause를 감싸는 형태로 구성

예시:
- bool
- dis_max
- function_score
```

---

#### 두 가지 사용 형태

**각 사용 형태별로 상이한 동작을 함**

**1. Query Context (쿼리 컨텍스트)**
```
특징: 문서 추출 시 relevance score 계산
목적: 얼마나 관련 있는지 점수 계산
```

**2. Filter Context (필터 컨텍스트)**
```
특징: 문서 추출만 하고 score 계산은 하지 않음
목적: 조건에 맞는지 여부만 판단 (Yes/No)
장점: 캐싱 가능, 빠른 성능
```

---

#### 추가적인 Expensive Query

**지원 쿼리**:
- **fuzzy**: 유사한 철자 검색
- **regex**: 정규 표현식 검색
- **prefix**: 접두사 검색
- **wildcard**: 와일드카드 검색
- **range**: 범위 검색
- **script_score**: 스크립트 기반 점수 계산

---

#### Query DSL 예시
```python
GET /_search
{
    "query": {                          # 1. query context임을 의미
        "bool": {                       # 2. compound query clause
            "must": [                   # query context
                {"match": {"title": "search"}},
                {"match": {"content": "Elasticsearch"}}
            ],
            "filter": [                 # 3. filter context
                {"term": {"status": "published"}},
                {"range": {"publish_date": {"gte": "2015-01-01"}}}
            ]
        }
    }
}
```

**설명**:
```
1. query: query context임을 의미
2. bool: compound query clause
   - must와 filter로 이루어짐
   - must는 query context (점수 계산)
3. filter: filter context (점수 계산 안 함)
```

---

### 3.2 검색 결과 확인

#### REST API 호출

**방법**:
- Query DSL을 통해 구문을 생성한 후
- REST API로 호출하여 결과를 얻을 수 있음

---

#### REST API 추가 옵션

**지원 옵션**:
```
1. Target index: 검색할 인덱스 지정
2. 검색 결과 최대 개수: size 파라미터
3. 기타 옵션: timeout, from 등
```

---

#### API 호출 결과 정보

**반환 정보**:
```
1. Top-k의 적합한 문서 리스트
2. 문서별 relevance score
3. 전체 매칭된 문서의 수
4. 기타 메타 정보: shard, timeout 발생 유무 등
```

---

## 4. Query DSL 활용 예시

### 4.1 기본 Full-text Query

#### Match Query

**기본 사용**:
```python
# 기본 full-text query
query_body = {
    "query": {
        "match": {
            "text": {
                "query": "서울 맛집 추천"
            }
        }
    }
}
```

**특징**:
- 형태소 분석기 적용
- 기본 operator는 "OR"
- "서울" OR "맛집" OR "추천" 중 하나라도 포함

---

#### Match Query with Operator

**AND 연산**:
```python
query_body = {
    "query": {
        "match": {
            "text": {
                "query": "서울 맛집 추천",
                "operator": "AND"  # 세 단어 모두 포함되어야 함
            }
        }
    }
}
```

**이유**:
```
검색 결과가 매우 많이 나오기 때문에
AND로 operator 설정해 주는 것이 좋음
```

---

#### Match Phrase Query

**정확한 구문 검색**:
```python
query_body = {
    "query": {
        "match_phrase": {  # 정확히 "서울 맛집 추천"이 나와야 함
            "text": {
                "query": "서울 맛집 추천"
            }
        }
    }
}
```

**특징**:
- 단어 순서까지 정확히 일치해야 함
- 구문 검색에 유용

---

### 4.2 Multi Match Query

#### 여러 필드 검색

**기본 사용**:
```python
# 단일 필드 검색
query_body = {
    "query": {
        "match": {
            "title": {
                "query": "지미"
            }
        }
    }
}
```

**멀티 필드 검색**:
```python
query_body = {
    "query": {
        "multi_match": {
            "query": "지미",
            "fields": ["title", "text"]  # 여러 필드 지정
        }
    }
}
```

**특징**:
- 쿼리를 지정한 후
- 찾고자 하는 field를 여러 개 설정할 수 있음

---

### 4.3 Compound Query (Bool Query)

#### Bool Query 기본

**구조**:
```python
query_body = {
    "query": {
        "bool": {  # bool로 감싸줌
            "must": {
                "match": {
                    "text": {
                        "query": "서울 맛집 추천"
                    }
                }
            }
        }
    }
}
```

---

#### Bool Query 옵션

**1. must**
```
특징: 반드시 매칭되어야 함 (AND)
점수: 계산함 (query context)
```

**2. filter**
```python
query_body = {
    "query": {
        "bool": {
            "must": {
                "match": {
                    "text": {
                        "query": "서울 맛집 추천"
                    }
                }
            },
            "filter": {  # 필터링
                "term": {  # keyword이기 때문에 형태소 분석기 X
                    "title": "지미"
                }
            }
        }
    }
}
```

**특징**:
- 조건에 맞는 것만 필터링
- 점수 계산 안 함 (filter context)
- 캐싱 가능

---

**3. must_not**
```python
query_body = {
    "query": {
        "bool": {
            "must": {
                "match": {
                    "text": {
                        "query": "서울 맛집 추천"
                    }
                }
            },
            "must_not": {  # title에 지미가 포함되어 있으면 안 됨
                "term": {
                    "title": "지미"
                }
            }
        }
    }
}
```

**특징**:
- 해당 조건에 맞지 않아야 함 (NOT)
- 점수 계산 안 함

---

**4. should**
```python
# should 예시 1 - term
query_body = {
    "query": {
        "bool": {
            "must": {
                "match": {
                    "text": {
                        "query": "서울 맛집 추천"
                    }
                }
            },
            "should": {  # title에 홍대가 나온다면 점수를 더 줌
                "term": {
                    "title": "홍대"
                }
            }
        }
    }
}
```
```python
# should 예시 2 - match
query_body = {
    "query": {
        "bool": {
            "must": {
                "match": {
                    "text": {
                        "query": "서울 맛집 추천"
                    }
                }
            },
            "should": {
                "match": {
                    "text": {  # 홍대나 맛집이 나오면 점수를 더 줌
                        "query": "홍대 맛집"
                    }
                }
            }
        }
    }
}
```

**특징**:
- must와 비슷하지만 필수는 아님
- 조건에 맞으면 점수를 더 줌 (가산점)
- 점수 계산함

---

## 전체 요약

### Elasticsearch 핵심 개념
```
Cluster (클러스터)
  ↓
Node (노드)
  ↓
Index (인덱스)
  ↓
Type (타입)
  ↓
Document (문서)
  ↓
Field (필드)
```

---

### RDBMS vs Elasticsearch

| 개념 | RDBMS | Elasticsearch |
|------|-------|---------------|
| **저장소** | Database | Search Engine |
| **테이블** | Table | Index |
| **행** | Row | Document |
| **열** | Column | Field |
| **스키마** | Schema | Mapping |
| **쿼리** | SQL | Query DSL |

---

### 분산 구조
```
Index
  ↓
Primary Shards (분산)
  ↓
Replica Shards (복제)

목적:
- 성능 향상 (병렬 처리)
- 고가용성 (장애 대응)
```

---

### Mapping 방식

| 방식 | 특징 | 장점 | 단점 |
|------|------|------|------|
| **Dynamic** | 자동 생성 | 빠른 시작 | 최적화 부족 |
| **Explicit** | 수동 정의 | 최적화 가능 | 초기 설정 필요 |

---

### Query Context vs Filter Context

| 구분 | Query Context | Filter Context |
|------|---------------|----------------|
| **점수 계산** | ✅ 함 | ❌ 안 함 |
| **캐싱** | ❌ 안 됨 | ✅ 됨 |
| **속도** | 느림 | 빠름 |
| **용도** | 관련도 검색 | 조건 필터링 |

---

### Bool Query 옵션

| 옵션 | 의미 | 점수 계산 | 역할 |
|------|------|----------|------|
| **must** | 필수 (AND) | ✅ | 반드시 매칭 |
| **filter** | 필터링 | ❌ | 조건 필터링 |
| **must_not** | 제외 (NOT) | ❌ | 매칭 제외 |
| **should** | 선택 (OR) | ✅ | 가산점 |

---

### 필드 타입
```
text:
- 전문 검색용
- 형태소 분석 적용
- 예: 본문, 제목

keyword:
- 정확한 매칭용
- 형태소 분석 미적용
- 예: ID, 카테고리, 태그
```

---

## 실전 활용 가이드

### 인덱스 설계

**1. Mapping 설계**:
```python
PUT /product-index
{
    "mappings": {
        "properties": {
            "title": {"type": "text", "analyzer": "nori"},
            "category": {"type": "keyword"},
            "price": {"type": "integer"},
            "created_at": {"type": "date"}
        }
    }
}
```

**2. Shard 개수 설정**:
```
소규모: 1-2 shards
중규모: 3-5 shards
대규모: 5-10 shards
```

**3. Replica 개수 설정**:
```
개발 환경: 0 replicas
운영 환경: 1-2 replicas
고가용성: 2+ replicas
```

---

### 검색 쿼리 최적화

**1. Filter 적극 활용**:
```python
# 좋은 예
{
    "query": {
        "bool": {
            "must": {"match": {"content": "검색어"}},
            "filter": [
                {"term": {"status": "active"}},
                {"range": {"price": {"lte": 10000}}}
            ]
        }
    }
}
```

**2. 적절한 Query 타입 선택**:
```
정확한 구문: match_phrase
여러 필드: multi_match
정확한 값: term
범위: range
```

**3. should 활용한 관련도 향상**:
```python
{
    "query": {
        "bool": {
            "must": {"match": {"content": "기본 검색"}},
            "should": [
                {"match": {"title": "중요 키워드"}},
                {"term": {"category": "선호 카테고리"}}
            ]
        }
    }
}
```

---

### 성능 최적화

**1. 인덱싱 최적화**:
```
- Bulk API 사용
- Refresh interval 조정
- Replica 수 줄이기 (인덱싱 시)
```

**2. 검색 최적화**:
```
- Filter context 사용
- 적절한 size 설정
- _source 필터링
```

**3. 하드웨어 최적화**:
```
- SSD 사용
- 충분한 메모리
- 네트워크 대역폭
```

---

## 주요 개념 정리

### Shard
```
정의: 인덱스를 구성하는 물리적 단위
목적: 데이터 분산, 병렬 처리
조정: 검색 속도 최적화
```

### Replica
```
정의: Shard의 복제본
목적: 고가용성, Throughput 증가
배치: 서로 다른 노드에 분산
```

### Mapping
```
정의: 문서 구조 정의
종류: Dynamic, Explicit
역할: RDBMS의 Schema와 유사
```

### Query DSL
```
정의: JSON 기반 쿼리 언어
구조: 트리 형태
종류: Leaf, Compound
```

### Analyzer
```
정의: 텍스트 분석기
역할: 토큰화, 정규화
한국어: Nori
```

---

## 트렌드 및 Best Practices

### 현재 트렌드
```
1. Elastic Stack 통합 사용
2. 실시간 분석 및 모니터링
3. 로그 분석 표준
4. APM (Application Performance Monitoring)
```

### Best Practices
```
1. 적절한 Shard 개수 설정
2. Filter context 적극 활용
3. Bulk API로 대량 인덱싱
4. Monitoring 및 Alerting 설정
5. 정기적인 성능 최적화
```

---

## 핵심 Takeaway
```
🔍 Elasticsearch: 분산형 검색 및 분석 엔진

📊 구조: Cluster → Node → Index → Document → Field

🔄 분산: Shard (분산) + Replica (복제)

📝 Mapping: Dynamic (자동) vs Explicit (수동)

🔎 Query DSL: JSON 기반, 트리 구조

⚡ Context: Query (점수) vs Filter (필터링)

🇰🇷 한국어: Nori 형태소 분석기

🔧 Bool Query: must, filter, must_not, should

📈 최적화: Filter 사용, 적절한 Shard 수

🚀 실시간: Near Real-time Search
```

---

## 실전 체크리스트

### 인덱스 생성 시
```
✅ Mapping 정의 (Explicit 권장)
✅ Analyzer 설정 (한국어: Nori)
✅ Shard 개수 결정
✅ Replica 개수 결정
✅ Index 이름 규칙 정의
```

### 검색 쿼리 작성 시
```
✅ 적절한 Query 타입 선택
✅ Filter context 적극 활용
✅ Bool Query로 조건 조합
✅ Size 적절히 설정
✅ 필요한 필드만 반환 (_source)
```

### 운영 시
```
✅ Monitoring 설정
✅ Alerting 설정
✅ 정기적인 성능 체크
✅ Index 관리 (삭제, 최적화)
✅ Backup 설정
```
