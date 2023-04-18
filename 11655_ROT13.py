import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'

st = sys.stdin.readline().rstrip()

for s in st:
    if s.isdigit() or s.isspace():
        print(s,end='')
        continue

    if s.isupper():
        s = s.lower()
        idx = alpha.find(s)
        idx = (idx+13)%26
        print(alpha[idx].upper(),end='')
    else:
        idx = alpha.find(s)
        idx = (idx+13)%26
        print(alpha[idx],end='')