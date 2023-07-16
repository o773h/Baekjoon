import sys
from itertools import permutations

n = int(sys.stdin.readline())
nums_list = list(map(int,sys.stdin.readline().split()))

max_result = 0

for nums in permutations(nums_list,n):
    result = 0
    for i in range(1,n):
        result += abs(nums[i]-nums[i-1])
    
    max_result = max(max_result,result)

print(max_result)