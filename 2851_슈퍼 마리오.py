import sys

sum = 0
n_list = []
flag = True
for _ in range(10):
    n_list.append(int(sys.stdin.readline()))

for n in n_list:
    if sum+n >= 100:
        if sum+n-100 <= 100-sum:
            result = sum+n
        else:
            result = sum
        flag = False
        break
    else:
        sum+=n

if flag:
    result = sum

print(result)