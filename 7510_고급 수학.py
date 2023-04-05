import sys

t = int(sys.stdin.readline())
for case in range(1,t+1):
    s = list(map(int,sys.stdin.readline().split()))
    s.sort()
    print("Scenario #",case,":",sep='')
    if s[2]**2 == s[0]**2 + s[1]**2:
        print("yes")
    else:
        print("no")
    print()