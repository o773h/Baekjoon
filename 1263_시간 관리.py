import sys

n = int(sys.stdin.readline())
ts_list = []

for _ in range(n):
    ts_list.append(list(map(int,sys.stdin.readline().split())))

ts_list.sort(key=lambda x : x[1])
flag = True
time = ts_list[-1][1]
for i in range(1,len(ts_list)+1):
    if time<ts_list[-i][1]:
        ts_list[-i][1] = time

    if ts_list[-i][1]<ts_list[-i][0]:
        flag = False
        break
    else:
        time = ts_list[-i][1] - ts_list[-i][0]

if flag:
    print(time)
else:
    print(-1)
