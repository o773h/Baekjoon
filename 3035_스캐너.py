import sys

r,c,zr,zc = map(int,sys.stdin.readline().split())

grid = []
for _ in range(r):
    grid.append(list(sys.stdin.readline().strip()))

for i in range(r):
    for _ in range(zr):
        for j in range(c):
            print(grid[i][j]*zc,end='')
        print()