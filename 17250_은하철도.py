import sys
sys.setrecursionlimit(int(1e6))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        planet[a] += planet[b]
        parent[b] = a
        return planet[a]
    elif a>b:
        planet[b] += planet[a]
        parent[a] = b
    
    return planet[b]


n,m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]
planet = [0]
for _ in range(n):
    planet.append(int(sys.stdin.readline()))

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(union_parent(parent,a,b))