import sys
from collections import deque

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

que = deque()
pocket = set()

idx = 0
max_length = 0

if n>=len(set(word)):
    max_length = len(word)
else:
    while idx<len(word):

        while len(pocket)<n:
            que.append(word[idx])
            pocket.add(word[idx])
            idx +=1
        
        if word[idx] not in pocket:
            length = len(que)
            max_length = max(max_length,length)
            while que:
                s = que.popleft()
                if s not in que:
                    pocket.remove(s)
                    pocket.add(word[idx])
                    break
        
        que.append(word[idx])
        idx+=1

    max_length = max(max_length,len(que))

print(max_length)