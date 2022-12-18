import sys

n,m = map(int,sys.stdin.readline().split())
n_list = []
m_list = []
result = []
count = 0
for _ in range(n):
    n_list.append(sys.stdin.readline().strip())

for _ in range(m):
    m_list.append(sys.stdin.readline().strip())

n_list.sort()
m_list.sort()
start = 0
for i in n_list:
    for j in range(start,m):
        if m_list[j]==i:
            result.append(i)
            start = j+1
            count+=1
        elif m_list[j]>i:
            start = j
            break

if count!=0:
    print(count)
    print(*result,sep='\n')
else:
    print(count)