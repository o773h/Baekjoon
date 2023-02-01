import sys

n = int(sys.stdin.readline())
n_list=[]
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

neg_zero_list = []
pos_list = []

for i in n_list:
    if i<=0:
        neg_zero_list.append(i)
    else:
        pos_list.append(i)

if n==1:
    print(n_list[0])
else:
    result = 0
    if len(neg_zero_list)%2==0 and len(neg_zero_list)!=0:
        for i in range(0,len(neg_zero_list),2):
            result += neg_zero_list[i]*neg_zero_list[i+1]
    elif len(neg_zero_list)%2==1:
        if len(neg_zero_list)!=1:
            for i in range(0,len(neg_zero_list)-1,2):
                result += neg_zero_list[i]*neg_zero_list[i+1]
        result+=neg_zero_list[-1]

                        
    if len(pos_list)%2==0 and len(pos_list)!=0:
        for i in range(1,len(pos_list),2):
            if pos_list[-i-1]==1:
                result += pos_list[-i] + pos_list[-i-1]
            else:
                result += pos_list[-i]*pos_list[-i-1]
    elif len(pos_list)%2==1:
        if len(pos_list)!=1:
            for i in range(1,len(pos_list),2):
                if pos_list[-i-1]==1:
                    result += pos_list[-i] + pos_list[-i-1]
                else:
                    result += pos_list[-i]*pos_list[-i-1]
        result+=pos_list[0]

    print(result)