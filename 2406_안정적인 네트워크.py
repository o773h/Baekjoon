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
parent = [i for i in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    union_parent(parent,x,y)

cost = []
for _ in range(n):
    cost.append(list(map(int,sys.stdin.readline().split())))

edges = []

for i in range(1,n):
    for j in range(i+1,n):
        edges.append((cost[i][j],i+1,j+1))

edges.sort()

total_cost = 0
k = 0
k_list = []
for cost,x,y in edges:
    if find_parent(parent,x)!=find_parent(parent,y):
        union_parent(parent,x,y)
        total_cost+=cost
        k_list.append((x,y))
        k+=1

print(total_cost,k)
if k>0:
    for x,y in k_list:
        print(x,y)