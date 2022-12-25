import sys
import collections

n_list = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(5):
    n_list.append(list(sys.stdin.readline().split()))

result=[]

def dfs(lst,x,y,num):
    
    if len(num)==6:
        if num not in result:
            result.append(num)
        return
    
    for i in range(4):
        px = x+dx[i]            
        py = y+dy[i]
        if 0<=px<5 and 0<=py<5:
            dfs(lst,px,py,num + lst[px][py])
        
for i in range(5):
    for j in range(5):
        dfs(n_list,i,j,n_list[i][j])
        
print(len(result))