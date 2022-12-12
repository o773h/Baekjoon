import sys

dq = []

def push_front(dq,num):
    dq.insert(0,num)

def push_back(dq,num):
    dq.append(num)

def pop_front(dq):
    if len(dq)==0:
        print(-1)
    else:
        print(dq[0])
        del dq[0]

def pop_back(dq):
    if len(dq)==0:
        print(-1)
    else:
        print(dq[-1])
        del dq[-1]

def size(dq):
    print(len(dq))

def empty(dq):
    if len(dq)==0:
        print(1)
    else:
        print(0)

def front(dq):
    if len(dq)==0:
        print(-1)
    else:
        print(dq[0])

def back(dq):
    if len(dq)==0:
        print(-1)
    else:
        print(dq[-1])

n = int(sys.stdin.readline())

for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0]=='push_front':
        push_front(dq,int(x[1]))
    elif x[0]=='push_back':
        push_back(dq,int(x[1]))
    elif x[0]=='pop_front':
        pop_front(dq)
    elif x[0]=='pop_back':
        pop_back(dq)
    elif x[0]=='size':
        size(dq)
    elif x[0]=='empty':
        empty(dq)
    elif x[0]=='front':
        front(dq)
    else:
        back(dq)