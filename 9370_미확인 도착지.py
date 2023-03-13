import sys
import heapq

INF = int(1e9)

T = int(sys.stdin.readline())

def dijkstra(start):
    distance = [INF for _ in range(n+1)]
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = dist + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(queue,(cost,next[0]))
    
    return distance


for _ in range(T):
    n,m,t = map(int,sys.stdin.readline().split())
    s,g,h = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]
    t_list = []
    result = []
    for _ in range(m):
        a,b,d = map(int,sys.stdin.readline().split())
        if (a==g and b==h) or (a==h and b==g):
            dist = d
        graph[a].append((b,d))
        graph[b].append((a,d))
    
    for _ in range(t):
        t_list.append(int(sys.stdin.readline()))


    s_distance = dijkstra(s)

    if s_distance[g] < s_distance[h]:
        dist = s_distance[g] + dist
        sh_distance = dijkstra(h)
    else:
        dist = s_distance[h] + dist
        sh_distance = dijkstra(g)


    for t in t_list:
        if s_distance[t] == sh_distance[t] + dist:
            result.append(t)
    
    result.sort()

    print(*result)