import sys
import math

n,w,h = map(int,sys.stdin.readline().split())

cross = math.sqrt(w**2 + h**2)

for _ in range(n):
    i = int(sys.stdin.readline())
    if cross>=i:
        print("DA")
    else:
        print("NE")