import sys

n,l = map(int,sys.stdin.readline().split())
h_list = list(map(int,sys.stdin.readline().split()))

h_list.sort()

for h in h_list:
    if l>=h:
        l+=1
    else:
        break

print(l)