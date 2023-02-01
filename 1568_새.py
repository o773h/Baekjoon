import sys

n = int(sys.stdin.readline())

count = 0
i = 1
while True:
    n-=i
    count+=1
    if n==0:
        break

    i+=1
    if n<i:
        i=1

print(count)