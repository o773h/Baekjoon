import sys

def find_partner(neg_list,pos_list):
    if len(neg_list)==0 or len(pos_list)==0:
        return 0
        
    left = 0
    right = len(pos_list)-1
    count = 0

    while left<len(neg_list) and right>-1:
        while abs(neg_list[left]) <= pos_list[right]:
            right-=1
            if right==-1:
                break

        if right!=-1:
            count+=1
            left+=1
            right-=1
           
    return count

n = int(sys.stdin.readline())
men = list(map(int,sys.stdin.readline().split()))
women = list(map(int,sys.stdin.readline().split()))

men.sort()
women.sort()

neg_men=[]
pos_men=[]

neg_women=[]
pos_women=[]

for i in men:
    if i<0:
        neg_men.append(i)
    else:
        pos_men.append(i)

for i in women:
    if i<0:
        neg_women.append(i)
    else:
        pos_women.append(i)
        

print(find_partner(neg_men,pos_women) + find_partner(neg_women,pos_men))