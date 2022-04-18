n = int(input())
s = [0 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    s[i] = int(input())

dp[0] = s[0]
if n>1:
    dp[1] = s[0]+s[1]
    #한칸+두칸 / 두칸+한칸 중 최댓값
    if n>2:
        dp[2] = max(s[0]+s[2],s[1]+s[2])

        for i in range(3,n):
            #두칸 + 현재 / 두칸 + 한칸 + 현재 최댓값
            dp[i] = max(dp[i-2]+s[i],dp[i-3]+s[i-1]+s[i])

print(dp[n-1])