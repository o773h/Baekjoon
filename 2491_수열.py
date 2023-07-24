import sys

n = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split()))
dp1 = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]

for i in range(1,n):
    if num[i] > num[i-1]:
            dp1[i] = max(dp1[i], dp1[i-1]+1)
    elif num[i] < num[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1]+1)
    else:
        dp1[i] = max(dp1[i], dp1[i-1]+1)
        dp2[i] = max(dp2[i], dp2[i-1]+1)
    
print(max(max(dp1),max(dp2)))