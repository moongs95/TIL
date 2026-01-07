# RAG & Limitations of LLMs

## Hallucination

- 쿼리가 들어오면 data source에서 retreiver을 통해 답변하기 때문에
- 그럴듯한 답변을 할 수가 없음

## Outdated Knowledge

- data에 있는 내용을 바탕으로 inference 가능

## Untraceable reasoning prosess

- 여전히 불투명성은 존재하지만
- 잘못된 답변을 생성했을 때 어느 부분에서 추출을 잘 못했는지 확인이 가능

## Bias

- RAG여도 개선되지 않을 수 있음
- Data 자체에 편향이 있다면 RAG를 사용해도 여전히 남아있는 문제

## RAG로 인해 발생하는 한계

1. 데이터 소스가 불충분하고 부정확한 사실을 포함한다면 옳은 답변을 retrieval 못함

2. 데이터 소스에 답이 있어도 retrieval 단계에서 실패할 수 있음

3. generator가 정답을 제대로 받아도 쿼리의 의도에 맞는 정답 생성에 실패할 수 있음
