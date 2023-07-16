import sys
from itertools import combinations

n = int(sys.stdin.readline())
min_score = 100
lst = []

for _ in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

for i,team in enumerate(combinations(range(n),n//2)):

    g1_score = 0
    g2_scroe = 0

    n_team = []
    for j in range(n):
        if j not in team:
            n_team.append(j)

    for j in range(n):
        if j in team:
            for t in team:
                g1_score += lst[j][t]
        else:
            for t in n_team:
                g2_scroe += lst[j][t]


    score = abs(g1_score - g2_scroe)
    min_score = min(min_score,score)

print(min_score)