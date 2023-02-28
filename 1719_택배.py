import sys
import heapq

INF = int(1e9)

def dijkstra(start):
    distance = [INF for _ in range(n+1)]
    result = [-1 for _ in range(n+1)]

    queue = []
    distance[start] = 0
    result[start] = '-'
    heapq.heappush(queue,(0,start))

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        
        for next in graph[node]:
            cost = dist + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                if node==start:
                    result[next[0]] = next[0]
                else:
                    result[next[0]] = result[node]
                heapq.heappush(queue,(cost,next[0]))

    return result[1:]
    
        
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(1,n+1):
    print(*dijkstra(i))