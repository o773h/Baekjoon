import sys
import collections

n,m = map(int,sys.stdin.readline().split())
king = sys.stdin.readline().rstrip()

graph = collections.defaultdict(list)
value = dict()
has_parent = dict()

for _ in range(n):
    a,b,c = sys.stdin.readline().split()
    graph[b].append(a)
    graph[c].append(a)

    has_parent[a] = True

    if b not in has_parent:
        has_parent[b] = False
    if c not in has_parent:
        has_parent[c] = False

queue = collections.deque()
for name,bool in has_parent.items():
    if bool == False:
        value[name] = 0
        queue.append(name)

value[king] = 1
while queue:
    name = queue.popleft()

    for next in graph[name]:
        if next in value:
            value[next]+= value[name]/2
            queue.append(next)
        else:
            value[next] = value[name]/2

max_value = -1
result_name = ''
for _ in range(m):
    d = sys.stdin.readline().rstrip()
    if d not in graph:
        continue
    if value[d] > max_value:
        max_value = value[d]
        result_name = d

print(result_name)