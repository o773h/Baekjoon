import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n)]
result = 0

if n<=2:
    result = 1
else:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3,n):
        dp[i] = dp[i-1] + dp[i-3]
    result = dp[-1]

print(result)