import sys

block_23 = [[[1,1,1]
            ,[0,0,1]],
            [[1,1,1]
            ,[0,1,0]],
            [[1,1,1]
            ,[1,0,0]],
            [[0,0,1]
            ,[1,1,1]],
            [[0,1,0]
            ,[1,1,1]],
            [[1,0,0]
            ,[1,1,1]],
            [[1,1,0]
            ,[0,1,1]],
            [[0,1,1]
            ,[1,1,0]]]

block_32 = [[[1,1],
             [1,0],
             [1,0]],
             [[1,0],
             [1,1],
             [1,0]],
             [[1,0],
             [1,0],
             [1,1]],
             [[1,1],
             [0,1],
             [0,1]],
             [[0,1],
             [1,1],
             [0,1]],
             [[0,1],
             [0,1],
             [1,1]],
             [[1,0],
             [1,1],
             [0,1]],
             [[0,1],
             [1,1],
             [1,0]],]

def solve_23():
    ret = 0
    for block in block_23:
        for i in range(n-1):
            for j in range(m-2):
                sum = 0
                for y in range(i,i+2):
                    for x in range(j,j+3):
                        sum+=grid[y][x]*block[y-i][x-j]
                ret = max(ret,sum)
    return ret

def solve_32():
    ret = 0
    for block in block_32:
        for i in range(n-2):
            for j in range(m-1):
                sum = 0
                for y in range(i,i+3):
                    for x in range(j,j+2):
                        sum+=grid[y][x]*block[y-i][x-j]
                ret = max(ret,sum)
    return ret

def solve_14():
    ret = 0
    for i in range(n):
            for j in range(m-3):
                sum = 0
                for x in range(j,j+4):
                    sum+=grid[i][x]
                ret = max(ret,sum)
    return ret

def solve_41():
    ret = 0
    for i in range(n-3):
            for j in range(m):
                sum = 0
                for y in range(i,i+4):
                    sum+=grid[y][j]
                ret = max(ret,sum)
    return ret

def solve_22():
    ret = 0
    for i in range(n-1):
        for j in range(m-1):
            sum = 0
            for y in range(i,i+2):
                for x in range(j,j+2):
                    sum+=grid[y][x]
            ret = max(ret,sum)
    return ret



n,m = map(int,sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,sys.stdin.readline().split())))

print(max(solve_14(),solve_22(),solve_23(),solve_32(),solve_41()))