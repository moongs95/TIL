# 기초대수학

## 대수학적 특징

### 수학적 객체

- 자연수, 정수, 유리수, 무리수, 실수, 복소수
- 집합, 함수, 벡터, 행렬, 그래프, 디지털 소자
- 필요에 따라 새로운 수학적 객체를 정의

### 수학적 객체에 대한 연산의 정의

- 복소수(수학적 객체) -> 덧셈, 뺄셈, 곱셈, 나눗셈, 켤레 복소수
- 새로 만든 수학적 객체에 맞는 새로운 연산을 정의
- 아예 새로운 연산을 정의하는 경우도 있지만 기존 연산을 확장시키는 경우가 많음

```text
`수학적 객체 + 연산`

새로 정의된 연산을 사용하는 과정에 대한 엄밀한 약속이 필요
```

## 교환법칙(Commutative Property)

- a+b=b+a
- 수에 대한 덧셈은 commutative함
- a−b≠b−a
- 수에 대한 뺄셈은 anti-commutative함
- a×b=b×a
- 수에 대한 곱셈은 commutative함
- a÷b≠b÷a
- 수에 대한 나눗셈은 anti-commutative함

## 결합법칙(Associative Property)

- (a+b)+c=a+(b+c)
- 수에 대한 덧셈은 associative함
- (a−b)−c≠a−(b−c)
- 수에 대한 뺄셈은 anti-associative함
- (a×b)×c=a×(b×c)
- 수에 대한 곱셈은 associative함
- (a÷b)÷c≠a÷(b÷c)
- 수에 대한 나눗셈은 anti-associative함

## 분배법칙(Distributive Property)

- a×(b+c)=a×b+a×c
- (b+c)×a=b×a+c×a
- 곱셈은 덧셈에 대해 distributive함

- a×(b−c)=a×b−a×c
- (b−c)×a=b×a−c×a
- 곱셈은 뺄셈에 대해 distributive함

- a÷(b+c)=a÷b+a÷c
- (b+c)÷a=b÷a+c÷a
- 나눗셈은 덧셈에 대해 distributive함

- a÷(b−c)=a÷b−a÷c
- (b−c)÷a=b÷a−c÷a
- 나눗셈은 뺄셈에 대해 distributive함

## 항등원(Identity)

- 자기 자신이 나오는 값
- a+0=a
- additive identity는 0
- a×1=a
- multiplicative identity는 1

## 역원(Inverse)

- 항등원이 나오는 값
- a+(−a)=0
- a의 additive inverse는 −a
- a×1/a=1
- a의 multiplicative inverse는 1/a = a^−1

## 대수학적 특징 사용 예시

### 방정식의 풀이

- ax+b=c
- 방정식을 푸는 과정 = 방정식을 만족시키는 x의 값을 구하는 과정
- 주어진 방정식을 x = α의 꼴로 바꿔야 함

1. 좌변에서 b를 제거 -> 양변에 b에 대한 additive inverse를 더함
2. 좌변에서 a를 제거 -> 양변에 a에 대한 muliplicative inverse를 곱함

### 곱셈공식

- (a+b)^2 = a^2+2ab+b^2
- (a-b)^2 = a^2-2ab+b^2
- (a+b)(a-b) = a^2 - b^2
- 분배법칙, 교환법칙 사용
- 역원, 항등원 사용(합차공식)
