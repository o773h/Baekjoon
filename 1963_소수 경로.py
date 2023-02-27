import sys
import collections

def change_num(num):
    change_list = []
    for i in range(1,10):
        num1 = (i*1000+num%1000)
        if num1 != num:
            if num1 in prime_numbers:
                if num1 not in visited:
                    visited.add(num1)
                    change_list.append(num1)

    for i in range(10):
        num2 = (num//1000)*1000 + i*100 + num%100
        num3 = (num//100)*100 + i*10 + num%10
        num4 = (num//10)*10 + i

        if num2!=num:
            if num2 in prime_numbers:
                if num2 not in visited:
                    visited.add(num2)
                    change_list.append(num2)
        if num3!=num:
            if num3 in prime_numbers:
                if num3 not in visited:
                    visited.add(num3)
                    change_list.append(num3)
        if num4!=num:
            if num4 in prime_numbers:
                if num4 not in visited:
                    visited.add(num4)
                    change_list.append(num4)

    return change_list

def bfs(start,end):
    queue = collections.deque()
    queue.append(start)
    count = 1
    result = 0

    while queue:
        num = queue.popleft()
        if num==end:
            return result
        count-=1
        queue.extend(change_num(num))
        if count==0:
            count = len(queue)
            result+=1

    return "Impossible"

nums = [True for _ in range(10000)]
for i in range(3,1000,2):
    if nums[i]:
        for j in range(i,10000,i):
            nums[j]=False

prime_numbers=set()
for i in range(1001,10000,2):
    if nums[i]:
        prime_numbers.add(i)
        for j in range(i,10000,i):
            nums[j]=False
            
t = int(sys.stdin.readline())
for _ in range(t):
    visited=set()
    start, end = map(int,sys.stdin.readline().split())
    if start==end:
        print(0)
    else:
        print(bfs(start,end))