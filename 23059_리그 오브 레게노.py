import sys
import heapq

def topological_sort():
    queue = []
    next_queue = []
    result = []
    for key,value in indegree.items():
        if value==0:
            heapq.heappush(queue,key)

    while queue:
        item = heapq.heappop(queue)
        result.append(item)

        for next in graph[item]:
            indegree[next]-=1
            if indegree[next]==0:
                heapq.heappush(next_queue,next)
        
        if len(queue)==0:
            queue = next_queue
            next_queue=[]

    if len(result)!=len(indegree):
        print(-1)
    else:    
        print(*result,sep='\n')


n = int(sys.stdin.readline())
indegree = dict()
graph = dict()

for _ in range(n):
    a,b = sys.stdin.readline().split()
    if a not in indegree:
        indegree[a] = 0
    if b not in indegree:
        indegree[b] = 0
    
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    indegree[b]+=1

topological_sort()