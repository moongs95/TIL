# 역행렬(Inverse Matrix)과 행렬식(Determinant)

→ 개념만, 모든 개념이 유기적으로 연결

## 단위행렬(항등행렬)

Multiplicative Identity = Identity Matrix

AI=IA=A

## 역행렬

→ mXm, nXn 형태

Multiplicative Inverse = Inverse Matrix

곱셈에 대한 역원
AB=BA=I ⟶ B=A^(−1)

## 2×2 행렬의 역행렬

1/ad-bc X bc는 부호를 바꾸고, ad는 자리를 바꿔줌

## 행렬식

ad−bc=0이라면  A^(-1)은 존재할 수 없음

즉 모든 행렬의 역행렬이 존재하는 것은 아님

2×2 행렬의 ad−bc를 계산해보면, 해당 행렬의 역행렬이 존재하는지 확인할 수 있음 → 역행렬의 리트머스지 같은 느낌

ad-bc가 2×2 행렬의 행렬식

→ 행렬식의 기하학적인 의미 유튜브 찾아보기

## 역행렬 구하기

Step.1) A, I로 augmented matrix를 만들기

Step.2) A를 I로 만들기(기본행렬 연산)

이 결과로 기존의 I는 A^(-1)로 바뀜

→ 공식(2X2만 가능)으로 구해도 동일한 결과

→ 이를 이용하면 3X3, 4X4, … nXn확장 가능

→ 역행렬을 구하는 다른 방식도 있음

**행렬식 구하기**

→ 역행렬이 존재하는지 안존재하는지 판단

Upper Triangular Matrix의 Determinant
→ main diagonal element를 모두 곱해주면 됨

⇒ upper triangle matrix로 만들어 주기(여인수 전개)

Operation.1 Row Exchanging

Ri⟷Rj ⟶ det(EA)=−det(A)

Operation.2 Row Multiplication

Ri⟵kRi ⟶ det(EA)=k⋅det(A)

Operation.3 Row Addition

Ri⟵Ri+Rj ⟶ det(EA)=det(A)
