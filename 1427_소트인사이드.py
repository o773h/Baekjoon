import sys

n = sys.stdin.readline().strip()
n_list = [0 for _ in range(10)]
for i in n:
    n_list[int(i)]+=1

for j in range(9,-1,-1):
    print(str(j)*n_list[j],end='')