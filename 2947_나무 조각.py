import sys

wood = list(map(int,sys.stdin.readline().split()))

for j in range(5,1,-1):
    for i in range(1,j):
        if wood[i-1]>wood[i]:
            wood[i-1],wood[i] = wood[i],wood[i-1]
            print(*wood)