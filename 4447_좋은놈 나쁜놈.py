import sys

n = int(sys.stdin.readline())

for _ in range(n):
    name = sys.stdin.readline().rstrip()

    g = 0
    b = 0
    for s in name:
        if s=='g' or s=='G':
            g+=1
        elif s=='b' or s=='B':
            b+=1
    
    if g>b:
        print(name,"is GOOD")
    elif g<b:
        print(name,"is A BADDY")
    else:
        print(name,"is NEUTRAL")