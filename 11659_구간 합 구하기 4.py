import sys

n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[i] + nums[i])

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    print(prefix_sum[j]-prefix_sum[i-1])