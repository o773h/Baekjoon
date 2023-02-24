import sys
import collections

def topological_sort(graph,indegree):
    result = []
    queue = collections.deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for next in graph[node]:
            indegree[next]-=1
            if indegree[next]==0:
                queue.append(next)
    if len(result)!=n:
        return [0]
        
    return result


n,m = map(int,sys.stdin.readline().split())
indegree=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]

for _ in range(m):
    lst = list(map(int,sys.stdin.readline().split()))
    for i in range(2,len(lst)):
        indegree[lst[i]]+=1
        graph[lst[i-1]].append(lst[i])

print(*topological_sort(graph,indegree),sep='\n')