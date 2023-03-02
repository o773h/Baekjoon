import sys

for _ in range(3):
    l = sys.stdin.readline().strip()
    result = 0
    for s in l:
        if s=='1':
            result+=1
    
    if result==3:
        print('A')
    elif result==2:
        print('B')
    elif result==1:
        print('C')
    elif result==0:
        print('D')
    else:
        print('E')