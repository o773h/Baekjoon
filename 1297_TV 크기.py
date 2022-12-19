import sys
import math

d,h,w = map(int,sys.stdin.readline().split())
k = d/math.sqrt(h**2+w**2)
w *= k
h *= k
print(int(h),int(w))