import sys
import collections

n = int(sys.stdin.readline())
p1,p2 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph,start,visited=[]):
    distance = [-1 for _ in range(n+1)]#
    queue = collections.deque()
    queue.append(start)
    distance[start]=0

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if distance[i]==-1:
                distance[i]=distance[node]+1
                queue.extend(graph[node])

    return distance[p2]

print(bfs(graph,p1))