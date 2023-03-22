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
        robot[a] += robot[b]
    elif a>b:
        parent[a] = b
        robot[b] += robot[a]


n = int(sys.stdin.readline())

parent = [i for i in range(1000000+1)]
robot = [1 for _ in range(1000000+1)]

for _ in range(n):
    l = list(sys.stdin.readline().split())
    if l[0]=='I':
        union_parent(parent,int(l[1]),int(l[2]))
    else:
        print(robot[find_parent(parent,int(l[1]))])