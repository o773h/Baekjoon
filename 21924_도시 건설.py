import sys

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

parent = [i for i in range(n+1)]
edges=[]

for _ in range(m):
    edges.append(tuple(map(int,sys.stdin.readline().split())))

edges.sort(key=lambda x:x[2])

l = 0
result = 0
for a,b,c in edges:
    if l==n-1:
        result+=c
    else:
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent,a,b)
            l+=1
        else:
            result+=c

if l<n-1:
    result = -1

print(result)