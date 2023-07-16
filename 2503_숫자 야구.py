import sys
from itertools import permutations

n = int(sys.stdin.readline())
lst = []
for i in permutations(range(1,10),3):
    a,b,c = i
    lst.append(a*100+b*10+c)

for _ in range(n):
    num,s,b = map(int,sys.stdin.readline().split())
    new_lst = []
    for l in lst:
        s_count = 0
        b_count = 0

        str_num = str(num)
        str_l = str(l)

        if '0' in str_l:
            continue

        for i in range(3):
            if str_num[i]==str_l[i]:
                s_count +=1
            elif (str_num[i] == str_l[i-1]) or (str_num[i] == str_l[i-2]):
                b_count +=1
        
        if s_count == s and b_count == b:
            new_lst.append(l)
    lst = new_lst

print(len(lst))