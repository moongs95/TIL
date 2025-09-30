cache = [0] * 1001

def hanoi(n):
    if cache[n] != 0:
        return cache[n]
    
    # base case
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    # recursive case
    cache[n] = 2 * hanoi(n - 1) + 1 
    return cache[n]


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    answer = hanoi(n) - hanoi(k) + hanoi(k-1)
    print(answer)
    