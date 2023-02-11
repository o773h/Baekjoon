import sys
import heapq

def dijkstra(distance,start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start]=0

    while queue:
        dist,node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        
        for next in graph[node]:
            cost = dist+next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue,(cost,next[0]))
    return distance
        
INF = int(1e9)

n,e = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
distance_1 = [INF for _ in range(n+1)]
distance_v1 = [INF for _ in range(n+1)]
distance_v2 = [INF for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,sys.stdin.readline().split())

distance_1 = dijkstra(distance_1,1)
distance_v1 = dijkstra(distance_v1,v1)
distance_v2 = dijkstra(distance_v2,v2)

route_v1_v2 = distance_1[v1] + distance_v1[v2] + distance_v2[n]
route_v2_v1 = distance_1[v2] + distance_v2[v1] + distance_v1[n]

if min(route_v1_v2,route_v2_v1)<INF:
    print(min(route_v1_v2,route_v2_v1))
else:
    print(-1)