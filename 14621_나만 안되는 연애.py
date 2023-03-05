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


n,m = map(int,sys.stdin.readline().split())
univ = ['']
univ.extend(sys.stdin.readline().split())

parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    u,v,d = map(int,sys.stdin.readline().split())
    if univ[u]!=univ[v]:
        edges.append((d,u,v))

edges.sort()

result = 0
l = 0
for d,u,v in edges:
    if find_parent(parent,u)!=find_parent(parent,v):
        union_parent(parent,u,v)
        result+=d
        l+=1
    if l==n-1:
        break

if l<n-1:
    result=-1

print(result)