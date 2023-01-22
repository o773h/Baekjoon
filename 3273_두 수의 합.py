import sys
n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())

n_list.sort()

start = 0
end = n-1
count = 0

for start in range(n):
    while start<end and n_list[start] + n_list[end] > x:
        end-=1

    if start>=end:
        break
    
    if n_list[start] + n_list[end] == x:
        count+=1

print(count)