import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    score1 = 0
    score2 = 0
    for _ in range(n):
        p1,p2 = sys.stdin.readline().split()
        
        if p1==p2:
            continue
        elif (p1=='R' and p2=='S') or (p1=='S' and p2=='P') or (p1=='P' and p2=='R'):
            score1 +=1
        else:
            score2 +=1
    
    if score1>score2:
        result="Player 1"
    elif score1<score2:
        result="Player 2"
    else:
        result="TIE"
    print(result)