import sys
import heapq

INF = int(1e9)

def dijkstra():
    queue = []
    distance[0] = 0
    heapq.heappush(queue,(0,0))

    while queue:
        dist,node = heapq.heappop(queue)
        if node==m-1:
            return True

        if dist> distance[node]:
            continue
        
        for next in graph[node]:
            cost = next[1] + dist
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                pre[next[0]] = node
                heapq.heappush(queue,(cost,next[0]))
    return False


t = int(sys.stdin.readline())
for case in range(1,t+1):
    n,m = map(int,sys.stdin.readline().split())
    distance = [INF for _ in range(m)]
    pre = [i for i in range(m)]
    graph = [[] for _ in range(m)]
    for _ in range(n):
        x,y,z = map(int,sys.stdin.readline().split())
        graph[x].append((y,z))
        graph[y].append((x,z))

    print("Case #",case,": ",sep='',end='')
    if dijkstra():
        result = [m-1]
        p = pre[m-1]
        while p !=0:
            result.append(p)
            p = pre[p]
        result.append(p)

        print(*result[::-1])
    else:
        print(-1)