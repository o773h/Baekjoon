import sys

t = int(sys.stdin.readline())

for _ in range(t):
    ps = sys.stdin.readline().strip()
    count = 0
    for i in ps:
        if count<0:
            break
        if i=='(':
            count+=1
        else:
            count-=1
    if count==0:
        print('YES')
    else:
        print('NO')
