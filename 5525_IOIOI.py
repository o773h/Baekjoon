import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

start = 0
end = 0
count = 0
result = 0
while end<m:
    if (count%2==0 and s[end]=='I') or (count%2==1 and s[end]=='O'):
        count+=1
    else:
        while s[end]=='O':
            end+=1
            if end==m:
                break
        start = end
        count = 1
    
    if count==2*n+1:
        result+=1
        start+=2
        count-=2
    
    end+=1

print(result)    