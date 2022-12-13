import sys

n,k = map(int,sys.stdin.readline().split())
n_list = [i for i in range(1,n+1)]
result_list = []

i = 0
while len(n_list)!=0:
    i+= k-1
    if i>=len(n_list):
        i= i % len(n_list)
    result_list.append(n_list[i])
    del n_list[i]

print("<",end='')
print(', '.join(str(x) for x in result_list),end='')
print(">")