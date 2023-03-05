import sys
import math

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int,sys.stdin.readline().split())

xy = []
parent = [i for i in range(n+1)]
edges = []
for _ in range(n):
    xy.append(tuple(map(int,sys.stdin.readline().split())))

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    union_parent(parent,a,b)

for i in range(n):
    for j in range(i+1,n):
        c = math.dist((xy[i][0],xy[i][1]),(xy[j][0],xy[j][1]))
        edges.append((c,i+1,j+1))

edges.sort()

result = 0
for c,i,j in edges:
    if find_parent(parent,i) != find_parent(parent,j):
        union_parent(parent,i,j)
        result+=c

print("%.2f"%result)