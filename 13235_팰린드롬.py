import sys

s = sys.stdin.readline().rstrip()

result = "false"
if s == s[::-1]:
    result = "true"
print(result)