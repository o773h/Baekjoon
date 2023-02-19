import sys

s = sys.stdin.readline().strip()

result = 0

count = {'0':0,'1':0}
pos = s[0]
for i in range(1,len(s)):
    if s[i]!=pos:
        count[pos]+=1
        pos = s[i]
count[s[-1]]+=1

result = min(count.values())

print(result)