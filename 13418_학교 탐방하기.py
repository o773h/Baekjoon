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

edges = []
parent1 = [i for i in range(n+1)]
parent2 = [i for i in range(n+1)]

for _ in range(m+1):
    a,b,c = map(int,sys.stdin.readline().split())
    edges.append((c,a,b))

edges.sort()

max_result = 0
l = 0
for c,a,b in edges:
    if find_parent(parent1,a) != find_parent(parent1,b):
        union_parent(parent1,a,b)
        l+=1
        if c==0:
            max_result+=1
    if l==n:
        break

edges.sort(reverse=True)

min_result = 0
l = 0
for c,a,b in edges:
    if find_parent(parent2,a) != find_parent(parent2,b):
        union_parent(parent2,a,b)
        l+=1
        if c==0:
            min_result+=1
    if l==n:
        break

print(max_result**2 - min_result**2)