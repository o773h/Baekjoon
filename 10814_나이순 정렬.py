import sys

n = int(sys.stdin.readline())
name_list=[[] for _ in range(10001)]

for _ in range(n):
    age,name = sys.stdin.readline().split()
    name_list[int(age)].append(name)

for i,lst in enumerate(name_list):
    if lst!=[]:
        for j in lst:
            print(i,j)