import sys

INF = int(1e9)

def bf(start):
    distance[start] = 0
    
    for i in range(n):
        for j in range(m):
            curr,next,cost = edges[j]
            if distance[curr]!= INF and distance[curr] + cost < distance[next]:
                distance[next] = distance[curr] + cost
                if i==n-1:
                    return True
    
    return False


n,m = map(int,sys.stdin.readline().split())

edges = []
distance = [INF for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    edges.append((a,b,c))

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i]==INF:
            print(-1)
        else:
            print(distance[i])