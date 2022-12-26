import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    req = sys.stdin.readline().split()
    if req[0]=='add':
        s.add(int(req[1]))
    elif req[0]=='remove':
        if int(req[1]) in s:
            s.remove(int(req[1]))
    elif req[0]=='check':
        if int(req[1]) in s:
            print(1)
        else:
            print(0)
    elif req[0]=='toggle':
        if int(req[1]) in s:
            s.remove(int(req[1]))
        else:
            s.add(int(req[1]))
    elif req[0]=='all':
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    else:
        s = set()