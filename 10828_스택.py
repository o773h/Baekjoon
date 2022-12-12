import sys

stk = []

def push(stk,num):
    stk.append(num)

def pop(stk):
    if len(stk)==0:
        print(-1)
    else:
        print(stk[-1])
        del stk[-1]

def size(stk):
    print(len(stk))

def empty(stk):
    if len(stk)==0:
        print(1)
    else:
        print(0)

def top(stk):
    if not stk:
        print(-1)
    else:
        print(stk[-1])

n = int(sys.stdin.readline())

for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0]=='push':
        push(stk,int(x[1]))
    elif x[0]=='pop':
        pop(stk)
    elif x[0]=='size':
        size(stk)
    elif x[0]=='empty':
        empty(stk)
    else:
        top(stk)