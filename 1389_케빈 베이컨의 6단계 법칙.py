import sys
import heapq

INF = int(1e9)

def dijkstra(start):
    queue = []
    distance = [INF for _ in range(n+1)]
    distance[start]= 0
    heapq.heappush(queue,(0,start))

    while queue:
        dist,node = heapq.heappop(queue)
        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + 1
            if distance[next]>cost:
                distance[next] = cost
                heapq.heappush(queue,(cost,next))

    return sum(distance[1:])


n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

min_distance = INF
result = 0
for i in range(1,n+1):
    distance = dijkstra(i)
    if distance<min_distance:
        min_distance = distance
        result = i

print(result)