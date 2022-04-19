#계단을 올랐을 때 얻을 수 있는 총 점수의 최댓값 구하기
# 계단은 한 번에 한 계단씩 / 두 계단씩 오를 수 있음
#연속된 세 개의 계단을 모두 밟아서는 안된다.
# -> 한 계단을 올랐으면 다음번에는 두 계단을 올라야 함
#마지막 도착 계단은 반드시 밟아야 한다.
#dp[n]은 n번째 계단을 밟았을때까지의 점수의 최댓값
#지난번 계단 + 두칸 올랐을 경우와
#지난번 계단 + 한칸 올랐을 경우인데,
#지난번 계단 이전에 한칸을 올랐다면 그 이전에는 두칸을 올랐어야 하므로
#총 세칸 전 + 한칸 전 + 현재 계단이 된다.

# IndexError 코드
# n이 1,2일 경우 dp[2]가 존재할 수 x -> IndexError

# n = int(input())
# s = [0 for _ in range(n)]
# dp = [0 for _ in range(n)]

# for i in range(n):
#     s[i] = int(input())

# dp[0] = s[0]
# dp[1] = s[0]+s[1]
# #한칸+두칸 / 두칸+한칸 중 최댓값
# dp[2] = max(s[0]+s[2],s[1]+s[2])

# for i in range(3,n):
#     #두칸 + 현재 / 두칸 + 한칸 + 현재 최댓값
#     dp[i] = max(dp[i-2]+s[i],dp[i-3]+s[i-1]+s[i])

# print(dp[n-1])

# 수정된 코드
# n이 1,2일 때와 3이상일때로 나눔

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