import sys

result = 1

e,s,m = map(int,sys.stdin.readline().split())
e1,s1,m1 = 1,1,1

while not (e1==e and s1==s and m1==m):
    e1+=1
    s1+=1
    m1+=1
    result+=1
    if e1==16:
        e1 = 1
    if s1==29:
        s1 = 1
    if m1==20:
        m1 = 1

print(result)