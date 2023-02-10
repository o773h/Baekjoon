import sys

a,b,c = map(int,sys.stdin.readline().split())
d = int(sys.stdin.readline())

c += d

b += c//60
c %= 60

a += b//60
b %= 60

a %= 24

print(a,b,c)