import sys
import heapq

INF = int(1e9)

def dijkstra():
    queue = []
    result = []
    heapq.heappush(queue,(0,1,0))
    distance[1] = 0

    while queue:
        dist,node,pre = heapq.heappop(queue)

        if dist>distance[node]:
            continue
        
        if pre!=0:
            result.append((node,pre))

        for next in graph[node]:
            cost = dist+next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue,(cost,next[0],node))
    return result


n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

result =  dijkstra()

print(len(result))
for i in result:
    print(*i)