# 벡터의 정사영

- Projection : 수직으로 그림자
- Scalar Projections : 출력이 스칼라
- Vector Projections : 출력이 벡터

## 스칼라 정사영

- comp_vu = ||u||cosθ
- scalar projection of u onto v
- v 벡터에 u벡터를 정사영 시킴
- 기하학적으로 내적 구할 때 사용 -> ||u||cosθ
- 반대 방향이라면 음수값이 나옴
- -1 <= cosθ <= 1, -||u|| <= comp_vu <= ||u||
- unit vector일 경우 cosθ

## 벡터 정사영

### 유도 1

- v와 상관없는 성분은 없애고, v와 관련된 성분만 가지고 있는 벡터
- 벡터로 표현된 comp_vu, proj_vu
- 스칼라 projection(길이=norm) x unit vetcor(같은 방향) ⇒ 벡터

### 유도 2

- 선들을 먼저 구하고 수직인지 확인
- unit vector라면 proj_vu = (cosθ)v
- 수직이라면 proj_vu = 0

## 벡터의 분해

- u를 벡터들의 합으로 분해하는 과정(u1 + u2 = u)
- 하나의 벡터를 나누는 방법은 무수히 많음
- 3개 이상으로도 분해 가능(v1 + v2 + v3 = u)

### Component Vecotr가 미리 정해진 경우

- u 벡터를 분해하려고 하는 데 이미 component vector 하나가 정해진 상황이라면 나머지 하나를 구하는 걸로 변형
- v + w = u -> w = u -v
- 벡터 방정식으로 구함

### 벡터의 수직 분해

- orthogonal decomposition
- u를 orthononal한 벡터들로 분해하는 과정
- 계산이 편리해짐
