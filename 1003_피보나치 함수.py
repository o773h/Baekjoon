# n    :  0 1 2 3 4 5 6 7
# 0호출:  1 0 1 1 2 3 5 8
# 1호출:  0 1 1 2 3 5 8 13
# n>=3 일때부터는 피보나치 수열을 따름

#메모화(memoization)를 통해 한 번 계산한 값을 저장해두기

dictionary = {
    0:0,
    1:1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fibonacci(n-1)+fibonacci(n-2)
        return dictionary[n]

t = int(input())

for _ in range(t):
    n = int(input())
    if n==0:
        print(1,0)
    else:
        print(fibonacci(n-1),fibonacci(n))