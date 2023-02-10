import sys

def find_parent(parent,x):
    if x!=parent[x]:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]
know_people = list(map(int,sys.stdin.readline().split()))

party = []
for _ in range(m):
    party.append(list(map(int,sys.stdin.readline().split())))

if know_people[0] ==0:
    print(m)
else:
    for i in range(2,len(know_people)):
        union(parent,know_people[i-1],know_people[i])

    members = []
    for j in party:
        members.append(j[1])
        for k in range(2,j[0]+1):
            union(parent,j[k-1],j[k])

    count = 0
    for i in members:
        if find_parent(parent,i) != find_parent(parent,know_people[1]):
            count+=1

    print(count)