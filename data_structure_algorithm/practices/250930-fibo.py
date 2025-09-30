# 최적화
cache = [0]*1001

def fibo(x):
    if cache[x] != 0:
        return cache[x]
    
    # base case
    if x == 1 or x == 2:
        return 1
    
    # recursive case
    cache[x] = fibo(x-1) + fibo(x-2)
    return cache[x]

    # print(f"fibo({x}) running")
    # base case
    # if x == 0:
    #     return 0
    # if x == 1:
    #     return 1
    
    # # recursive case
    # if x > 1:
    #     return fibo(x - 1) + fibo(x - 2)
    # else:
    #     return fibo(x + 2) - fibo(x + 1)


if __name__ == "__main__":
    n = int(input())
    print(fibo(n))