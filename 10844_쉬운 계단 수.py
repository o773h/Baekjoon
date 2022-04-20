#1,2,3,4,5,6,7,8,9
#뒤에 앞 숫자보다 1 크거나 1 작거나 총 2가지 숫자가 올 수 있음
#하지만 앞에 숫자가 0인 경우에는 뒤에 1밖에 오지 못하고, 9인 경우에는 뒤에 8밖에 오지 못함
#9인 경우는 직전에 8인 경우 갯수이고, 0인 경우는 직전에 1인경우임

n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n)]

for i in range(1,10):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n-1])%1000000000)