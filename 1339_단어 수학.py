import sys
from collections import defaultdict

n = int(sys.stdin.readline())
alpha_dict = defaultdict(int)

for i in range(n):
    s = sys.stdin.readline().strip()
    for j in range(1,len(s)+1):
        alpha_dict[s[-j]]+=10**(j-1)

n_list = list(alpha_dict.values())
n_list.sort(reverse=True)

i = 9
result = 0
for num in n_list:
    result += num*i
    i-=1

print(result)