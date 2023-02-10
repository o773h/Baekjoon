import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = list(sys.stdin.readline().split())
    num = float(s[0])
    for i in range(1,len(s)):
        if s[i]=='@':
            num *=3
        elif s[i]=='%':
            num +=5
        else:
            num -=7
    print("%.2f"%num)