import sys

n,m = map(int,sys.stdin.readline().split())

grid = []

for _ in range(n):
    grid.append(sys.stdin.readline().rstrip())

for i in grid:
    print(i[::-1],sep='')