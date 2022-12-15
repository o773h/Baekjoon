import sys

k,n = map(int,sys.stdin.readline().split())
k_list = []
for _ in range(k):
    k_list.append(int(sys.stdin.readline()))

start = 1
end = max(k_list)

while start<=end:
    mid = (start+end)//2
    count = 0
    for i in k_list:
        count+=i//mid

    if count>=n:
        start = mid+1
    else:
        end = mid-1

print(end)