import sys
import collections

t = int(sys.stdin.readline())

for _ in range(t):
    deq = collections.deque()
    func = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    
    lst = list(sys.stdin.readline().strip().split(','))
    lst[0] = lst[0][1:]
    lst[-1] = lst[-1][:-1]
    lst = ' '.join(lst).split()
    deq.extend(lst)

    flag = True
    count = 0
    for i in func:
        if i=='R':
            count+=1
        else:
            if len(deq)==0:
                flag = False
                break

            if count%2==1:
                deq.pop()           
            else:
                deq.popleft()


    if flag:
        print("[",end='')
        if count%2==1:
            deq.reverse()
            print(','.join(deq),end='')
        else:
            print(','.join(deq),end='')
        print("]")
    else:
        print("error")