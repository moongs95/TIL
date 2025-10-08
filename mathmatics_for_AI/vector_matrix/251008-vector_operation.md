# 벡터와 벡터의 연산

## 벡터의 정의

1. 순서쌍으로서의 벡터(CS)
2. 화살표로서의 벡터(물리학)

- 스칼라 : 하나의 값으로만 특정한 물리량 표현 ex. 돈, 에너지, 가격
- 벡터 : 크기와 방향을 가진 물리량을 나타낼 때 사용되는 수학적 객체 ex. 속도, 힘, 바람

### 벡터의 차원

- 원소의 개수가 n개 = n차원 벡터

### 벡터의 공간

- n차원 벡터의 집합, n차원 vector space, real vector space
- 좌표 평면은 2차원 벡터들의 집합(R square)
- 좌표 공간은 3차원 벡터들의 집합(R cube)

### 벡터의 표현

- bold체로 표현하면 vector

## 벡터의 길이

- 벡터의 길이는 norm이라고 부르고 |⋅|, ||⋅||기호를 사용하여 표현
- 피타고라스 정의 사용
- 차원이 늘어나도 그대로 계산, 고차원이어도 일반화가 가능

## 벡터의 연산

- 수학적 객체 : 벡터
- 연산 : 덧셈, 뺄셈, 스칼라 곱셈, 내적, 외적, 정사영

### 같은 벡터

- 두 벡터가 같은 점을 가리킬 때 같은 벡터
- 모든 원소가 같다면 같은 벡터

## 벡터의 덧셈

- 두 개의 벡터를 입력받아서 새로운 벡터를 출력하는 연산
- 평행사변형 법, tip-to-tail method
- 구하는 방식만 다를 뿐 값은 동일

### 벡터 덧셈의 대수학적 특징

- Commutative Property **u+v=v+u** 교환법칙 성립(스칼라의 교환법칙 이용)
- Associative Property  **(u+v)+w=u+(v+w)** 결합법칙 성립(스칼라의 결합법칙 이용)
- Additive Identity  **u+0=u** 어떤 벡터를 더해야 자기 자신이 나오는지? 0벡터(스칼라의 항등원 이용)
- Additive Inverse  **u+(−u)=0** 어떤 벡터를 더해야 항등원(제로벡터)가 나오는지? **−u**, negative u(스칼라의 역원 이용) 

## 스칼라 곱셈

- Scalar Multiplication : 스칼라ㅇ와 벡터의 곱
- 스칼라 하나, 벡터 하나를 입력 받아서 벡터를 만드는 연산
- 중간에 기호가 없음, 그대로 붙임(implicit) -> 중요 point!
- 원소에 모두 k를 곱해줌
- k > 0이면 scalar multiplication은 벡터의 방향 바뀌지 않음
- k > 1, norm 길이 늘어남
- 0 < k < 1, norm 길이 줄어듦
- k < 0이면 scalar multiplication은 벡터의 방향이 정반대로 바뀜
- k < -1, norm 길이 늘어남
- -1 < k < 0, norm 길이 줄어듦
- 방향을 바꾸거나 길이 변경

### 스칼라 곱셈의 대수학적 특징

- Associative Property k(lu)=(kl)u 곱셈의 결합법칙
- Distributive Property (k+l)u=ku+lu, k(u+v)=ku+kv 곱셈의 분배법칙
- Multiplicative Identity 1u=u 곱셈의 항등원은 1

## 벡터의 뺄셈

- 벡터의 덧셈과 스칼라 곱셈을 통해서 벡터의 뺄셈을 구함
- **u** - **v** = **u** + (-**v**)

1. -**v** : **v**를 뒤집어 줌
2. **u**+(-**v**) : 뒤집어 준걸 **u**에 더해줌

### 벡터의 뺄셈의 대수학적 특징

- Anti-commutative Property u−v≠v−u 스칼라와 동일, **u**와 **v**가 같다면 0벡터가 되서 commutative함
- Anti-associative Property (u−v)−w≠u−(v−w) 스칼라와 동일, **w**가 0벡터면 commutative함

## 벡터의 정규화

1. ||**u**|| = 1 → unit vector
2. **u**와 **v**가 수직일때

- Nomaligation = Unitigation
- 입력받은 벡터를 unit vector로 바꾸는 연산
- **u**hat = **u** / ||**u**||
- 1/||u||은 항상 양수임 → 따라서 방향이 바뀌지 않음
- Scalar multiplication과 다를 바 없음
- 2차원 벡터를 정규화하면 unit circle 위의 벡터로 바뀜
- 3차원 벡터를 정규화하면 unit sphere 위의 벡터로 바뀜

## 벡터 사이의 거리

- 좌표 사이의 거리
- d(**u**, **v**) = ||**u**−**v**|| = ||**v**−**u**||
- norm을 구하면 됨
- L1 거리 = 절대값
- L2 거리 = 제곱, 유클리드 거리
- L3 거리 = 세제곱의 절대값
