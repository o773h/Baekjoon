import sys

k = int(sys.stdin.readline())
stk = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n==0:
        del stk[-1]
    else:
        stk.append(n)

print(sum(stk))