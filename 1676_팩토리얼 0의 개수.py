import sys
import math

n = int(sys.stdin.readline())
n_str = str(math.factorial(n))
count = 0

for i in range(1,len(n_str)+1):
    if n_str[-i]!='0':
        break
    count+=1

print(count)