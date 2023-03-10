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


n,m,k = map(int,sys.stdin.readline().split())
k_list = list(map(int,sys.stdin.readline().split()))

parent = [i for i in range(n+1)]
edges = []

if k>1:
    for i in range(1,k):
        union_parent(parent,k_list[0],k_list[i])

for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().split())
    edges.append((w,u,v))

edges.sort()

result = 0
l = 0
for w,u,v in edges:
    if find_parent(parent,u) != find_parent(parent,v):
        union_parent(parent,u,v)
        result += w
        l+=1
    if l==n-k:
        break

print(result)