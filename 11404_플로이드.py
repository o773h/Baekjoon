import sys
import heapq

INF = int(1e9)

def dijkstra(start):
    queue = []
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    heapq.heappush(queue,(0,start))

    while queue:
        dist, node = heapq.heappop(queue)
        if dist> distance[node]:
            continue

        for next in graph[node]:
            cost = dist + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(queue,(cost,next[0]))
    for i in range(1,n+1):
        if distance[i]==INF:
            print(0,end=' ')
        else:
            print(distance[i],end=' ')
    print()


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

for i in range(1,n+1):
    dijkstra(i)