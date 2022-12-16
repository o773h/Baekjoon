import sys

n = int(sys.stdin.readline())
cows=[]
counts = [0 for _ in range(2)]
for _ in range(n):
    cows.append(list(sys.stdin.readline().split()))

for i in cows:
    if (i[0]=='1' and i[1]=='2') or (i[0]=='2' and i[1]=='3') or (i[0]=='3' and i[1]=='1'):
        counts[0]+=1
    elif (i[0]=='1' and i[1]=='3') or (i[0]=='3' and i[1]=='2') or (i[0]=='2' and i[1]=='1'):
        counts[1]+=1

print(max(counts))