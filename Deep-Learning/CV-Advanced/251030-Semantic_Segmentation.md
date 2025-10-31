# Semantic Segmentation

## Semantic Segmentation Process
- 이미지에서 각각의 픽셀마다 클래스 레이블을 예측
- 즉, 클래스 레이블만으로 이루어진 출력 이미지를 얻음

## FCN (Fully Convolutional Network)
- Semantic segmentation의 가장 기초가 되는 encoder-decoder 모델
- 기존 이미지 분류 백본에서 fc layer 대신 1x1 convolution과 transposed convolution을 사용

# CNN-based Segmentation: U-Net

## U-Net
- Contracting path와 expanding path가 대칭적인 U자인 인코더-디코더 구조
- 같은 level의 layer에서 skip connection을 사용
- Low level feature map과 high level feature map 함께 디코딩

## U-Net ++
- 기존 U-Net의 한계점은 동일한 깊이의 인코더, 디코더만 skip connection
- 이를 해결하기 위해 skip connection path 개선, deep supervision 등의 방법 사용

## U-Net 3+
- U-Net ++의 경우 복잡하고 많은 skip connection으로 인해 parameter 수↑,  memory ↑
- Full-scale skip connections, full-scale deep supervision, classification-guided module을 이용해 개선

## Eff-UNet
- 인코더 백본으로 EfficientNet-b7을 채택
- EfficientNet-b7 백본을 U-Net 구조로 구성하여 skip connection 적용

# CNN-based Segmentation: DeepLab

## DeepLab
- Semantic Segmentation에서 3가지 Challenge가 존재함
- Reduced feature resolution → Atrous convolution
- Existence of objects at multiple scales → Atrous spatial pyramid pooling (ASPP)
- Reduced localization accuracy due to DCNN invariance → Conditional Random Field (CRF)
- Atrous convolution은 이후 여러 논문에서 기본 모듈이 됨

# Transformer-based Segmentation

## SETR
- Transformer를 semantic segmentation task에 성공적으로 최초 적용
- Encoder는  ViT 사용
- 디코더는 SETR-Naive, SETR-PUP, SETR-MLA를 제안
- ViT를 그대로 사용하여 파라미터 수가 많고, image resolution이 줄어들지 않아 연산의 복잡도가 올라감

## SegFormer
- SETR의 한계점을 개선한 모델
- Transformer 기반의 모델 중에서 베이스라인으로 많이 이용됨
- 효율적인 연산을 위해 attention 고도화, 인코더 개선, 가벼운 MLP 디코더 사용

## SegFormer Encoder
- Hierarchical transformer block
- Local continuity를 높이기 위해 overlap patch merging 적용
- 효율적인 연산을 위해 efficient self-attention 사용
- Positional encoding을 Mix-FFN으로 대체

## SegFormer Decoder
- MLP layer로만 구성돼 가벼움
- 4개의 transformer block의 feature map으로부터 segmentation mask 생성
