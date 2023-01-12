import sys
import collections

def move(a_list,robots):
    for i in range(n-2,0,-1):
        if robots[i]==1 and robots[i+1]==0 and a_list[i+1]>=1:
            robots[i]=0
            robots[i+1]=1
            a_list[i+1]-=1
    if robots[-1]==1:
        robots[-1]=0


n,k = map(int,sys.stdin.readline().split())

a_list = collections.deque()
robots = collections.deque()

a_list.extend(list(map(int,sys.stdin.readline().split())))
robots.extend([0 for _ in range(n)])


step=0
while True:
    step+=1

    a_list.appendleft(a_list.pop())
    robots.appendleft(robots.pop())

    if robots[-1]==1:
        robots[-1]=0

    move(a_list,robots)

    if a_list[0]!=0:
        robots[0]=1
        a_list[0]-=1

    count = 0
    for i in a_list:
        if i==0:
            count+=1
    if count>=k:
        break

print(step)