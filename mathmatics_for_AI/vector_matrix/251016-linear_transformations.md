# 선형변환(Linear Transformations)

## 선형변환의 정의

벡터를 변환 → 행렬과 벡터의 곱으로 변환

matrix X vector = vector

→ y = f(x)처럼 T(u) = Tu로 나타냄

→ n차원 벡터를 입력해서 m차원 벡터를 출력하는 변환

왜 선형적?

Linearity를 만족 = Homogeneity(균일성, 균등성) + Additivity(가산성)

→ 두 조건을 모두 만족

## 선형변환의 종류

2차원 벡터에 대한 선형변환
- reflection
- scaling
- shearing
- rotation
- projection onto axes

## 대칭변환(Reflection Transformation)

→ 이미지 처리

x축 대칭 변환 : y값을 negative하게 바꿔줌

```text
[[1, 0],
[0 , -1]]
```

y축 대칭 변환 : x값을 negative하게 바꿔줌

```text
[[-1, 0],
[0 , 1]]
```

원점 대칭 변환 : x, y값을 negative하게 바꿔줌

```text
[[-1, 0],
[0 , -1]]
```

→ 모든 점에 대해서 대칭변환(원본을 복원할 수 있음) ⇒ 이미지도 대칭변환할 수 있음

## 사형변환(Projection Transformation)

x축 사형변환 : y값을 0으로 만듦

```text
[[1, 0],
[0 ,0]]
```

y축 사형변환 : x값을 0으로 만듦

```text
[[0, 0],
[0 , 1]]
```

→ 원본을 복원시키지 못하는 변환(1:1 대응이 아니기 때문), 위 아래로 대칭이동해도 같은 값

## 스케일 변환(Scaling Transformation)

→ 이미지를 늘리거나 줄임

x축 스케일 변환 : y는 그대로 x 좌표를 변경해줌

```text
[[a, 0],
[0 , 1]]
```

y축 스케일 변환 : x는 그대로 y 좌표를 변경해줌

```text
[[1, 0],
[0 , b]]
```

x축 + y축 스케일 변환 : x, y 값 변경해줌

```text
[[a, 0],
[0 , b]]
```

→ a, b > 0 이라면 늘어남, 0< a, b < 1 라면 줄어듦

## 전단변환(Shearing Transformation)

x축 방향으로 양쪽에서 눌러줌

```text
[[1, a],
[0 , 1]]
```

y축 방향으로 양쪽에서 눌러줌

```text
[[1, 0],
[b , 1]]
```

→ 활용도가 높진 않음

## 회전변환(Rotation Transformation)

→ 가장 특이하고 중요

반시계 방향의 회전변환

```text
[[cosθ, -sinθ],
[sinθ , cosθ]]
```

시계 방향의 회전변환

```text
[[cosθ, sinθ],
[-sinθ , cosθ]]
```

radian

3.14(**π**) → 반바퀴

6.28(2**π**) → 한바퀴


→ 우함수(cos) 기함수(sin) 성질로 인해 모두 negative를 주면 저렇게 변경됨
