import sys

a = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
b = int(sys.stdin.readline())

if s=='*':
    print(a*b)
else:
    print(a+b)