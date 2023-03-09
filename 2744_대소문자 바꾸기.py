import sys

s = sys.stdin.readline().rstrip()

for i in s:
    if i.islower():
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')