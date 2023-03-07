import sys
from itertools import combinations_with_replacement as comb

n,m = map(int,sys.stdin.readline().split())

for j in comb([i for i in range(1,n+1)],m):
    print(*j)