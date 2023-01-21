import sys
import bisect

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))

n1,n2 = n_list[0],n_list[1]
sum = abs(n1+n2)

for i,num in enumerate(n_list):
  
    right = bisect.bisect_right(n_list,-num)
    left = bisect.bisect_left(n_list,-num)

    if right == left:
        try:
            if num == n_list[left] or num == n_list[left-1]:
                continue
            right_sum = abs(num + n_list[left])
            left_sum = abs(num + n_list[left-1])

            if left_sum > right_sum:
                if sum > right_sum:
                    sum = right_sum
                    n1,n2 = num,n_list[left]
            else:
                if sum > left_sum:
                    sum = left_sum
                    n1,n2 = num,n_list[left-1]
            
        except IndexError:
            if (right == n and i==n-1):
                continue
            if sum > abs(num + n_list[-1]):
                sum = abs(num + n_list[-1])
                n1,n2 = num,n_list[-1]
    else:
        n1,n2 = num,n_list[left]
        break

    
print(min(n1,n2),max(n1,n2))