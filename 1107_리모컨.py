import sys
from itertools import product

buttons = ['0','1','2','3','4','5','6','7','8','9']

n = sys.stdin.readline().strip()
l = len(n)
n = int(n)
m = int(sys.stdin.readline())
if m!=0:
    for i in sys.stdin.readline().split():
        buttons.remove(i)

result_list = [abs(100-n)]
for i in range(l-1,l+2):
    if i==7:
        break
    for _,j in enumerate(product(buttons,repeat=i)):
        if len(j)!=0:
            result_list.append(i + abs(int(''.join(j))-n))

print(min(result_list))