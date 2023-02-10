import sys

n = int(sys.stdin.readline())

for _ in range(n):
    r,e,c, = map(int,sys.stdin.readline().split())
    advertise = e-c

    if r<advertise:
        print("advertise")
    elif r>advertise:
        print("do not advertise")
    else:
        print("does not matter")