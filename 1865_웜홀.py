import sys

def bf():
    for i in range(n):
        for j in range(2*m+w):
            curr,next,cost = edges[j]
            
            if distance[curr]+cost < distance[next]:
                distance[next] = distance[curr] + cost
                if i==n-1:
                    return True
    
    return False


tc = int(sys.stdin.readline())

for _ in range(tc):
    n,m,w = map(int,sys.stdin.readline().split())

    edges = []
    distance = [0 for _ in range(n+1)]

    for _ in range(m):
        s,e,t = map(int,sys.stdin.readline().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    
    for _ in range(w):
        s,e,t, = map(int,sys.stdin.readline().split())
        edges.append((s,e,-t))

    negative_cycle = bf()

    if negative_cycle:
        print("YES")
    else:
        print("NO")