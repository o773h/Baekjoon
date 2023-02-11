import sys

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
parent=[i for i in range(n+1)]
for _ in range(n-2):
    a,b = map(int,sys.stdin.readline().split())
    union(parent,a,b)


for i in range(2,n+1):
    if find_parent(parent,i)!=1:
        node = i
        break

print(1,node)