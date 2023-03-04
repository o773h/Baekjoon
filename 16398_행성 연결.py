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

matrix=[]
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))

parent = [i for i in range(n)]
edges=[]
for i in range(n):
    for j in range(i+1,n):
        edges.append((i,j,matrix[i][j]))

edges.sort(key = lambda x : x[2])

cost = 0
l = 0
for i,j,c in edges:
    if find_parent(parent,i) != find_parent(parent,j):
        union_parent(parent,i,j)
        cost +=c
        l +=1
    if l==n-1:
        break

print(cost)