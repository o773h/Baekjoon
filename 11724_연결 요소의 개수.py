import sys
import collections

def bfs(graph,x,visited):
    count = 0
    queue = collections.deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        if x not in visited:
            count = 1
            visited.append(x)
            queue.extend(graph[x])
    
    return count


n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[]
result = 0

for i in range(1,n+1):
    result += bfs(graph,i,visited)

print(result)