import sys

while True:
    s = sys.stdin.readline()
    if s=='.\n':
        break
    stk = []
    flag = True
    for i in s:
        if i=='(' or i=='[':
            stk.append(i)
        if i==')':
            if stk==[] or stk[-1]!='(':
                flag = False
                break
            else:
                flag = True
                del stk[-1]

        if i==']':
            if stk==[] or stk[-1]!='[':
                flag = False
                break
            else:
                flag = True
                del stk[-1]
    
    if flag and stk==[]:
        print('yes')
    else:
        print('no')
