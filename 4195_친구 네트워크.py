import sys

def find_parent(parent,x):
    if x!=parent[x]:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,count,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        count[a] += count[b]
        parent[b] = a
    elif a>b:
        count[b] += count[a]
        parent[a] = b
        

t = int(sys.stdin.readline())
for _ in range(t):
    parent = {}
    count = {}

    f = int(sys.stdin.readline())
    for _ in range(f):
        a,b = sys.stdin.readline().split()
        
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        
        union(parent,count,a,b)
        print(count[find_parent(parent,a)])