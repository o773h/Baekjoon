import sys

n = int(sys.stdin.readline())
n_list = []
num = 0
count = 0
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

for i in range(1,n+1):
    if n_list[-i]>num:
        count+=1
        num = n_list[-i]

print(count)