import sys

max_num = 0
result = (1,1)
for i in range(9):
    l = list(map(int,sys.stdin.readline().split()))
    num = max(l)
    if max_num < num:
        max_num = num
        result = (i+1,l.index(num)+1)

print(max_num)
print(*result)