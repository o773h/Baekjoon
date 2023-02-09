import sys
import heapq

INF = int(1e9)

def dijkstra(start,distacne,graph):
    queue = []
    heapq.heappush(queue,(0,start))
    distacne[start]=0

    while queue:
        dist,node = heapq.heappop(queue)

        if distacne[node] < dist:
            continue

        for next in graph[node]:
            cost = dist + next[1]
            if cost < distacne[next[0]]:
                distacne[next[0]] = cost
                heapq.heappush(queue,(cost,next[0]))

    return distacne

n,m,x = map(int,sys.stdin.readline().split())

graph_go_x = [[] for _ in range(n+1)]
graph_go_home = [[] for _ in range(n+1)]

distance_x = [INF for _ in range(n+1)]
distance_home = [INF for _ in range(n+1)]

for _ in range(m):
    a,b,t = map(int,sys.stdin.readline().split())
    graph_go_x[b].append((a,t))
    graph_go_home[a].append((b,t))

distance_x = dijkstra(x,distance_x,graph_go_x)
distance_home = dijkstra(x,distance_home,graph_go_home)

max_distance = distance_x[1] + distance_home[1]
for i in range(2,n+1):
    if distance_x[i] + distance_home[i] > max_distance:
        max_distance = distance_x[i] + distance_home[i]

print(max_distance)