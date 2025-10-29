# Transformer 이해하기

## 01 Why Transformer?

### 1.1 Transformer

- 최근 **Computer Vision** 분야에서도 Transformer backbone이 주류가 됨  
- **NLP의 Long-term dependency 문제**를 해결하기 위해 고안됨  

#### Long-term Dependency 문제
- 기존 모델들은 sequence data를 순차적으로 처리 → 긴 문장에서 정보 손실 발생  
- 예시:  
  - (a) The animal didn’t cross the street because it was too **tired**.  
  - (b) The animal didn’t cross the street because it was too **wide**.  
  - 문맥에 따라 ‘it’이 **animal** 또는 **street**을 의미  

#### Attention 개념
- 단어 간의 연관성을 반영해 중요한 정보를 집중적으로 학습  
- Long-term dependency와 context 관계를 반영할 수 있음  

#### CNN의 한계점
- **Long-range dependency**: 멀리 떨어진 객체 간 관계 학습이 어려움  
- **Attention 부족**: 이미지 내 object 간 상호 관계 파악 어려움  
- → Transformer가 NLP에서 해결한 메커니즘을 Vision에 적용 → **ViT (Vision Transformer)** 등장  

---

## 02 Transformer의 구조

### 2.1 Transformer Pipeline

#### Input: Sentence to Embedding
- 문장을 컴퓨터가 이해할 수 있는 **벡터(embedding)** 형태로 변환  
- **Tokenization**: 문장을 의미 단위(token)로 분리  
- **Word Embedding**: 각 token을 벡터로 변환 (학습 가능한 값)

#### Positional Encoding
- 단어의 **위치 정보를 embedding에 추가**  
- 같은 단어라도 위치에 따라 의미가 달라질 수 있음  
- 최근에는 positional encoding도 **학습 가능한 파라미터**로 설정  

---

### Self-Attention
- 입력 embedding을 **Query(Q)**, **Key(K)**, **Value(V)**로 변환  
  - Query: 관심 있는 단어  
  - Key: 모든 단어  
  - Value: 단어의 정보  
- Query-Key 내적 → Attention Score 계산 → Value에 가중합 적용  
- Hidden size가 커질수록 gradient 불안정 → **Scaled Dot Product Attention** 사용  

#### Multi-Head Attention
- 여러 attention head를 통해 다양한 context 학습  
- 더 복잡하고 풍부한 관계 파악 가능  

#### Feed Forward + Add & Norm
- Attention 출력에 원본 embedding을 더하고 정규화  
- 이후 fully connected layer 통과  
- Multi-head attention + Feed Forward → **Encoder Block**  
- Encoder를 여러 층 쌓아 깊은 Transformer 구성  

---

# Backbone 이해하기: Transformer

## 01 Transformer와 CNN

### 1.1 Transformer

#### Transformer의 특징
- 긴 문장의 **long-term dependency 문제 해결**  
- **Self-Attention**으로 단어 간 연관성 및 중요도 학습  
- 연산 효율성과 확장성이 높으며, 데이터가 커져도 성능 포화 X  
- **LLM (Large Language Model)** 발전의 기반이 됨  

#### Vision에서의 Transformer
- CNN은 receptive field를 넓혀도 long-range dependency 해결 불가  
- → 픽셀을 token으로 간주해 attention 계산  
- 하지만 픽셀 수가 많을수록 연산량이 폭증  

---

## 02 Vision Transformer (ViT)

### 2.1 Introduction

- 모든 픽셀에 대한 attention은 비효율적  
- → N×N **patch 단위로 token 생성**  
- “An Image is Worth 16×16 Words”  

#### ViT 파이프라인
1. **Image → Patch → Embedding → Transformer Encoder → Task Head**  
2. Patch 크기: (P, P), N=HW/P²  
3. Flatten 후 Linear Projection (D 차원 feature)  
4. **[CLS] Token** 추가: 이미지 전체 대표  
5. **Positional Embedding** 추가: 위치 정보 반영  
6. Transformer Encoder 적용  
7. **MLP Head**: classification 수행  

#### 결과
- CNN과 유사한 성능  
- Transformer를 이미지 처리에 성공적으로 적용했다는 점에 의의  

#### 한계점
- CNN의 inductive bias (Locality, Translation equivariance 등) 부재  
- Attention은 global 관계에 집중 → **local feature 학습 어려움**  
- Patch 과정에서 **neighborhood 구조 파괴**  

---

## 03 Swin Transformer

### 3.1 Introduction

#### ViT의 문제점
- 해상도↑ → Self-Attention 계산량 급증  
- Segmentation/Detection에서는 세밀한 표현력 부족  
- CNN의 inductive bias(국소성, 계층 구조) 사라짐  

→ **Swin Transformer (Hierarchical Vision Transformer using Shifted Windows)** 제안  

#### 특징
- **Hierarchical 구조**: 작은 patch → 큰 patch로 점진적 병합  
- 다양한 크기의 객체 처리에 유리  
- Segmentation, Object Detection 등에서 효과적  

---

### 3.2 Methods

#### Patch Partitioning
- 이미지를 (P×P) patch로 분할 (RGB 채널 concat → 4×4×3=48차원 등)  

#### Linear Embedding
- ViT처럼 linear projection 적용, **CLS token 없음**

#### Relative Position Bias
- 절대 위치 대신 **patch 간 상대적 거리**에 집중  
- Attention 계산 시 relative bias term 추가  

#### Self-Attention 구조
- **W-MSA**: Window-based Multi-head Self-Attention  
- **SW-MSA**: Shifted Window Multi-head Self-Attention  

#### Shifted Window
- Window 내 patch끼리만 attention 계산 → 효율성↑  
- 인접 window 간 연결 끊김 문제 발생 → **Window를 절반만큼 shift**  
- Window 간 관계 복원 및 연산량 절감  

#### Cyclic Shift
- Shift 시 이미지 가장자리 patch 손실 방지  
- 이미지 전체를 cyclic shift → 누락 부분을 masking 처리  

#### Patch Merging
- 인접 2×2 patch를 병합 → dimension 4C → Linear Layer로 2C로 조정  
- Channel-wise merging  

#### Computational Complexity
- 기존 모든 patch 간 attention 대비  
- **Window 내 attention만 계산**하여 계산량 크게 감소  

---

### 3.3 Results

- Object Detection 등 다양한 Vision Task에서 우수한 성능  
- CNN의 효율성과 Transformer의 표현력을 모두 갖춘 구조  

