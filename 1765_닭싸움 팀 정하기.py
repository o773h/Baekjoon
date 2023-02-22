import sys
import collections

def find_parent(parent,x):
    if x!=parent[x]:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def union_enemy(parent,enemy,node):
    queue = collections.deque()
    queue.extend(enemy[node])
    l = len(queue)

    for _ in range(l):
        x = queue.popleft()
        queue.extend(enemy[x])
    
    while queue:
        frined = queue.popleft()
        union_parent(parent,node,frined)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [i for i in range(n+1)]
enemy = [[] for _ in range(n+1)]
for _ in range(m):
    s,p,q = sys.stdin.readline().split()
    if s=='E':
        enemy[int(p)].append(int(q))
        enemy[int(q)].append(int(p))
    else:
        union_parent(parent,int(p),int(q))
    
for i in range(1,n+1):
    if len(enemy[i])!=0:
        union_enemy(parent,enemy,i)
    
result = collections.defaultdict(int)

for i in range(1,n+1):
    result[find_parent(parent,i)]+=1

print(len(result))