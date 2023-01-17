import sys

n = sys.stdin.readline().strip()

for i in range(len(n)):
    print(n[i],end='')
    if (i+1)%10==0:
        print()