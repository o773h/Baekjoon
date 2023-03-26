import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

dp = a[:]

for i in range(1,n):
    for j in range(0,i):
        if a[j]<a[i]:
            dp[i] = max(dp[j]+a[i],dp[i])

print(max(dp))