import sys

def dfs(graph,start,visited=[]):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph,i,visited)
    return visited


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
m = int(sys.stdin.readline())
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(len(dfs(graph,1))-1)