import sys
import heapq

INF = int(1e12)

def dijkstra():
    queue = []
    distance[0] = 0
    heapq.heappush(queue,(0,0))

    while queue:
        dist, node = heapq.heappop(queue)

        if node == n-1:
            return dist

        if distance[node] < dist:
            continue

        for next in graph[node]:
            if ward[next[0]]==0:
                cost = next[1] + dist
                if distance[next[0]] > cost:
                    distance[next[0]] = cost
                    heapq.heappush(queue,(cost,next[0]))
    return -1


n,m = map(int,sys.stdin.readline().split())
ward = list(map(int,sys.stdin.readline().split()))
ward[-1]=0

graph = [[] for _ in range(n)]
distance = [INF for _ in range(n)]

for _ in range(m):
    a,b,t = map(int,sys.stdin.readline().split())
    graph[a].append((b,t))
    graph[b].append((a,t))

print(dijkstra())