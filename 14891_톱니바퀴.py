import sys
import collections

def rotate(gear,i,clockwise):
    if clockwise==1:
        gear[i].extendleft(gear[i].pop())

    else:
        gear[i].extend(gear[i].popleft())

def contact(gear):
    check_list=[False for _ in range(4)]
    for i in range(3):
        if gear[i][2]!=gear[i+1][6]:
            check_list[i]=True
    
    return check_list
        

gear = [collections.deque() for _ in range(4)]


for i in range(4):
    gear[i].extend(list(sys.stdin.readline().strip()))

k = int(sys.stdin.readline())

for _ in range(k):
    num,clockwise = map(int,sys.stdin.readline().split())
    check_list = contact(gear)

    if num==1:
        if gear[0][2] != gear[1][6]:
            if gear[1][2] != gear[2][6]:
                if gear[2][2] != gear[3][6]:
                    rotate(gear,3,clockwise*-1)
                rotate(gear,2,clockwise)
            rotate(gear,1,clockwise*-1)
        rotate(gear,0,clockwise)

    elif num==2:
        if gear[0][2] != gear[1][6]:
            rotate(gear,0,clockwise*-1)

        if gear[1][2] != gear[2][6]:
            if gear[2][2] != gear[3][6]:
                rotate(gear,3,clockwise)
            rotate(gear,2,clockwise*-1)
        rotate(gear,1,clockwise)

    elif num==3:
        if gear[2][2] != gear[3][6]:
            rotate(gear,3,clockwise*-1)

        if gear[1][2] != gear[2][6]:
            if gear[0][2] != gear[1][6]:
                rotate(gear,0,clockwise)
            rotate(gear,1,clockwise*-1)
        rotate(gear,2,clockwise)
    
    else:
        if gear[2][2] != gear[3][6]:
            if gear[1][2] != gear[2][6]:
                if gear[0][2] != gear[1][6]:
                    rotate(gear,0,clockwise*-1)
                rotate(gear,1,clockwise)
            rotate(gear,2,clockwise*-1)
        rotate(gear,3,clockwise)

    
result = 0
for i in range(4):
    result += int(gear[i][0])*(2**i)

print(result)