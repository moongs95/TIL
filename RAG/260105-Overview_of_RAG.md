# Overview of RAG

## Plan Generative LM Pipeline

1. User input

- Parametric memory
- LM이 이미 학습되어 있다는 뜻

2. Generation

- Generation based on parametric memory

---

### 한계가 존재

- 비쌈
- 학습 리소스 매우 큼
- 월간, 주간 재학습 어려움
- Hallucination, Outdated, misalignment ...
- 불투명성

## RAG Pipeline

1. Indexing

- Document chunking Embedding
- 데이터 준비
- 관련문서 처리 -> 유저 쿼리 해결에 사용
- chunking : 문서 길이 다 다름 -> 관리하기 용이하게 분할
- 유저쿼리와 비슷한 문서 가져오기 위해 청킹마다 유사도 임베딩

2. User input

3. Retrieval

- Retrieve corresponding documnet
- 관련 문서 찾기
- BM25(전통적), 언어모델로 검증
- 유사도 기반, 답변 위해 여러 청크 필요할 수 있음

4. Generation

- Retrieved Document + User query
- 관련문서와 쿼리른 LLM에 같이 넣으면 언어 모델이 생성

### LM과의 차이점

- Indexing, Retrieval 단계 추가
- 외부 메모리 사용 -> non-parametric memory

## Static RAG

- Retrieval : TF-IDF or BM25
- Generation : Pretrained LM + No Fine-tuning
- Augmentation : Basic

## Pivotal Questions in RAG

1. What to retrieve

- granularity : from token to chunks, KG
- source : structured/unstructured/LLM generated
- 청크 사이즈 클수록 정보의 양이 많지만 정확도는 떨어짐
- 청크 사이즈 작을 수록 정확도는 올라가지만 문맥 반영이 어려움

2. When to retrieve

- single, adaptive(항상 검색이 필요하지 않음, 선택적 retrieve), multiple

3. How to use the retrieved information

- input, intermediate layer, output layer
- reireive + 유저 쿼리
- 프롬프트 어떻게 결합할지 활용의 부분
