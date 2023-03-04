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

parent= [i for i in range(n)]
edges=[]
planet=[]
for i in range(n):
    x,y,z = map(int,sys.stdin.readline().split())
    planet.append((x,y,z,i))

planet.sort()
for i in range(1,n):
    c = planet[i][0]-planet[i-1][0]
    edges.append((c,planet[i][3],planet[i-1][3]))

planet.sort(key=lambda x : x[1])
for i in range(1,n):
    c = planet[i][1]-planet[i-1][1]
    edges.append((c,planet[i][3],planet[i-1][3]))

planet.sort(key=lambda x : x[2])
for i in range(1,n):
    c = planet[i][2]-planet[i-1][2]
    edges.append((c,planet[i][3],planet[i-1][3]))

edges.sort()

cost = 0
l = 0
for c,a,b in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        cost += c
        l +=1
    if l==n-1:
        break

print(cost)