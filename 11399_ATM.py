import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
n_list.sort()
sum = 0
for i in range(n):
    sum+=n_list[i]*(n-i)

print(sum)