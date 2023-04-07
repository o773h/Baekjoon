import sys

n,m,k = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
create = [0 for _ in range(n+1)]

result = True
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[y].append(x)

for _ in range(k):
    s,a = map(int,sys.stdin.readline().split())

    if not result:
        continue

    if s==1:
        flag = True
        for prev in graph[a]:
            if create[prev]<1:
                flag = False
                break
        if flag:
            create[a]+=1
        else:
            result = False

    else:
        if create[a]==0:
            result = False
        else:
            create[a]-=1

if result:
    print("King-God-Emperor")
else:
    print("Lier!")