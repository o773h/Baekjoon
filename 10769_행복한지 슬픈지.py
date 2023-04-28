import sys

happy = 0
sad = 0

s = sys.stdin.readline().rstrip()
n = len(s)

for i in range(n-2):
    if s[i]==':' and s[i+1]=='-':
        if s[i+2]==')':
            happy +=1
        elif s[i+2]=='(':
            sad +=1

if happy==0 and sad==0:
    result = 'none'
elif happy==sad:
    result = 'unsure'
elif happy>sad:
    result = 'happy'
else:
    result = 'sad'

print(result)