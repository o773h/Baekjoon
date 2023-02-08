import sys

def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

lst = []
parent =[i for i in range(n+1)]

for _ in range(n):
    lst.append(list(sys.stdin.readline().split()))

for i in range(n):
    for j in range(i,n):
        if lst[i][j]=='1':
            union(parent,i+1,j+1)

route = list(map(int,sys.stdin.readline().split()))

first = find(parent,route[0])
result = "YES"
for i in range(1,len(route)):
    if find(parent,route[i])!=first:
        result = "NO"
        break

print(result)