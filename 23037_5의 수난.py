import sys

num = sys.stdin.readline().strip()

result = 0
for n in num:
    result += int(n)**5

print(result)