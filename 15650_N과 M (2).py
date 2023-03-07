import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())

for j in combinations([i for i in range(1,n+1)],m):
    print(*j)