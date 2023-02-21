import sys

n,k = map(int,sys.stdin.readline().split())
lst = [[0 for _ in range(k+1)] for _ in range(n+1)]


for i in range(n+1):
    lst[i][0] = 1

for i in range(1,n+1):
    for j in range(1,k+1):
        lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

print(lst[n][k]%10007)