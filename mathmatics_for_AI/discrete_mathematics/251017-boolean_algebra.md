# 불대수
## Boolean Values

TRUE : 1, 1.0, 5V(3.3V), Yes

FALSE : 0, 0.0, 0V, No

→ 2가지 state만 존재

불리안으로 논리연산을 다룸

In mathematics and mathematical logic, Boolean algebra is a branch of algebra.
It differs from elementary algebra in two ways.
First, t**he values of the variables are the truth values** true and false, usually denoted 1 and 0,
whereas in elementary algebra the values of the variables are numbers.
Second, Boolean algebra uses **logical operators**
such as **conjunction** (and) denoted as ∧, **disjunction** (or) denoted as ∨, and the **negation** (not) denoted as ¬.
Elementary algebra, on the other hand, uses arithmetic operators such as addition, multiplication, subtraction, and division.
Boolean algebra is therefore a formal way of describing logical operations,
in the same way that elementary algebra describes numerical operations.
Ref. Wikipedia

## Digital Logic Gates

디지털 소자

Logic gates are the instantiated logical operators

→ 함수

NOT gate

진리표 : truth table

Y = A바 바는 not을 의미

False를 받으면 True, True를 받으면 False를 출력해줌

AND gate, OR gate

두 개의 입력(T/F)을 받아서 하나(T or F)를 출력

Y = A·B = AB, Y = A + B

→ 기호만 같을 뿐 곱하기, 덧셈과는 다른 연산

XOR gate

서로 입력이 다를 때 1을 출력, 같을 때는 0을 출력

Y = A ⊕B

논리 소자를 가지고 이어준 것 : 논리 회로

AND - NOT / OR - NOT / XOR - NOT

→ 모두 반대로 나옴

NAND gate / NOR gate / XNOR gate

Y = (AB)바 / Y = (A + B)바 / Y = (A ⊕B)바

가산기 회로

### Half Adder

마지막에는 carry over

A + B = C(AB) S(A⊕B)

HA : 반쪽짜리 덧셈기

### Full Adder

FA : 이전 단계에서 넘겨준 것 까지 계산

### 4bit Adder

4자리 숫자

→ 4개만 받아서 4개로 출력 넘어가는 건(Cout) 오버플로우

⇒ FA + FA + FA + HA

### Boolean Algebra Laws

A, B는 T/F

X⋅0=0
0⋅0=0
1⋅0=0

X⋅1=X
0⋅1=0
1⋅1=1

X⋅X=X
0⋅0=0
1⋅1=1

X⋅X바=0
0⋅1=0
1⋅0=0

X+0=X
0+0=0
1+0=1

X+1=1
0+1=1
1+1=1

X+X=X
0+0=0
1+1=1

X+X바=1
0+1=1
1+0=1

교환법칙

XY=YX
(XY)Z=X(YZ)

X+Y=Y+X
(X+Y)+Z=X+(Y+Z)

분배법칙

X(Y+Z)=XY+XZ

드모르간 법칙과 같음

(XY)바=X바+Y바, (X+Y)바=X바⋅Y바

X⊕Y=(X+Y바)⋅(X바+Y)=X바Y+XY바

→ 실수와 다르게 작용한다

### 디지털 회로의 간략화

회로가 많으면 전기를 많이 잡아먹음 → 비효율적

연산의 결과가 동일하다면 간략화 할 수 있음, 연산속도 효율적, 배터리 아낌

Y = AB + BC(B + C)

→ B(A+C)와 동일, 불대수의 연산 규칙

⇒ 5개의 연산이 2개로 간략화

## Karnaugh Map

The Karnaugh(/ˈkɑːnɔː/) map (KM or K-map) is **a method of
simplifying** Boolean algebra expressions.
Ref. Wikipedia

## Karnaugh Map(2-inputs)

truth table이 주어졌을 때 간략하게 만들어 주는 방법

위 아래, 가로 세로가 1일 때 묶어

→ 그냥 B값이 1일때 1이 됨

A는 not이든 아니든 상관없음 don’t care → A는 식에서 빠짐

→ B가 not일때 1

A는 don’t care → 식에서 빠짐

→ 이번에는 B가 don’t care

→ A, B 모두 don’t care

→ 2X2 간략화 시킨 소자를 연결할 수도 있음

## Karnaugh Map(3-inputs)

→ 순서가 달라짐 1이 변하는 순으로 변경(gray code)

똑같이 1을 연결해서 don’t care를 빼주고 식을 간략화 함

카르노 맵 반대로도 넘어갈 수 있음

4개를 한 번에 묶어줄 수있음 → 4개일 경우 2개가 don’t care가 됨

위 아래로 확장만 가능

가로로 4개 확장 가능 → 이 경우도 2개가 don’t care

크로스 될 경우 두 개를 or 연산으로 간략화

## 7-segment Display

seven segment decoder circuit

7개의 입력 → 출력 연결

0/1 입력

0이면 꺼지고 1이면 켜짐

카르노맵을 쓰지 않으면 모든 입력 단에 회로가 만들어져서 복잡한 회로가 만들어짐

→ 가르노맵으로 디코딩 맵 간략화

A가 1이 켜진걸로 카르노맵을 생성 → 식을 간략화

1. 4개를 먼저 묶어서 2개를 don’t care
2. 2개를 묶어서 1개를 don’t care
3. 모든 회로 or로 묶어줌

불대수 : 컴퓨터를 이루는 부품들에 대한 내용
