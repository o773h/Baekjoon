import sys
import collections

def topological_sort(graph,indegree,result,cost):
    queue = collections.deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
            result[i] = cost[i]

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            indegree[next]-=1
            result[next] = max(result[next],result[node]+cost[next])

            if indegree[next]==0:
                queue.append(next)  

n = int(sys.stdin.readline())

indegree=[0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
cost = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for i in range(1,n+1):
    c,num,*nums = map(int,sys.stdin.readline().split())
    indegree[i] = num
    cost[i] = c
    for j in nums:
        graph[j].append(i)
    
topological_sort(graph,indegree,result,cost)

print(max(result))