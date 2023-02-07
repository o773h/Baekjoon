import sys

s = sys.stdin.readline().strip()

start = s[0]
result = 10
for i in range(1,len(s)):
    if s[i]!=start:
        result+=10
        start=s[i]
    else:
        result+=5
        
print(result)