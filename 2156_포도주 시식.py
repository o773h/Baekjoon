#연속으로 세 잔을 마실 수 없다.
#1<=n<=10000 이므로, n이 1,2일때는 그냥 다 마시면 된다.
#계단 문제와 비슷

n = int(input())
wine = []
dp = [0 for _ in range(n)]

for i in range(n):
    wine.append(int(input()))

dp[0] = wine[0]
if n>1:
    dp[1]=dp[0]+wine[1]
    if n>2:
        dp[2] = max(dp[1],wine[0]+wine[2],wine[1]+wine[2])
        for i in range(3,n):
            dp[i] = max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])

print(dp[-1])