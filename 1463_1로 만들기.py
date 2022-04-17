# 다이나믹 프로그래밍(DP)
# n번째 연산을 하는 최솟값은 n-1번째 최솟값의 +1
# -1을 했을 경우, 2로 나누었을 경우, 3으로 나누었을 경우를 했을 때 중, 최소 횟수를 구해야 함.
# dp 리스트는 정수n이 1이 되기 위한 최소 횟수임
# dp[n] = n이 1이 되기 위한 최소 횟수

n = int(input())

dp = [0 for _ in range(n+1)]


for i in range(2,n+1):
    dp[i] = dp[i-1] + 1

    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)

print(dp[n])