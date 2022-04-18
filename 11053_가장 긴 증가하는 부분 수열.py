a = int(input())
a_list = list(map(int,input().split()))

dp = [1 for _ in range(a)]

for i in range(a):
    for j in range(i):
        if a_list[i]>a_list[j] and dp[i]<=dp[j]:
            dp[i]=dp[j]
            dp[i]+=1

print(max(dp))