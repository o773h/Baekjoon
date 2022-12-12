import sys

q = []

def push(q,num):
    q.append(num)

def pop(q):
    if len(q)==0:
        print(-1)
    else:
        print(q[0])
        del q[0]

def size(q):
    print(len(q))

def empty(q):
    if len(q)==0:
        print(1)
    else:
        print(0)

def front(q):
    if len(q)==0:
        print(-1)
    else:
        print(q[0])

def back(q):
    if len(q)==0:
        print(-1)
    else:
        print(q[-1])

n = int(sys.stdin.readline())

for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0]=='push':
        push(q,int(x[1]))
    elif x[0]=='pop':
        pop(q)
    elif x[0]=='size':
        size(q)
    elif x[0]=='empty':
        empty(q)
    elif x[0]=='front':
        front(q)
    else:
        back(q)