# Modeling tuning & Operation


## Hyper parameter tuning

- Hyper parameter : 최적의 파라미터를 도출하기 위해 우리가 직접 세팅하는 값
- 대표적 방법론
1. Grid-Search : 하이퍼 파라미터를 일정한 간격으로 변경하며 최적의 파라미터를 찾아가는 기법
2. Random Search : 정해진 범위 내에서 Random하게 하이퍼 파라미터 탐색
3. BayesianOptimization : 입력값(x)를 Input으로 하는 목적 함수 f(x)를 찾는 것, x(hyper-parameter)/f(x)(precision, recall, AUC 등) -> 주로 사용
- 순차적으로 하이퍼 파라미터를 업데이트해 가면서 평가를 통해 최적의 하이퍼 파라미터 조합을 탐색


## Model explanation

- Permutation Importance : 모델 상관없이 모든 알고리즘에 다 가능 함.
- Shapley Value : 양과 음의 관계를 같이 볼 수 있음.
- 두 가지 모델 비교해서 신뢰성 확보


## Modeling operation

- Target 고객 수준 결정
- Model Save
- Mart 생성
- Model Input
- Target 추출
