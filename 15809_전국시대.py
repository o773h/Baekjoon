import sys
sys.setrecursionlimit(1000000)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,o, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if o==1:
        if a<b:
            power[a] += power[b]
            parent[b] = a
        elif a>b:
            power[b] += power[a]
            parent[a] = b
    else:
        if power[a] > power[b]:
            power[a] = power[a] - power[b]
            parent[b] = a
        elif power[a] < power[b]:
            power[b] = power[b] - power[a]
            parent[a] = b
        else:
            parent[a] = 0
            parent[b] = 0


n,m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]
power = [0]

for _ in range(n):
    power.append(int(sys.stdin.readline()))

for _ in range(m):
    o,p,q = map(int,sys.stdin.readline().split())
    union_parent(parent, o, p, q)

country = set()
for i in range(n+1):
    country.add(find_parent(parent, i))

result = []
for c in country:
    if c!=0:
        result.append(power[c])

result.sort()

print(len(country)-1)
print(*result)