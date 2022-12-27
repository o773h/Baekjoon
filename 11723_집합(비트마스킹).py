import sys

m = int(sys.stdin.readline())
s = 0

for _ in range(m):
    req = sys.stdin.readline().split()
    if req[0]=='add':
        s = s|(1<<int(req[1]))
    elif req[0]=='remove':
        s = s & ~(1<<int(req[1]))
    elif req[0]=='check':
        if (s & (1<<int(req[1])))==0:
            print(0)
        else:
            print(1)
    elif req[0]=='toggle':
        s = s ^ (1<<int(req[1]))
    elif req[0]=='all':
        s = (1<<21) - 1
    else:
        s = 0