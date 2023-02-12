import sys

n = int(sys.stdin.readline())

for i in range(n-1,0,-1):
    print('*'*(n-i),' '*(2*i),'*'*(n-i),sep='')

for i in range(n):
    print('*'*(n-i),' '*(2*i),'*'*(n-i),sep='')