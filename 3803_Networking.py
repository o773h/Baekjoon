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


while True:
    p = tuple(map(int,sys.stdin.readline().split()))

    if len(p)==1:
        break
    parent = [i for i in range(p[0]+1)]
    edges = []
    for _ in range(p[1]):
        a,b,c = map(int,sys.stdin.readline().split())
        edges.append((c,a,b))
    
    edges.sort()
    result = 0
    l = 0
    for c,a,b in edges:
        if find_parent(parent,a)!= find_parent(parent,b):
            union_parent(parent,a,b)
            result+=c
            l+=1
        if l==p[0]-1:
            break
    
    print(result)
    sys.stdin.readline()