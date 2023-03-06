import sys
import collections
import heapq

dy = [-1,0,0,1]
dx = [0,-1,1,0]

def bfs():
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = collections.deque()
    move = []
    y,x = baby_shark['y'],baby_shark['x']
    grid[y][x] = 0
    queue.append((y,x))
    visited[y][x] = True
    
    count = 1
    second = 0

    while queue:
        y,x = queue.popleft()
        count-=1
        for i in range(4):
            py = y + dy[i]
            px = x + dx[i]

            if 0<=py<n and 0<=px<n:
                if visited[py][px]==False:
                    if grid[py][px]==0 or grid[py][px]==baby_shark['status']:
                        visited[py][px] = True
                        queue.append((py,px))
                    elif grid[py][px]<baby_shark['status']:
                        heapq.heappush(move,(py,px))
                        
        if count==0:
            second +=1
            count = len(queue)

            if len(move)>=1:
                y,x = heapq.heappop(move)
                baby_shark['y'] = y
                baby_shark['x'] = x

                baby_shark['eat'] +=1
                if baby_shark['eat']==baby_shark['status']:
                    baby_shark['status']+=1
                    baby_shark['eat'] = 0
                return second

    return -1
            
                        
n = int(sys.stdin.readline())

grid = []
for i in range(n):
    l = list(map(int,sys.stdin.readline().split()))
    if 9 in l:
        y = i
        x = l.index(9)
    grid.append(l)

baby_shark = {'y':y,'x':x,
              'status':2,'eat':0}

result = 0
while True:
    second = bfs()
    if second==-1:
        break
    result += second

print(result)