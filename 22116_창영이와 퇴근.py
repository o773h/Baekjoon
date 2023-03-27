import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n = int(sys.stdin.readline())
parent = [i for i in range(n*n)]

grid = []
for _ in range(n):
    grid.append(list(map(int,sys.stdin.readline().split())))

edges = []

for i in range(n-1):
    for j in range(n-1):
        edges.append(((abs(grid[i][j]-grid[i][j+1])),i*n+j,i*n+j+1))
        edges.append(((abs(grid[i][j]-grid[i+1][j])),i*n+j,(i+1)*n+j))

for i in range(n-1):
    edges.append(((abs(grid[i][n-1]-grid[i+1][n-1])),i*n+n-1,(i+1)*n+n-1))

for j in range(n-1):
    edges.append(((abs(grid[n-1][j]-grid[n-1][j+1])),(n-1)*n+j,(n-1)*n+j+1))

edges.sort()

for w,a,b in edges:
    union_parent(parent,a,b)
    if find_parent(parent,0)==find_parent(parent,n*n-1):
        print(w)
        break

if n==1:
    print(0)