# 벡터의 내적

- 벡터의 연산 중 가장 중요한 연산
- Dot Product

## 내적의 정의

- Algebraic Approach : 연산에 대한 dot product의 정의, 실제 dot product를 연산할 때 자주 사용
- Geometric Approach : 기하학적인 dot product의 의미, 의미를 해석할 때 자주 사용

### 내적의 대수학적 정의

- 원소별로 곱하고 모두 더하는 연산
- 연산 결과가 scalar이므로 scalar product라고 부름
- n차원 x n차원 -> 스칼라

### 내적의 기하학적 정의

- u ⋅v = ∥u∥∥v∥cosθ
- 정사영시킨 후 사각형 넓이가 내적 값
- cosθ값에 따라 음수가 될 수 있음
- θ=pi일 때 -∥u∥∥v∥
- θ=0일 때 ∥u∥∥v∥
- -∥u∥∥v∥ <= u ⋅v <= ∥u∥∥v∥

## 내적의 대수학적 특징

- Commutative Property : **u⋅v=v⋅u** 교환법칙 성립
- Anti-associative Property : **(u⋅v)⋅w≠u⋅(v⋅w) →** 정의 자체가 되지 않음, 스칼라(벡터와 벡터의 내적은 스칼라)와 벡터는 내적을 할 수 없음
- Distributive Property : **u⋅(v+w)=u⋅v+u⋅w** 분배법칙 성립
- Homogeneity : **(**k**u)⋅v=u⋅(**k**v)=**k**(u⋅v)** 안에 있는 스칼라는 밖으로 빼줄 수 있음
- Zero Vectors :  **0⋅u=**0
- Zero Dot Product : u⋅v=0 ↛ u=0∨v=0 둘다 0벡터가 아닐 수 있음

## 내적과 놈

- u⋅u = ||u||^2
- 놈끼리 비교할 때는 self 내적으로 구함
- 연산 효율성을 위해 루트를 뺌
- 길이를 비교할 때도 동일

## 벡터의 곱셈공식

- (u+v)^2=∥u∥^2+2(u⋅v)+∥v∥^2
- (u−v)^2=∥u∥^2−2(u⋅v)+∥v∥^2
- (u+v)⋅(u−v)=∥u∥^2−∥v∥^2
- (x+u)⋅(x+v)=∥x∥^2+(u+v)⋅x+u⋅v
- (ax+u)⋅(bx+v)=ab∥x∥^2+(bu+av)⋅x+u⋅v

## 내적과 수직성

- perpendicular = orthogonal
- ||u|| = 1 (unit vector)
- 두 벡터가 수직인지 알아보기 위해서 내적을 활용
- 두 벡터가 수직이라면 두 벡터의 내적은 0
- 제로벡터의 내적을 제외하고 고려
- 수직하는 두 벡터의 내적은 0인 것을 곱셉공식에 접목시킬 수 있음

## 코사인 유사도

- 딥러닝, 머신러닝에서 광범위하게 사용
- 비슷한 것이 거리가 제일 가까운 것일까? -> 아님
- 가리키는 방향이 같은 것이 비슷한 것
- 비슷할 수록 각도는 0, cosθ는 1에 가까워짐, 반대일 수록 각도는 파이, cosθ는 -1에 가까워짐 ⇒ 코사인을 이용한 유사도 측정
- -1 ≤ cosine similarity ≤ 1 (끼인각을 이용)
- cosθ = u⋅v/∥u∥∥v∥ ⇒ unit vector라면 분모가 1이 됨으로 내적만 구하면 됨
