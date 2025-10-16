# 선형시스템

→ 역행렬 determinant를 구하기 위해

## 선형시스템의 정의

Linear System = System(연립) of Linear Equations

→ x들의 값을 구한다.

리니어하지 않은 상황도 리니어 근사하게 만듦 → solution 구하기 쉽기 때문

## 선형시스템과 행렬, 벡터

SLE는 행렬, 벡터에 대한 방정식으로 간단하게 표현할 수 있음

A : coefficient matrix 계수 행렬
x : variable vector 변수 벡터
b : constant vector 상수 벡터

## 선형시스템의 풀이

A, B가 주어졌을 때, 방정식을 만족시키는 x를 구하는 과정

Hyperplane들의 intersection을 구하는 과정

## 선형시스템의 활용

Span에 벡터가 포함되는지 확인하기

벡터들의 독립성

선형변환 전의 벡터

→ 역추적

## 첨가행렬(Augmented Matrix)

Coefficient matrix와 constant vector를 합친 augmented matrix

→ 선형시스템 표현의 편의성

## 기본 행 연산(Elementary Row Operations)

Operation.1 Row Exchanging Ri ⟷ Rj

→ 분수꼴을 정수로 변환할 수 있음

Operation.3 Row Addition Ri ⟵ Ri + Rj

→ 계수끼리 더해서 0이 되는 경우 변수를 없애줄 수 있음

→ 곱해서 더해주는 것

## 기본행렬(Elementary Row Matrix)

→ 앞에 곱해주는 행렬은 원래 항등행렬 ⇒ 이를 변경해서 행 연산

Operation.1 Row Exchanging

→ 앞에 곱해주는 행렬로 어떤 행을 살릴지 결정

Operation.2 Row Multiplication

Operation.3 Row Addition

## 가우스-조던 소거법(Gaws-Jordan elimination)

가우시안 소거법

Reduced Row Echelen form

단계적인 row operation을 통해 SLE를 풀어나가는 과정
→ n개의 x로 나타내는 방정식 해결

cofficient matrix를 **identity matrix**로 만들면 됨

## 가우스-조던 소거법(해가 존재하는 경우)


## 가우스-조던 소거법과 벡터의 독립성

서로 독립적인지 보기 위해서 → 선형 방정식 = 0일때 모든 해의 값이 0밖에 존재하지 않을때 서로 독립적

## 스팬에 포함된 벡터

**v**가 선형결합으로 나타낼 수 있는지

## 가우스-조던 소거법(무수히 많은 해가 존재하는 경우)

1개의 solution, 해가 무수히많은, 해가 존재하지 않는 solution ⇒ 3개 밖에 없음

→ 3번째가 전부 다 0이 되서 해가 0 ⇒ 0, 0, 1 불가능

a1 = 1, a2 = 1 + a3 → 관계식을 만족하면 항상 해가 존재

변수가 3개인데 식이 2개 → 자유도를 낮출 수 없어서 무수히 많은 해가 존재

## 가우스-조던 소거법(해가 존재하지 않는 경우)

→ 3번째가 0 0 0인데 -8?
0=-8을 만족시키는 a가 없음 → solution이 없음

u1, u2, u3의 선형결합으로 나타낼 수 없음 ⇒ span에 포함되지 않음
