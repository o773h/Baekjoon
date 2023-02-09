import sys
import collections

def bfs(move,visited,x):
    queue = collections.deque()
    queue.append(x)
    visited[x]= True
    count = 1
    distance = 0
    while queue:
        x = queue.popleft()
        count-=1
        for i in range(1,7):
            px = x + i
            if visited[px]==False:
                visited[px]=True
                if px == 100:
                    return distance+1
                elif px<100:
                    if px in move:
                        if visited[move[px]] == False:
                            visited[move[px]]=True
                            queue.append(move[px])                        
                    else:
                        queue.append(px)
        if count==0:
            count = len(queue)
            distance+=1
        

n,m = map(int,sys.stdin.readline().split())
move = dict()
visited=[False for _ in range(101)]
for i in range(n+m):
    u,v = map(int,sys.stdin.readline().split())
    move[u] = v

print(bfs(move,visited,1))