import sys

g = int(sys.stdin.readline())

n = 100000
square_numbers= [i*i for i in range(n)]

start = 1
end = 2
result = []
while start<n:
    while square_numbers[end]-square_numbers[start]<g:
        end+=1
        if end==n:
            break
    
    if end==n:
        break

    if square_numbers[end]-square_numbers[start] >= g:
        if square_numbers[end]-square_numbers[start] ==g:
            result.append(end)
        start+=1

if len(result)==0:
    print(-1)
else:
    print(*result,sep='\n')