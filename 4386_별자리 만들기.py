import sys
import math

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
stars = []
for _ in range(n):
    x,y = map(float,sys.stdin.readline().split())
    stars.append((x,y))

parent = [i for i in range(n)]
edges=[]

for i in range(n):
    for j in range(i+1,n):
        c = math.dist((stars[i][0],stars[i][1]),(stars[j][0],stars[j][1]))
        edges.append((i,j,c))

edges.sort(key=lambda x:x[2])

result = 0
l = 0
for a,b,c in edges:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=c
        l+=1
    if l==n-1:
        break

print(round(result,2))