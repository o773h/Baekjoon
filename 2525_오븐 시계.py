import sys

a,b = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())

b += c

a += b//60
a %= 24
b %= 60

print(a,b)