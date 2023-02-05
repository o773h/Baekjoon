import sys

def quad_tree(result,grid,n):
    flag_1 = False
    flag_0 = False
    for i in range(n):
        if '1' in grid[i]:
            flag_1 = True
        if '0' in grid[i]:
            flag_0 = True
        if flag_1 and flag_0:
            break
    if flag_1 and not flag_0:
        return result+'1'
    elif not flag_1 and flag_0:
        return result+'0'
    else:
        result+='('
        grid1 = [grid[i][:n//2] for i in range(0,n//2)]
        grid2 = [grid[i][n//2:] for i in range(0,n//2)]
        grid3 = [grid[i][:n//2] for i in range(n//2,n)]
        grid4 = [grid[i][n//2:] for i in range(n//2,n)]
        
        result = quad_tree(result,grid1,n//2)
        result = quad_tree(result,grid2,n//2)
        result = quad_tree(result,grid3,n//2)
        result = quad_tree(result,grid4,n//2)

        return result+')'


n = int(sys.stdin.readline())

grid = []
for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))

result = ''
result = quad_tree(result,grid,n)

print(result)