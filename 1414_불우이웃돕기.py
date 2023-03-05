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


alpha = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(sys.stdin.readline())
result = 0
parent = [i for i in range(n)]
cable = []
edges=[]
for _ in range(n):
    cable.append(sys.stdin.readline().strip())

for i in range(n):
    for j in range(n):
        if cable[i][j]=='0':
            continue

        if i==j:
            result+=alpha.index(cable[i][j])
        else:
            edges.append((alpha.index(cable[i][j]),i,j))

edges.sort()

l = 0
for c,i,j in edges:
    if l==n-1:
        result+=c
    else:
        if find_parent(parent,i)!=find_parent(parent,j):
            union_parent(parent,i,j)
            l+=1
        else:
            result+=c

if l<n-1:
    result = -1

print(result)