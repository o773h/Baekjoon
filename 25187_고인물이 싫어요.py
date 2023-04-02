import sys
sys.setrecursionlimit(1000000)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        water_tank[a] += water_tank[b]
        parent[b] = a
    elif a>b:
        water_tank[b] += water_tank[a]
        parent[a] = b


n,m,q = map(int,sys.stdin.readline().split())

parent = [i for i in range(n+1)]

water_tank = [0]
water_tank.extend(list(map(int,sys.stdin.readline().split())))
for i in range(1,n+1):
    if water_tank[i] == 0:
        water_tank[i] = -1

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    union_parent(parent,u,v)

for _ in range(q):
    k = int(sys.stdin.readline())
    if water_tank[find_parent(parent,k)]>0:
        print(1)
    else:
        print(0)