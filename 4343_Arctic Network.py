import sys
import math

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

for _ in range(n):
    s,p = map(int,sys.stdin.readline().split())

    edges = []
    parent = [i for i in range(p)]
    xy = []
    for _ in range(p):
        xy.append(tuple(map(int,sys.stdin.readline().split())))
    
    for i in range(p):
        for j in range(i+1,p):
            c = math.dist(xy[i],xy[j])
            edges.append((c,i,j))

    edges.sort()

    result = 0
    l = 0
    for c,a,b in edges:
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result= c
            l +=1
        if l==p-s:
            break

    print("%.2f"%result)