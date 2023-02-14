import sys

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,cost,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
        cost[a] = min(cost[a],cost[b])
    else:
        parent[a] = b
        cost[b] = min(cost[a],cost[b])

n,m,k = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]

cost = [0]
cost.extend(list(map(int,sys.stdin.readline().split())))

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    union(parent,cost,a,b)

result = 0

for i in range(1,n+1):
    if parent[i]==i:
        result+=cost[i]


if result>k:
    print("Oh no")
else:
    print(result)