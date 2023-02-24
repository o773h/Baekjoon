import sys
import collections

def topological_sort(graph,indegree,times,end):
    result = [0 for _ in range(n+1)]
    queue = collections.deque()
    
    for i in range(1,n+1):
        if indegree[i]==0:
            if i==end:
                return times[i]
            queue.append(i)
            result[i] = times[i]

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if result[next]<result[node]+times[next]:
                result[next] = result[node]+times[next]
            indegree[next]-=1
            if indegree[next]==0:
                if next==end:
                    return result[next]
                queue.append(next)


t = int(sys.stdin.readline())
for _ in range(t):
    n,k = map(int,sys.stdin.readline().split())
    indegree = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    times = [0]
    times.extend(list(map(int,sys.stdin.readline().split())))

    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        graph[x].append(y)
        indegree[y]+=1
    
    end = int(sys.stdin.readline())
    print(topological_sort(graph,indegree,times,end))