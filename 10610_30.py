import sys

n_dict = {'9':0,'8':0,'7':0,'6':0,'5':0,'4':0,'3':0,'2':0,'1':0,'0':0}
n = sys.stdin.readline().strip()
sum = 0
for s in n:
    n_dict[s]+=1
    sum += int(s)

result = ''

if n_dict['0']==0 or sum%3!=0:
    result = '-1'
else:
    for key,value in n_dict.items():
        if value!=0:
            result+=key*value

print(result)