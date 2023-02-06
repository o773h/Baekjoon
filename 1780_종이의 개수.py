import sys

def find_paper(n,grid,result):
    flag_0 = False
    flag_1 = False
    flag_m1 = False
    for i in range(n):
        if 0 in grid[i]:
            flag_0 = True
        if 1 in grid[i]:
            flag_1 = True
        if -1 in grid[i]:
            flag_m1 = True
    if flag_m1 and not (flag_0 or flag_1):
        result[0]+=1
    elif flag_0 and not (flag_1 or flag_m1):
        result[1]+=1
    elif flag_1 and not (flag_0 or flag_m1):
        result[2]+=1
    
    else:
        grid1 = [grid[i][:n//3] for i in range(n//3)]
        grid2 = [grid[i][n//3:2*n//3] for i in range(n//3)]
        grid3 = [grid[i][2*n//3:] for i in range(n//3)]

        grid4 = [grid[i][:n//3] for i in range(n//3,2*n//3)]
        grid5 = [grid[i][n//3:2*n//3] for i in range(n//3,2*n//3)]
        grid6 = [grid[i][2*n//3:] for i in range(n//3,2*n//3)]

        grid7 = [grid[i][:n//3] for i in range(2*n//3,n)]
        grid8 = [grid[i][n//3:2*n//3] for i in range(2*n//3,n)]
        grid9 = [grid[i][2*n//3:] for i in range(2*n//3,n)]

        result = find_paper(n//3,grid1,result)
        result = find_paper(n//3,grid2,result)
        result = find_paper(n//3,grid3,result)
        result = find_paper(n//3,grid4,result)
        result = find_paper(n//3,grid5,result)
        result = find_paper(n//3,grid6,result)
        result = find_paper(n//3,grid7,result)
        result = find_paper(n//3,grid8,result)
        result = find_paper(n//3,grid9,result)
    
    return result

n = int(sys.stdin.readline())

grid = []
for _ in range(n):
    grid.append(list(map(int,sys.stdin.readline().split())))

result=[0,0,0]
print(*find_paper(n,grid,result),sep='\n')