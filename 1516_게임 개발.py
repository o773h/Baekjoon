import sys
import collections

def topological_sort():
    queue = collections.deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
            result[i] = times[i]
    
    while queue:
        node = queue.popleft()

        for next in graph[node]:
            indegree[next]-=1
            result[next] = max(result[next],result[node] + times[next])
            if indegree[next]==0:
                queue.append(next)
    return result


n = int(sys.stdin.readline())

indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
times = [0]
result = [0 for _ in range(n+1)]

for num in range(1,n+1):
    c,*l = map(int,sys.stdin.readline().split())
    times.append(c)
    for i in range(len(l)-1):
        graph[l[i]].append(num)
        indegree[num]+=1

result = topological_sort()

for i in range(1,n+1):
    print(result[i])