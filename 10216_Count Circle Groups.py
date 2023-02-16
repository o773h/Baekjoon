import sys
from collections import defaultdict

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def check(circle1,circle2):
    if (circle1[0]-circle2[0])**2 + (circle1[1]-circle2[1])**2<=(circle1[2]+circle2[2])**2:
        return True
    return False


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    parent = [i for i in range(n)]

    grid=[]
    for _ in range(n):
        grid.append(list(map(int,sys.stdin.readline().split())))

    for i in range(n):
        for j in range(i+1,n):
            if find_parent(parent,i)!=find_parent(parent,j):
                if check(grid[i],grid[j]):
                    union(parent,i,j)
    
    group = defaultdict(int)
    for i in range(n):
        group[find_parent(parent,i)]+=1
    
    print(len(group))