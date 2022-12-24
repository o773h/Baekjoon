import sys
import collections

def dfs(graph,start,visited=[]):

    stk = collections.deque()
    stk.append(start)

    while stk:
        node = stk.pop()
        if node not in visited:
            visited.append(node)
            stk.extend(sorted(graph[node],reverse=True))
    
    return visited


def bfs(graph,start,visited=[]):
    
    queue = collections.deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    
    return visited


n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(*dfs(graph,v))
print(*bfs(graph,v))