import sys

n = int(sys.stdin.readline())

s = set()
for _ in range(n):
    a,b = sys.stdin.readline().split()
    if b=='enter':
        s.add(a)
    if b=='leave':
        s.remove(a)

s = sorted(list(s),reverse=True)
print(*s,sep='\n')