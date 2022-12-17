import sys

n,k = map(int,sys.stdin.readline().split())
n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

count = 0
for i in range(1,n+1):
    if k>=n_list[-i]:
        count += k//n_list[-i]
        k = k%n_list[-i]
    if k==0:
        break

print(count)