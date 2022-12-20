import sys
import math

n,j,h = map(int,sys.stdin.readline().split())
count = 1

while True:
    if abs(j-h)==1 and max(j,h)%2==0:
        print(count)
        break
    else:
        j = math.ceil(j/2)
        h = math.ceil(h/2)
        count+=1