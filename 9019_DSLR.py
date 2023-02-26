import sys
import collections

def calc_num(queue,end,num,s):
    num1 = (num*2) % 10000
    if num1 not in num_dict:
        num_dict[num1] = s+'D'
        if num1==end:
            return num_dict[num1]
        queue.append(num1)

    num2 = num-1
    if num2==-1:
        num2=9999
    if num2 not in num_dict:
        num_dict[num2] = s+'S'
        if num2==end:
            return num_dict[num2]
        queue.append(num2)

    num3 = (num%1000)*10 + num//1000
    if num3 not in num_dict:
        num_dict[num3] = s+'L'
        if num3==end:
            return num_dict[num3]
        queue.append(num3)

    num4 = (num%10)*1000 + (num//10)
    if num4 not in num_dict:
        num_dict[num4] = s+'R'
        if num4==end:
            return num_dict[num4]
        queue.append(num4)
        
    return False

def bfs(start,end):
    queue = collections.deque()
    queue.append(start)
    num_dict[start]=''

    while queue:
        num = queue.popleft()
        result = calc_num(queue,end,num,num_dict[num])
        
        if result:
            return result


t = int(sys.stdin.readline())
for _ in range(t):
    num_dict = dict()
    a,b = map(int,sys.stdin.readline().split())
    print(bfs(a,b))