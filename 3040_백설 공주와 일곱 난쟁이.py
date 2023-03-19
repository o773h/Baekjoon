import sys
from itertools import combinations

nums = []
for _ in range(9):
    nums.append(int(sys.stdin.readline()))

for comb in combinations(nums,7):
    if sum(comb)==100:
        print(*comb,sep='\n')