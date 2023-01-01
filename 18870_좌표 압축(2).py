import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
sorted_list = sorted(set(n_list))
dict = {}

for i,num in enumerate(sorted_list):
    dict[num]=i

for num in n_list:
    print(dict[num],end=' ')