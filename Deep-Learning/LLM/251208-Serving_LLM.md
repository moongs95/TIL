# Serving LLM

- LLM 추론 최적화를 위해 사용되는 기술에 대한 이해
- 실제 LLM 서빙(서비스) 시 고려해야하는 부분에 대한 이해

## Introduction

- 모델 성능 향상을 위해 비약적으로 증가하는 모델 사이즈
- 성능과 함께 증가하는 모델 수요

### LLM 추론의 어려움

- 모델 사이즈(파라미터 수) 증가
- 더 많은 연산량, GPU 메모리, 에너지, 비용 필요
- Autoregressive, Generative model

### LLM 추론 과정

- Prefill and Decoding(generation)
- Prefill : 입력 프롬프트의 각 토큰에 대해 K/V 벡터 계산(KV 캐시 생성)
- Decode : 다음 토큰 생성(next token prediction), KV 캐시에 append

## LLM inference optimization techniques

### KV-Cache

- 토큰 생성 시 중복 계산 방지, 연산량에 제한을 둬서 긴 context에서도 추론이 가능해짐, 메모리 효율
- 메모리 요구량(naive) = Model weights + KV-Cache
- Memory trade-off
- Batch size 하락 : gpu util, throughput 낮아짐, latency(cost) 올라감
- Sequence length 하락 : 사용성 저하
- Precision 하락 : 모델 성능(품질) 저하
- 실 서비스 환경에서는 요구사항 파악이 필수

### Paged Attention

- KV-Cache 활용의 어려움: over-reservation - 요청이 생성할 sequence 길이를 예측할 수 없음, fragmentation(파편화) - 실제 남은 공간 충분해도 사용 못함
- 모델의 메모리를 좀 더 유연하게 해결
- OS에서 메모리를 관리하기 위해 사용하는 virtual memory와 paging 개념 도입
- Logical(개념적)/Physical(물리적) 메모리를 나누어 관리 -> 메모리는 불연속적인 공간에 할당(physically)
- block table을 통해 매핑 개념적으로는 연속적이기 때문에 메모리를 불연속적인 공간에 할당해도 연속적으로 느낌
- 동일한 prompt에 대한 kv-cache 공유 가능
- 다중 샘플링 예시(copy-on-write 방식 메모리 할당)
- 높은 throughput 달성

### Prefix caching

- 반복되는 프롬프트의 중복 연산을 방지
- 기존 계산된 kv-cache를 그대로 활용
- LLM 워크로드 상 동일한 prompt를 가진 요청이 반복됨
- 추가 kv-cache 할당 방지
- 중복 연산 방지 (gpu computing ↓)
- TTFT↓ (time-to-first-token)
- cache-hit가 없으면 gain도 없음
- Generation 성능에는 영향 X

### Countinuous batching

- Problem of static-batch inference : llm은 시퀀스가 다르기 때문에 메모리가 남는 공간이 생긴다
- prefill 다 채우로 decoding을 했을 때 decode가 일찍 끝난 곳은 메모리가 낭비됨
- 끝났으면 다음거를 바로 처리할 수 있도록 함

### Chunked prefill

- Prefill stragey : prefill first
- 토큰 생성을 일시 중단하고, 새로운 요청의 prefill 과정 먼저 수행 -> 일시 중단되면 사용성이 떨어짐
- 이후 생성 과정을 배치 처리할 수 있음
- TTFT 최적화 가능
- 이전 요청은 prefill 과정과 같이 batching되어 한 개의 토큰 생성 가능

---

- Better strategy : chunked-prefill
- Prefill 과정을 정해진 길이(chunk size)만큼 여러 개의 chunk로 나누어 실행
- Prefill 수행 중 응답 생성이 중단되는 대신, 느려짐
- Compute bound, I/O bound precess를 병렬적으로 수행, 리소스 활용 극대화
- Chunk 크기만큼 처리할 때 효율이 가장 높음

---

- Chunk size trade-off
● Chunk size ↑ (한 번에 처리하는 프롬프트=토큰 수 많음)
○ Decode interrupt ↓ → 오버헤드 ↓
○ GPU 연산 효율 ↑ → throughput ↑
○ Decode 대기 시간 ↑ → TTFT ↑
● Chunk size ↓ (한 번에 처리하는 프롬프트=토큰 수 적음)
○ Decode interrupt ↑ → 오버헤드 ↑
○ GPU 연산 효율 ↓ → throughput ↓
○ Decode 대기 시간 ↑ → TTFT ↓
● 상황에 따라 적절한 chunk size 설정 필요

### LLM througtput metrics

- TTFT(Time to first token) : 첫 번째 토큰 생성까지 걸리는 시간
- TTFT = prefill + decode(one time)
- 응답을 end-user에게 바로 보여주는 경우, 사용성에 중요한 지표

---

- Latency : 요청 처리가 완료될 때까지 걸리는 시간
- 일반적으로 대부분의 서비스에서 모니터링하는 지표
- LLM의 경우, 입력&출력 토큰에 따라 Latency 편차가 커서 추론 성능을 트래킹하기 적절하지 않음
- 추론 시간 분포를 분석하기 위해 사용 가능
- 서비스에서 timeout이 발생하지 않는지 모니터링 필요

---

- TPS(Tokens per second) : 초당 토큰 생성 수
- 관심사에 따라 prefill 시간을 포함 여부 결정
- 사용자가 체감하는 생성 성능은 prefill 시간을 제외한 TPS

---

- TPOT/ITL(Time Per Output Token/Inter-token Latency)
- 토큰 하나를 생성하는데 걸리는 시간
- PTOP/ITL = (1 / TPS)

---

- Total input / output tokens
- TPS & TPOT는 개별 요청의 성능 지표를 분석
- 토큰 처리량을 별도로 확인하는게 시스템 성능 파악에 도움이 됨

---

- Infra & System Metrics
● KV Cache 사용량
● GPU util 
● 에러 비율 
● Queue 대기 시간
● CPU / RAM: GPU 외부 리소스가 병목이 되는지 확인

---

- LLM 추론 성능 변수
● GPU 연산 성능
● GPU 메모리 크기 / 대역폭
●모델 아키텍처 (파라미터 수, 레이어 구성 등)
●요청 워크로드 (입력 프롬프트, 생성 토큰 길이, 동시 요청 수, 요청 길이 분포)
●내부 스케줄링 구현 및 정책 ( ex - prefill chunk size)
→ 변수가 다양하고, 워크로드를 예상하기 힘듦
→ 온라인 환경에서 지표 모니터링이 매우 중요
