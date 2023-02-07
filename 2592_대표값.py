import sys
from collections import defaultdict

num = defaultdict(int)
for _ in range(10):
    num[int(sys.stdin.readline())]+=1

max_value = 0
mode = 0
sum = 0
for key,value in num.items():
    sum += key * value
    if value>max_value:
        mode = key
        max_value = value

print(sum//10)
print(mode)