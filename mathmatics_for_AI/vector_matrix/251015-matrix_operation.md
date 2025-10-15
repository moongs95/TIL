# 행렬(Matrix) 요약 정리

## 📘 1. 행렬의 정의
- 행렬(Matrix)은 **수를 직사각형 형태로 배열한 수학적 객체**
- **1차 텐서 = 벡터**, **2차 텐서 = 행렬**
- 행렬은 여러 **수직한 축의 개수(차원)** 를 가짐

---

## 🧮 2. 행렬의 표현
- 일반적으로 **대문자**로 표현 (예: A, B, C)
- 행렬의 원소는 **스칼라(scalar)** 값이며, **보통 소문자 normal font**로 표시  
  예시:
A = [a\_ij]

여기서 i는 행(row), j는 열(column)을 의미

---

## 🧭 3. 행렬의 모양
- 행이 m개, 열이 n개이면 **m×n 행렬(matrix)**
A ∈ R^(m×n)


---

## 🧱 4. 행벡터와 열벡터
- **Row vector (행벡터)** → 1×n 행렬  
- **Column vector (열벡터)** → n×1 행렬  
- 보통 벡터는 **column vector**로 표현

---

## 🧩 5. 행렬을 벡터 배열로 표현
- m×n 행렬은 n차원 row vector m개를 **세로로 쌓은(vertical stacking)** 형태  
- 또는 column vector n개를 **가로로 쌓은(horizontal stacking)** 형태로 볼 수도 있음

---

## 🧾 6. 행과 열의 표현법
- `[A]ij` : i행 j열의 원소 (scalar)  
- `[A]i*` : i번째 행 (row vector)  
- `[A]*j` : j번째 열 (column vector)

---

## 🧱 7. 행렬의 종류

### (1) 모양에 따른 구분
| 종류 | 설명 |
|------|------|
| **Row vector** | 행 1개 |
| **Column vector** | 열 1개 |
| **Square matrix** | 행과 열의 수가 같은 행렬 |
| **Rectangular matrix** | 행과 열의 수가 다른 행렬 |

---

### (2) 원소에 따른 구분
| 종류 | 설명 |
|------|------|
| **Zero matrix (0행렬)** | 모든 원소가 0 |
| **Identity matrix (항등행렬)** | 주대각선(main diagonal)은 1, 나머지는 0 |
| **Diagonal matrix** | 대각선 이외의 원소가 0 |
| **Triangular matrix** | 위/아래 삼각형 형태 (Upper / Lower) |

---

## ➕ 8. 행렬의 연산
행렬에서 가능한 기본 연산:
- 덧셈(Addition)
- 뺄셈(Subtraction)
- 스칼라 곱(Scalar Multiplication)
- 전치(Transpose)
- 행렬 곱(Matrix Multiplication)

---

## 🔹 9. 행렬의 덧셈과 뺄셈
- 같은 크기의 행렬만 연산 가능  
- 원소별로 더하거나 뺌
(A ± B)\_ij = a\_ij ± b\_ij


### 대수적 특징
| 성질 | 수식 |
|------|------|
| 교환법칙 | A + B = B + A |
| 결합법칙 | (A + B) + C = A + (B + C) |
| 항등원 | A + 0 = A |
| 역원 | A + (−A) = 0 |

---

## 🔸 10. 스칼라 곱 (Scalar Multiplication)
- 행렬의 모든 원소에 스칼라 k를 곱함
(kA)\_ij = k * a\_ij


### 대수적 특징
| 성질 | 수식 |
|------|------|
| 결합법칙 | k(lA) = (kl)A |
| 분배법칙 | (k+l)A = kA + lA,  k(A+B) = kA + kB |
| 항등원 | 1A = A |

---

## 🔄 11. 행렬의 전치 (Transpose)
- **행과 열을 맞바꾸는 연산**
(A^T)\_ij = A\_ji

- 시각적으로 **main diagonal** 을 기준으로 대칭

### 전치의 특징
| 성질 | 수식 |
|------|------|
| 전치의 전치 | (A^T)^T = A |
| 덧셈의 전치 | (A + B)^T = A^T + B^T |
| 스칼라 곱의 전치 | (kA)^T = kA^T |
| 곱의 전치 | (AB)^T = B^T A^T |
| 항등·대각행렬 | I^T = I, D^T = D |

---

## ✴️ 12. 행렬의 곱셈 (Matrix Multiplication)

### 기본 정의
C = A × B
C\_ij = Σ (A\_ik × B\_kj)

즉,  
A의 i번째 **행(row)** 과 B의 j번째 **열(column)** 을 내적(dot product)

### 곱셈 조건
- A: (m×n), B: (n×p) → AB: (m×p)
- 즉, **앞 행렬의 열 수 = 뒤 행렬의 행 수**

---

### 곱셈 형태별 결과
| 연산 | 결과 형태 |
|------|------------|
| Row × Matrix | Row vector |
| Matrix × Column | Column vector |
| Row × Column | Scalar (내적 결과) |

---

### 대수적 특징
| 성질 | 수식 |
|------|------|
| 결합법칙 | (AB)C = A(BC) |
| 분배법칙 | A(B ± C) = AB ± AC |
| 항등원 | AI = IA = A |
| ⚠️ 교환법칙 | **성립하지 않음! (AB ≠ BA)** |

---

## 💡 13. 행렬과 벡터의 곱
- 행렬 × 벡터 = 각 행(row)과 벡터의 **내적(dot product)** 결과를 모은 벡터  
y = A x
y\_i = Σ a\_ij x\_j

- 즉, 행렬 곱은 **벡터 내적의 확장**

---

## ✅ 핵심 요약

| 주제 | 핵심 내용 |
|------|------------|
| 행렬의 정의 | 수를 직사각형으로 배열한 2차 텐서 |
| 행렬의 기본 표현 | A ∈ R^(m×n), a\_ij는 스칼라 원소 |
| 주요 연산 | 덧셈, 뺄셈, 스칼라 곱, 전치, 행렬 곱 |
| 전치의 특징 | (AB)^T = B^T A^T |
| 곱셈 조건 | 앞 행렬의 열 = 뒤 행렬의 행 |
| 곱셈의 핵심 | 내적의 확장 형태 |
| 교환법칙 | ❌ 성립하지 않음 |

---
