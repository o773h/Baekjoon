import sys
from collections import defaultdict

t = int(sys.stdin.readline())

for _ in range(t):
    clothes = defaultdict(int)
    n = int(sys.stdin.readline())
    for _ in range(n):
        a,b = sys.stdin.readline().split()
        clothes[b]+=1

    result = 1
    for i in clothes.values():
        result *= (i+1)

    print(result-1)