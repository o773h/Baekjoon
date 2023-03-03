import sys

Y = 2000

def find_parent(parent,y,x):
    if parent[y][x] != y*Y + x:
        parent[y][x] = find_parent(parent,parent[y][x]//Y,parent[y][x]%Y)
    return parent[y][x]

def union_parent(parent,y1,x1,y2,x2):
    p1 = find_parent(parent,y1,x1)
    p2 = find_parent(parent,y2,x2)

    if p1<p2:
        parent[p2//Y][p2%Y] = p1
    else:
        parent[p1//Y][p1%Y] = p2


n,m = map(int,sys.stdin.readline().split())
parent = [[Y*y + x for x in range(m+1)] for y in range(n+1)]

grid = []
for _ in range(n):
    grid.append(sys.stdin.readline().rstrip())

for y in range(n):
    for x in range(m):
        if grid[y][x]=='D':
            union_parent(parent,y,x,y+1,x)
        elif grid[y][x]=='U':
            union_parent(parent,y,x,y-1,x)
        elif grid[y][x]=='R':
            union_parent(parent,y,x,y,x+1)
        else:
            union_parent(parent,y,x,y,x-1)

result=set()
for y in range(n):
    for x in range(m):
        result.add(find_parent(parent,y,x))

print(len(result))