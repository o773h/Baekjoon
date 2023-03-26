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


p,w = map(int,sys.stdin.readline().split())
c,v = map(int,sys.stdin.readline().split())

parent = [i for i in range(p+1)]
edges = []
for _ in range(w):
    start,end,width = map(int,sys.stdin.readline().split())
    edges.append((width,start,end))

edges.sort(reverse=True)

for w,s,e in edges:
    if find_parent(parent,s) != find_parent(parent,e):
        union_parent(parent,s,e)
        if find_parent(parent,c) == find_parent(parent,v):
            print(w)
            break