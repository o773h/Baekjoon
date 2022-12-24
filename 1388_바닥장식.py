import sys

n,m = map(int,sys.stdin.readline().split())
nm_list = []
for _ in range(n):
    nm_list.append(sys.stdin.readline().strip())

count = 0

for i in nm_list:
    flag = True
    for j in i:
        if j=='-' and flag:
            count+=1
            flag = False
        elif j=='|':
            flag = True

for i in range(m):
    flag = True
    for j in range(n):
        if nm_list[j][i]=='|' and flag:
            count+=1
            flag = False
        elif nm_list[j][i]=='-':
            flag = True

print(count)