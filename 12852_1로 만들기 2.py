import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]
parent=[0 for _ in range(n+1)]

for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    parent[i] = i-1

    if i%3==0:
        if dp[i] > dp[i//3]+1:
            dp[i] = dp[i//3]+1
            parent[i] = i//3
            
    if i%2==0:
        if dp[i] > dp[i//2]+1:
            dp[i] = dp[i//2]+1
            parent[i] = i//2

print(dp[n])
p = n
while p!=1:
    print(p,end=' ')
    p = parent[p]
print(1)