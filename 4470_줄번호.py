import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    print(i+1,"."," ",s,sep="")