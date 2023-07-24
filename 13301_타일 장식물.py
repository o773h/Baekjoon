import sys

memo = {0:1,1:1}
def fibo(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

n = int(sys.stdin.readline())
print(2*(fibo(n)+fibo(n-1)))