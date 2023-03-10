import sys

lst = []
for i in range(1,9):
    n = int(sys.stdin.readline())
    lst.append((n,i))

lst.sort()

sum = 0
result = []
for i in range(3,8):
    sum += lst[i][0]
    result.append(lst[i][1])

print(sum)
print(*sorted(result))