import sys

s = sys.stdin.readline().rstrip()

start = 0
end = len(s)-1
result = 1

while start<end:
    if s[start]!=s[end]:
        result = 0
        break

    start+=1
    end-=1

print(result)