import sys

n = int(sys.stdin.readline())
n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

sum = 0 

median = n_list[n//2]

mode = n_list[0]
now = n_list[0]
count = 0
max_count = -1
flag = True

n_range = n_list[-1] - n_list[0]

for i in n_list:
    if now==i:
        count+=1
    else:
        if max_count<count:
            max_count = count
            mode = now
            flag = True
        elif (max_count==count) and flag==True:
            mode = now
            flag = False
        count = 1
    now = i
    sum+=i

if max_count<count:
    max_count = count
    mode = now
    flag = True
elif (max_count==count) and flag==True:
    mode = now
    flag = False

print(round(sum/n))
print(median)
print(mode)
print(n_range)