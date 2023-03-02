import sys
import collections

alpha = collections.defaultdict(int)
st = sys.stdin.readlines()

for line in st:
    for s in line:
        if s!=' ' and s!='\n':
            alpha[s]+=1

m = max(alpha.values())
result = []
for k,v in alpha.items():
    if v == m:
        result.append(k)

result.sort()
print(*result,sep='')