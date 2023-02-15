import sys
import collections

def topological_sort(graph,indegree,result):
    queue = collections.deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
            result[i]=1
    
    while queue:
        node = queue.popleft()

        for next in graph[node]:
            indegree[next]-=1
            if indegree[next]==0:
                queue.append(next)
                result[next] = result[node]+1

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b]+=1

topological_sort(graph,indegree,result)

print(*result[1:])