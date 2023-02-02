import sys

def make_word(result, count):
    result+= "AAAA"*(count//4)
    count = count%4
    result += "BB" * (count//2)

    return result

s = sys.stdin.readline().rstrip()

result = ''
count = 0
flag = True
for i in s:
    if i =='.':
        if count%2==1:
            flag = False
            break
        else:
            result = make_word(result,count)
            count = 0
        result+='.'
    else:
        count+=1

if count%2==1:
    flag = False
else:
    result = make_word(result,count)

if flag:
    print(result)
else:
    print(-1)