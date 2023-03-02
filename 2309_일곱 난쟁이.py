import sys

height = []
for _ in range(9):
    height.append(int(sys.stdin.readline()))
height.sort()

sum_height = sum(height)

left = 0
right = 8
while True:  
    
    sum_left_right = height[left] + height[right]
    if sum_height - sum_left_right == 100:
        for i in range(9):
            if i!=left and i!=right:
                print(height[i])
        break
    elif sum_height - sum_left_right > 100:
        left+=1
    else:
        right-=1