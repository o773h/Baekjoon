import sys

max_sum = 0
idx = 0
for i in range(1,6):
    s = sum(map(int,sys.stdin.readline().split()))
    if s >max_sum:
        max_sum = s
        idx = i

print(idx,max_sum)