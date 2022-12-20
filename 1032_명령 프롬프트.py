import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    lst.append(sys.stdin.readline().strip())

name = list(lst[0])
length = len(name)
for i in range(1,n):
       for j in range(length):
            if name[j]=='?':
                continue
            if name[j]!=lst[i][j]:
                name[j]='?'

print(*name,sep='')