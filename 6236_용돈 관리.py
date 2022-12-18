import sys

n,m = map(int,sys.stdin.readline().split())

moneys =[]
for _ in range(n):
    moneys.append(int(sys.stdin.readline()))


start = max(moneys)
end = sum(moneys)



while start<=end:
    count = 0
    money = 0
    mid = (start+end)//2
    for i in moneys:
        if money<i:
            money=mid
            count+=1
            money-=i
        else:
            money-=i
    
    if count>m:
        start = mid+1
    else:
        end = mid-1

print(start)