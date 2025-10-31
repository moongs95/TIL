# Transformer-based Detector

## DETR
- Transformer 구조를 사용한 최초의 detector로, prior knowledge를 제거한 end-to-end 모델
- Transformer encoder-decoder를 통해 N개의 box 예측
- Hungarian algorithm과 bipartite matching loss를 통해 GT와 매칭하여 모델 학습
