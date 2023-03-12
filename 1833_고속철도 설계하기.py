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

parent = [i for i in range(n+1)]
edges = []
cost_list = []
total_cost = 0
for _ in range(n):
    cost_list.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(i+1,n):
        if cost_list[i][j]<0:
            total_cost+=(-cost_list[i][j])
            union_parent(parent,i+1,j+1)
        else:
            edges.append((cost_list[i][j],i+1,j+1))

edges.sort()

result = []
l = 0
for cost,u,v in edges:
    if find_parent(parent,u)!=find_parent(parent,v):
        union_parent(parent,u,v)
        total_cost+=cost
        l+=1
        result.append((u,v))

print(total_cost,l)
for res in result:
    print(*res)