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
        parent[b] = a
    else:
        parent[a] = b


n,m,k = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]

stones = list(map(int,sys.stdin.readline().split()))
unable_move = set()
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    a,b = min(a,b),max(a,b)
    unable_move.add((a,b))

ans = "YES"
if m>1:

    for i in range(1,n):
        if (i,i+1) not in unable_move:
            union_parent(parent,i,i+1)

    if (1,n) not in unable_move:
        union_parent(parent,1,n)

    result = dict()

    for i in range(1,n+1):
        p = find_parent(parent,i)
        if p not in result:
            result[p] = stones[i-1]
        else:
            result[p] = min(result[p], stones[i-1])

    if sum(result.values()) > k:
        ans = "NO"

print(ans)