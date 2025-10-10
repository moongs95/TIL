# 그람-슈미트 과정

- 임의의 갯수, 차원의 벡터 입력 -> 임의의 갯수, 차원의 벡터 출력(서로 orthnormal)
- 갯수와 차원은 같아야 함
- orthnormal : unit vector, orthogonal 성질 두 개 다 만족

## 2개의 벡터

- 2차원 벡터 2개를 입력 -> 2차원 벡터 2개를 출력(서로 orthnormal)

### 방법

1. v1 = u1을 normalization → ||v1|| = 1
2. v2 프라임 = u2 - u2를 v1에 projection시킨 값(벡터의 분해 사용) → v1ㅗv2프라임
3. v2 = v2프라임을 normalization → v2ㅗv1, ||v2|| = 1

## 3개의 벡터

- 3차원 벡터 3개 입력 → 3차원 벡터 3개 출력(otrhonormal)

### 방법

1. v1 = u1의 정규화 → ||v1|| = 1
2. v2프라임 = u2 - v1에 projection된 u2 → v1ㅗv2프라임
3. v2 = v2프라임의 정규화(v2프라임에 v2프라임의 놈을 나눠줌) → v2ㅗv1, ||v2|| = 1
4. v3프라임 = u3 - u3를 v1에 projection한 벡터 - u3를 v2에 projection한 벡터 -> v3프라임ㅗv1, v3프라임ㅗv2
5. v3 = v3프라임의 정규화(v3프라임에 v3프라임의 놈을 나눠줌) → ||v1|| = 1, 모두 서로 수직(서로의 내적이 0)

## 일반화

- n차원으로 일반화
- Gram-Schmidt algorithm is a way of finding a set of two or more vectors that are perpendicular to each other.
- 모든 프로젝션을 빼줌 ⇒ 평행한 성분을 없애고 서로 수직이 되도록 만들기 위해서
- 그람슈미트 프로세스는 k개의 벡터를 입력받고 orthnormal한 벡터를 찾아냄
- how? projection을 빼주고 정규화를 반복(unit vector화)
- 중요! method of constructing an **orthonormal basis**
