import sys

n = sys.stdin.readline().strip()

num_of_set = 0
num_list = []
for i in n:
    if int(i) in num_list:
        num_list.remove(int(i))
    elif int(i)==9:
        if 6 in num_list:
            num_list.remove(6)
        else:
            num_list.extend([0,1,2,3,4,5,6,7,8,9])
            num_of_set+=1
            num_list.remove(int(i))
    elif int(i)==6:
        if 9 in num_list:
            num_list.remove(9)
        else:
            num_list.extend([0,1,2,3,4,5,6,7,8,9])
            num_of_set+=1
            num_list.remove(int(i))
    else:
        num_list.extend([0,1,2,3,4,5,6,7,8,9])
        num_of_set+=1
        num_list.remove(int(i))

print(num_of_set)