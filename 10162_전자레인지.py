import sys

t = int(sys.stdin.readline())

a = 300
b = 60
c = 10

result = []
result.append(t // a)
t %= a
result.append(t//b)
t %= b
result.append(t//c)
t %= c

if t!=0:
    print(-1)
else:
    print(*result)