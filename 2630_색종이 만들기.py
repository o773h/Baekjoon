import sys

def check_paper(lst,n,white_blue):
    blue_flag = True
    white_flag = True
    for i in range(n):
        for j in range(n):
            if lst[i][j]=='0':
                blue_flag = False
            else:
                white_flag = False
        
    if blue_flag:
        white_blue[1]+=1
        return 
    if white_flag:
        white_blue[0]+=1
        return 
    
    new_list1 = [lst[i][:n//2] for i in range(n//2)]
    new_list2 = [lst[i][n//2:] for i in range(n//2)]
    new_list3 = [lst[i][:n//2] for i in range(n//2,n)]
    new_list4 = [lst[i][n//2:] for i in range(n//2,n)]

    check_paper(new_list1,n//2,white_blue)
    check_paper(new_list2,n//2,white_blue)
    check_paper(new_list3,n//2,white_blue)
    check_paper(new_list4,n//2,white_blue)


n = int(sys.stdin.readline())
n_list =[]

for _ in range(n):
    n_list.append(list(sys.stdin.readline().split()))

white_blue=[0,0]

check_paper(n_list,n,white_blue)
print(*white_blue,sep='\n')