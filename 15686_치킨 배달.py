import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())
grid = []
chickens = []
houses = []

for i in range(n):
    grid.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if grid[i][j]==2:
            chickens.append((i,j))
        elif grid[i][j]==1:
            houses.append((i,j))


distance_list = []

for chicken in combinations(chickens,m):       
    total_distance = 0

    for house in houses:
        distance = 0
        for i in chicken:
            if distance==0:
                distance = abs(house[0] - i[0]) + abs(house[1] - i[1])
            else:
                distance = min(distance,abs(house[0] - i[0]) + abs(house[1] - i[1]))
        
        total_distance+=distance
        
    distance_list.append(total_distance)
    

print(min(distance_list))