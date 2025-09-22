# 순환과 반복, 피보나치 수열 그리고 하노이 탑

## 순환

- 알고리즘이나 함수가 수행 도중에 자기 자신을 다시 호출하여 문제를 해결하는 기법
- 정의 자체가 순환적으로 되어 있는 경우에 적합
- 팩토리얼

```C
double power(double x, int n)
{
	if(n==0) return 1;
	else if((n%2) == 0)
		return power(x*x, n/2);
	else return x*power(x*x, (n-1)/2);
}
```


## 피보나치 수열

- 순환 호출을 사용하면 비효율적인 예시
- 같은 항이 중복해서 계산
- n이 커지면 더 심해짐

```C
int fib_iter(int n)
{
  if(n==0) return 0;
  if(n==1) return 1;

  int pp = 0;
  int p = 1;
  int result = 0;

  for (int i = 2;i <= n; i++){
    result = p + pp;
    pp = p;
    p = result;
  }
  retur result;
}
```

## 하노이 탑

- 막대 A에 쌓여 있는 원판 n개를 막대 C로 옮기는 것
- 한 번에 하나의 원판만 이동
- 맨 위에 있는 원판만 이동
- 크기가 작은 원판 위에 큰 원판이 쌓일 수 없음
- 중간의 막대 임시적으로 이용 가능

```C
// 막대 from에 쌓여있는 n개의 원판을 막대 tmp를 사용하여 막대 to로 // 옮긴다.
void hanoi_tower(int n, char from, char tmp, char to)
{
  if(n==1){
    from에서 to로 원판을 옮긴다.
  }
  else{
    hanoi_tower(n-1, from, to, tmp);
    from에 있는 한 개의 원판을 to로 옮긴다.
    hanoi_tower(n-1, tmp, from, to);
  }
```
