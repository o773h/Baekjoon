import sys
import itertools

x = sys.stdin.readline().strip()
lst = [i for i in x]
result = []

for i in itertools.permutations(lst):
    s=''
    for j in i:
        s +=j
    result.append(int(s))

result.sort()
x = int(x)
flag = True

for i in result:
    if i>x:
        print(i)
        flag = False
        break

if flag:
    print(0)