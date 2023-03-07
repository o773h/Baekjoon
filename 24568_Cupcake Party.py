import sys

r = int(sys.stdin.readline())
s = int(sys.stdin.readline())

result = r*8+s*3-28

if result<0:
    print(0)
else:
    print(result)