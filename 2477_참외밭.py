import sys

k = int(sys.stdin.readline())
n_list = []

for _ in range(6):
    n_list.append(int(sys.stdin.readline().split()[1]))

max_len = max(n_list)
max_idx = n_list.index(max_len)

len1 = n_list[max_idx-1]
len2 = n_list[(max_idx+1) % 6]

if len1>len2:
    second_len = len1
    second_idx = max_idx-1
    area2 = (len1-len2) * n_list[(max_idx+2) % 6]
else:
    second_len = len2
    second_idx = (max_idx+1) % 6
    area2 = (len2-len1) * n_list[max_idx-2]

area = max_len * second_len

print(k * (area - area2))