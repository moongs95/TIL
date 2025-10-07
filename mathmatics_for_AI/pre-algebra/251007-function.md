# 함수

## 정의

- 두 집합 X, Y에 대해 X의 원소가 Y에 오로지 하나만 대응되는 관계
- x(출력) → function(지령된 연산) → y(입력) : 인공지능 알고리즘
- Domain(X) : 함수의 입력값이 될 수 있는 모든 값들의 집합
- Codomain(Y) : 함수의 출력값이 될 수 있는 모든 값들의 집합
- Range(R) : 함수의 실제 출력값들의 집합
- Injective : 같은 y는 한 번씩만 대응, many-to-one Not OK
- Surjective : Codomain = Range, 모든 y는 적어도 하나의 x에 대응
- Bijective : Injective + Surjective -> 둘 다 만족, 1:1대응, 역함수 조건

## 함수의 그래프

- 모든 Domain의 원소(x)에 대한 함숫값(f(x))의 쌍(x, f(x))을 좌표계 위에 나타낸 것
- (x, y)라는 원소, 점들의 집합
- 함수의 특성을 이해하는데 가장 좋은 도구

## 함수의 변형

- 대칭이동, 평행이동, 수축과 팽창

### 함수의 평행이동

- horizontal translations(x축 방향) y=f(x) -> y=f(x−α) => α만큼 이동하는 건 x-α, -α만큼 이동하는 건 x+α
- vertical translations(y축 방향) y=f(x) -> y−β=f(x) -> y=f(x)+β => β만큼 이동하는 건 y-β, -β만큼 이동하는 건 y+β
- vertical + horizontal translations(x, y축 방향) y=f(x) -> y=f(x−α)+β => α, β만큼 이동하는 건  x-α, y-β

### 함수의 대칭이동

- across the y-axis y=f(x) -> y=f(−x) ⇒ y축 대칭은 x대신에 -x를 넣음
- across the x-axis y=f(x) -> −y=f(x) -> y=−f(x) ⇒ x축 대칭은 y대신에 -y를 넣음
- across the origin y=f(x) -> y=−f(−x) ⇒ 원점 대칭은 둘 다 부호 변경

### 함수의 수축과 팽창

- horizontal dilations y=f(x) -> y=f(α⋅x) ⇒ x축으로 수축과 팽창
- vertical dilations y=f(x) -> β⋅y=f(x) -> y=1/β ⋅f(x) ⇒ y축으로 수축과 팽창
- vertical + horizontal dilations y=f(x) -> y=1/β f(α⋅x)
- Compressing α>1, β>1 ⇒ 1보다 크면 수축이 일어나고
- Stretching 0<α<1, 0<β<1 ⇒ 1보다 작으면 팽창이 일어남

### 삼각함수를 위한 대칭이동

- x=1일 때 대칭이동 => x -> 2-x
- x=α일 때 대칭이동 => x -> 2α-x
- y=1일 때 대칭이동 => y -> 2-y
- y=β일 때 대칭이동 => y -> 2β-y

## 우함수와 기함수

### 우함수(Even Functions)

- 좌우대칭 했을 때 자기 자신이 그대로 나오는 함수
- y=f(x)^2 → -x를 넣어도 같음
- x제곱, x네제곱, cos(x)
- 적분할 때 용이함, 함수들 방정식 풀때

### 기함수(Odd Functions)

- 원점대칭했을 때 자기 자신이 그대로 나오는 함수
- y=x → -y, -x를 넣어도 같음
- x, x세제곱, sin(x), tan(x)
- 적분할 때 용이함, 항상 0이 나옴

### 우함수와 기함수의 특징

- 상수를 곱해도 우함수, 기함수가 됨
- c⋅(odd) = (odd)
- f(−x)=−f(x) -> cf(−x)=−cf(x)
- c⋅(even) = (even)
- f(−x)=f(x) -> cf(−x)=cf(x)

- 우함수, 기함수끼리 더하거나 빼도 자기 자신
- (even) ± (even) = (even)
- f(−x)=f(x), g(−x)=g(x), h(x)=f(x)±g(x) -> f(−x)±g(−x)=f(x)±g(x) -> h(−x)=h(x)
- (odd) ± (odd) = (odd)
- f(−x)=−f(x), g(−x)=−g(x),  h(x)=f(x)±g(x) -> f(−x)±g(−x)=−(f(x)±g(x)) -> h(−x)=−h(x)
- 우함수, 기함수 곱셈은 차수에따라 달라짐
- (odd) × (odd) = (even)
- (odd) × (even) = (odd)
- (even) × (even) = (even)
- 홀수 X 홀수 = 짝수, 홀수 X 짝수 = 홀수, 짝수 X 짝수 = 짝수

## 합성함수(Composition Function)

- 입력 -> 출력=다른 함수의 입력 -> 최종 출력
- h(x) = (g ∘ f)(x) = g(f(x))
- 딥러닝 신경망의 여러 층을 합성함수로 생각할 수 있음

## 역함수(Inverse Function)

- 합성함수를 이용 + 항등함수(f(x) -> g(x) -> f(x), 자기 자신이 그대로 나오는 함수, g(f(x)) = f(x))
- 항등함수가 나오게 하는 함수가 역함수
- 함수 f가 inverse function을 가지기 위해선 f가 bijective function이어야 함

## 증가/감소함수

### 증가함수
- x가 증가할 때 y도 함께 증가하는 함수
- x1 < x2 ⟷  f(x1) < f(x2)

### 감소함수

- x가 증가할 때 y는 감소하는 함수
- x1 < x2 ⟷  f(x1) > f(x2)

### 증가/감소함수와 부등식

- 주어진 부등식을 만족시키는 x의 범위를 구하는 과정
- 방정식과 마찬가지로 부등식의 좌변을 x로 정리
- 부등호가 바뀌지 않을 때 : 부등호의 양변에 같은 수를 더하거나 뺄 때, 부등호의 양변의 함수를 같은 증가함수에 입력했을 때
- 부등호가 바뀔 때 : 부등호의 양변의 함수를 같은 감소함수에 입력했을 때
