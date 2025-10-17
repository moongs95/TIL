# From AlexNet to ChatGPT

## 01 딥러닝의 도래 | Emergence of Deep Learning

### LeNet-5부터 AlexNet까지

**LeNet-5 (1998)**  
1998년 Yann LeCun에 의해 제안된 모델로, 손글씨 숫자(MNIST)를 인식하기 위해 설계된 최초의 합성곱 신경망 구조. LeNet-5 모델은 초기 CNN으로 다가올 딥러닝의 가능성을 보여줌.

🔗 https://ko.wikipedia.org/wiki/MNIST_%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4

---

**ImageNet Large Scale Visual Recognition Challenge (ILSVRC)**  
ImageNet 데이터셋은 수백만 개의 라벨링된 이미지로 구성된 대규모 시각 데이터베이스. 2010년부터 2017년까지 진행된 ILSVRC 대회는 딥러닝 발전의 주요 촉매 역할을 함.

- 이미지 내 객체 분류 성능을 평가  
- 클래스 수가 매우 많음  
- 딥러닝 기술 발전의 결정적 전환점  

2017년 이후 종료된 이유: 딥러닝 모델이 사람보다 더 높은 정확도를 기록했기 때문.  
특히 **2012년 AlexNet**이 딥러닝 전성기의 문을 열었음.

🔗 https://theaisummer.com/cnn-architectures/

---

**AlexNet (2012)**  
ImageNet 대회에서 압도적인 성능으로 우승하며 딥러닝 시대를 연 모델.  
GPU 병렬 처리, ReLU 활성화 함수, Dropout, Data Augmentation 등의 기술을 도입.

- GPU 두 개를 병렬로 활용하여 대규모 학습 수행  
- 기존 모델보다 월등한 성능 달성  
- 딥러닝의 대중화를 이끈 역사적 모델  

---

## 02 딥러닝의 발전 | Advancements in Deep Learning

### VGGNet부터 Transformer까지

**VGG (2014)**  
ImageNet 대회에서 좋은 성적을 낸 모델로, 깊은 네트워크가 성능 향상에 기여함을 입증.  
16층, 19층 버전이 존재하며 3×3 합성곱 필터를 일관되게 사용.

- 단순하고 규칙적인 구조  
- 네트워크 깊이를 확장하여 성능 향상  

🔗 https://towardsdatascience.com/understanding-and-coding-a-resnet-in-keras-446d7ff84d33  
🔗 https://wikidocs.net/164796

---

**GoogLeNet (2015)**  
Inception 모듈을 도입하여 다양한 크기의 합성곱과 풀링을 결합, 파라미터 수를 대폭 줄이면서 성능을 높임.  

- 다양한 필터 크기의 병렬 처리  
- 효율적인 구조 설계  
- 연산량 감소 및 성능 향상  

🔗 https://bskyvision.com/entry/CNN-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%93%A4-GoogLeNetinception-v1%EC%9D%98-%EA%B5%AC%EC%A1%B0

---

**Generative Adversarial Networks (GAN, 2014)**  
Ian Goodfellow가 제안한 생성 모델.  
생성자(Generator)와 판별자(Discriminator)를 경쟁시켜 진짜 같은 데이터를 생성.

- Generator: 가짜 데이터를 생성  
- Discriminator: 진짜와 가짜를 구별  
- 상호 경쟁을 통해 점점 진짜 같은 데이터 생성  

→ 생성 모델링의 혁신적 전환점.

---

**ResNet (2015)**  
Residual Connection(잔차 연결)을 도입하여 깊은 네트워크 학습의 기울기 소실 문제 해결.  
"skip connection"을 통해 입력 x를 직접 다음 층으로 전달하여 학습 안정성 향상.

- f(x) + x 구조로 학습 효율 개선  
- 매우 깊은 네트워크 학습 가능  
- 과적합 없이 정확도 향상  

ResNet은 2015 ILSVRC 우승 모델로, 사람보다 높은 인식 정확도를 달성.  
이후 대회는 공식적으로 종료됨.

🔗 https://medium.com/analytics-vidhya/deep-residual-learning-for-image-recognition-resnet-94a9c71334c9  
🔗 https://www.researchgate.net/figure/Main-breakthroughs-in-ImageNet-image-classification-challenge_fig1_335937276

---

**Sequence-to-Sequence (Seq2Seq, 2014)**  
입력 시퀀스를 다른 시퀀스로 변환하는 인코더-디코더 구조.  
기계 번역 등 자연어 처리에 주로 사용됨.

- 인코더: 입력 시퀀스를 하나의 Context Vector로 압축  
- 디코더: Context Vector를 이용해 출력 시퀀스 생성  
- Transformer의 전신이 되는 구조  

---

**Transformer (2017)**  
논문 *“Attention Is All You Need”* 에서 제안된 모델.  
RNN/LSTM 대신 Self-Attention을 이용해 시퀀스 데이터를 처리.

- 병렬 연산 가능 → 학습 속도 향상  
- 문맥 간 관계 학습에 탁월  
- 대부분의 최신 NLP 모델의 기반 구조  

🔗 https://nlp.seas.harvard.edu/2018/04/03/attention.html

---

## 03 최신 딥러닝 동향 | Latest Trends in Deep Learning

### BERT부터 ChatGPT까지

**BERT (2018)**  
Bidirectional Encoder Representations from Transformers.  
양방향 Transformer 인코더를 사용하여 문맥 이해 능력을 극대화.

- 빈칸 채우기(Masked Language Model) 방식  
- Self-supervised 학습  
- 다양한 NLP 과제에 파인튜닝으로 적용 가능  

🔗 https://wikidocs.net/115055

---

**GPT (2018)**  
Generative Pre-trained Transformer.  
Transformer의 디코더만을 사용하여 대규모 언어 모델을 사전학습(pre-training) 후, 특정 태스크에 맞게 미세조정(fine-tuning).

- 대규모 데이터 기반 비지도 학습  
- GPT → GPT-2 → GPT-3 → GPT-4로 발전  
- In-context learning의 핵심 구조  

🔗 https://jalammar.github.io/how-gpt3-works-visualizations-animations/

---

**EfficientNet (2019)**  
모델의 깊이, 너비, 해상도를 동시에 스케일링하는 효율적 CNN 구조 제안.

- 적은 파라미터로 높은 정확도  
- 세 가지 축(Depth, Width, Resolution) 동시 최적화  
- 효율성과 정확도의 균형을 달성  

---

**Vision Transformer (ViT, 2020)**  
Transformer를 이미지 인식에 적용.  
이미지를 패치로 분할하여 토큰처럼 처리.

- CNN 없이 Transformer만으로 이미지 분류 가능  
- 대규모 데이터에서 탁월한 성능  
- NLP와 CV 간 경계를 허물음  

---

**ChatGPT (2022)**  
OpenAI의 GPT 구조를 기반으로 한 대화형 AI 모델.  
사전 학습 + 대화 데이터로 미세조정되어 자연스러운 대화 수행.

- 문맥 유지 및 논리적 대화 가능  
- 다양한 분야의 질문에 대응  
- GPT-3.5, GPT-4 기반 상용화  

codex: 코드 데이터로 학습된 GPT 모델 → 논리적 추론 능력 향상.

---

**Large Language Models (LLMs)**  
대형 언어 모델 진영은 공개형(Open LLM)과 비공개형(Closed LLM)으로 나뉨.

- Meta의 LLaMA 시리즈 → 완전 공개  
- OpenLLM 진영은 빠르게 기술 격차를 좁히는 중  

---

**Open LLM Leaderboard**  
오픈소스 LLM 성능을 비교·평가하는 플랫폼.  
Eleuther AI 평가 스위트를 기반으로 점수를 계산.

🔗 https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

---

**Papers with Code**  
최신 딥러닝 모델과 논문, 데이터셋을 추적할 수 있는 플랫폼.  
연구 트렌드를 빠르게 파악할 수 있음.

🔗 https://paperswithcode.com/

