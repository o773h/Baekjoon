import sys

n = int(sys.stdin.readline())
dp = [0,1]

for i in range(2,n+1):
    j = 1
    min_value = 123456789
    while i>=j**2:
        min_value = min(min_value,dp[i-j**2])
        j+=1
    dp.append(min_value+1)

print(dp[n])