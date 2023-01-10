import sys

h,w = map(int,sys.stdin.readline().split())
h_list = list(map(int,sys.stdin.readline().split()))

higest = h_list.index(max(h_list))

high = h_list[0]
idx = 0
result = 0
sum = 0
for i in range(1,higest+1):
    if h_list[i]>=high:
        result += high * (i-idx-1) - sum
        sum = 0
        idx = i
        high = h_list[i]
    else:
        sum+=h_list[i]

high = h_list[-1]
idx = -1
sum = 0
for i in range(2,w-higest+1):
    if h_list[-i]>=high:
        result += high * (idx+i-1) - sum
        sum = 0
        idx = -i
        high = h_list[-i]
    else:
        sum+=h_list[-i]

print(result)