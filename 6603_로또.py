import sys
from itertools import combinations

while True:
    lst = list(map(int,sys.stdin.readline().split()))
    if lst[0]==0:
        break

    for i in combinations(lst[1:],6):
        print(*i)
    print()