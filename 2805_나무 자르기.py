import sys

n,m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

i = 0
j = max(trees)

while i<=j:
    mid = (i+j)//2
    x=0
    for k in trees:
        if k>mid:
            x+= k-mid
    if x>=m:
        i = mid+1
    else:
        j = mid-1

print(j)