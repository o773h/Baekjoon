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


v,e = map(int,sys.stdin.readline().split())
edge = []
parent = [i for i in range(v+1)]

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    edge.append((c,a,b))

edge.sort()

result = 0
for c,a,b in edge:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=c

print(result)