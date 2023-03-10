import sys

chess = [1,1,2,2,2,8]
lst = list(map(int,sys.stdin.readline().split()))

for i in range(6):
    print(chess[i]-lst[i],end=' ')