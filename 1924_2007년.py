import sys

day = ['MON','TUE', 'WED', 'THU', 'FRI', 'SAT' , 'SUN']

result = -1

x,y = map(int,sys.stdin.readline().split())

for i in range(1,x):
    for j in range(1,31+1):
        result+=1
        if j==28:
            if i==2:
                break
        if j==30:
            if i==4 or i==6 or i==9 or i==11:
                break

result+=y
result = result%7

print(day[result])