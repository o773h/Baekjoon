import sys

a,b = sys.stdin.readline().strip().split()
min_count = len(a)

for i in range(len(b)-len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j]!=b[j+i]:
            count+=1
    min_count = min(count,min_count)

print(min_count)