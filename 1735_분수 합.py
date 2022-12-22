import sys
import math

a1,b1 = map(int,sys.stdin.readline().split())
a2,b2 = map(int,sys.stdin.readline().split())

a = a1 * b2 + a2*b1
b = b1 * b2

print(a//math.gcd(a,b),b//math.gcd(a,b))