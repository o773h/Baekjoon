import sys

result = 0
min_num = 100
for _ in range(7):
    n = int(sys.stdin.readline())

    if n%2==1:
        result+=n
        min_num = min(min_num,n)

if result==0:
    print(-1)
else:
    print(result)
    print(min_num)