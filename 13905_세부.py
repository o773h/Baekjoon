import sys
sys.setrecursionlimit(1000000)

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
s,e = map(int,sys.stdin.readline().split())

parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    u,v,k = map(int,sys.stdin.readline().split())
    edges.append((k,u,v))

edges.sort(reverse=True)

result = 0
for k,u,v in edges:
    if find_parent(parent,u) != find_parent(parent,v):
        union_parent(parent,u,v)
        if find_parent(parent,s)==find_parent(parent,e):
            result = k
            break

print(result)