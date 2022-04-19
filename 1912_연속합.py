# 연속합 구하기
# 연속된 몇개의 수를 선택해서 구할 수 있는 합 중 최댓값 구하기

n = int(input())
num_list = list(map(int,input().split()))

dp=[0 for _ in range(n)]

dp[0]=num_list[0]

for i in range(1,n):
    # 새로 시작해서 연속합 구하기 / 이전값과 더하여 연속합 구하기
    dp[i] = max(num_list[i],dp[i-1]+num_list[i])

print(max(dp))