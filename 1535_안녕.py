import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
m = list(map(int,sys.stdin.readline().split()))

dp = [(0,100)]

for i in range(n):
    new_dp = []
    for e in dp:
        if e[1]-l[i]>0:
            new_dp.append((e[0]+m[i],e[1]-l[i]))
        new_dp.append((e[0],e[1]))
    dp = new_dp

print(max(dp)[0])
