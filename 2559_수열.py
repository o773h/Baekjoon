import sys

n,k = map(int,sys.stdin.readline().split())
n_list = list(map(int,sys.stdin.readline().split()))
sum = 0
sum_list = []

for i in range(k):
    sum += n_list[i]

sum_list.append(sum)

for j in range(k,n):
    sum = sum - n_list[j-k] + n_list[j]
    sum_list.append(sum)

print(max(sum_list))