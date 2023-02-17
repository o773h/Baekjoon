import sys
import collections

move=[(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]

def bfs(l,start,end,visited):
    if start==end:
        return 0

    queue = collections.deque()
    queue.append(start)
    visited[start[0]][start[1]]=True

    count = 1
    distance = 1

    while queue:
        x,y = queue.popleft()
        count -=1
        for i in move:
            px = x+i[0]
            py = y+i[1]

            if 0<=px<l and 0<=py<l:
                if px==end[0] and py==end[1]:
                    return distance
                
                if visited[px][py]==False:
                    visited[px][py]=True
                    queue.append((px,py))

        if count==0:
            distance+=1
            count = len(queue)


t = int(sys.stdin.readline())

for _ in range(t):
    l = int(sys.stdin.readline())
    start = tuple(map(int,sys.stdin.readline().split()))
    end = tuple(map(int,sys.stdin.readline().split()))
    visited=[[False for _ in range(l)] for _ in range(l)]

    print(bfs(l,start,end,visited))