import sys
from itertools import permutations

n,k = map(int,sys.stdin.readline().split())
n_list = list(map(lambda x : x-k , map(int,sys.stdin.readline().split())))

result = 0
for kit in permutations(n_list,n):
    sum = 0
    flag = True
    for k in kit:
        sum +=k
        if sum<0:
            flag = False
            break
    if flag:
        result+=1

print(result)