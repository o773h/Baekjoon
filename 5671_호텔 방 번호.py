while True:
    try:
        s = input()
    except EOFError:
        break

    n,m = map(int,s.split())
    count = 0
    
    for i in range(n,m+1):
        flag = True
        for j in range(10):
            if str(i).count(str(j))>=2:
                flag = False
                break
        if flag:
            count+=1
    print(count)