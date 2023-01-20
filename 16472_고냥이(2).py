import sys
from collections import deque

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

que = deque()

idx = 0
max_length = 0
count = 0
if n>=len(set(word)):
    max_length = len(word)
else:
    while idx<len(word):

        while count<n:
            if word[idx] not in que:
                count+=1
            que.append(word[idx])
            idx +=1
        
        if word[idx] not in que:
            length = len(que)
            max_length = max(max_length,length)
            while que:
                s = que.popleft()
                if s not in que:
                    break
        
        que.append(word[idx])
        idx+=1

    max_length = max(max_length,len(que))

print(max_length)