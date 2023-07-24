import sys

word = sys.stdin.readline().rstrip()
devil = sys.stdin.readline().rstrip()
angel = sys.stdin.readline().rstrip()

dp = [[[0,0] for _ in range(len(word))] for _ in range(len(devil))]

for i in range(len(devil)):
    if word[0] == devil[i]:
        dp[i][0][0] = 1
    
    if word[0] == angel[i]:
        dp[i][0][1] = 1


for i in range(1,len(devil)):
    for j in range(1,len(word)):
        if word[j] == devil[i]:
            for k in range(i):
                dp[i][j][0] += dp[k][j-1][1]

        if word[j] == angel[i]:
            for k in range(i):
                dp[i][j][1] += dp[k][j-1][0]
            
result = 0
for i in range(len(devil)):
    result += dp[i][-1][0] + dp[i][-1][1]

print(result)