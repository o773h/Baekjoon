import sys
import heapq

def topological_sort():
    queue = []
    result = []
    for i in range(1,n+1):
        if indegree[i]==0:
            heapq.heappush(queue,i)
    
    while queue:
        node = heapq.heappop(queue)
        result.append(node)

        for next in graph[node]:
            indegree[next]-=1
            if indegree[next]==0:
                heapq.heappush(queue,next)
    return result


n,m = map(int,sys.stdin.readline().split())
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] +=1

print(*topological_sort())