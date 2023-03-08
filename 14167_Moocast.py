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

edges = []
parent = [i for i in range(n)]
xy = []
for _ in range(n):
    xy.append(tuple(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(i+1,n):
        c = (xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2
        edges.append((c,i,j))

edges.sort()

result = 0
l = 0
for c,a,b in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result= c
        l +=1
    if l==n-1:
        break

print(result)