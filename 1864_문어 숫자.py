import sys

s_dict = {'-':0,'\\':1,'(':2,'@':3,'?':4,
     '>':5,'&':6,'%':7,'/':-1}

while True:
    st = sys.stdin.readline().strip()
    if st=='#':
        break

    result= 0
    for i in range(1,len(st)+1):
        result += s_dict[st[-i]]*(8**(i-1))

    print(result)