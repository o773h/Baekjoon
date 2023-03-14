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


t = int(sys.stdin.readline())
for _ in range(t):
    n,m,p,q = map(int,sys.stdin.readline().split())

    parent = [i for i in range(n+1)]
    edgs = []
    for _ in range(m):
        u,v,w = map(int,sys.stdin.readline().split())
        edgs.append((w,u,v))
    
    edgs.sort()
    result = "NO"
    l = 0
    for w,u,v in edgs:
        if find_parent(parent,u)!= find_parent(parent,v):
            union_parent(parent,u,v)
            l+=1
            if (u==p and v==q) or (u==q and v==p):
                result = "YES"
        if l == n-1:
            break
    
    print(result)