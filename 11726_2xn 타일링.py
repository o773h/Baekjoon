# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하기
# 2x1 -> 1가지
# 2x2 -> 2가지
# 2x3 -> 2x1의 경우에 1x2 타일 두개를 추가하면 되고,
#     -> 2x2의 경우에 2x1 타일 하나를 추가하면 되니까
# 2x3-> 1가지 + 2가지
# 마찬가지로 2xn 의 방법의 수 (2x(n-1)의 방법의 수) + (2x(n-2)의 방법의 수)
# 따라서 피보나치수열임을 알 수 있다.
# 메모화를 통해서 반복된 계산을 최소화할 수 있다.

memo = {
    1:1,
    2:2
}

def solve(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = solve(n-1)+solve(n-2)
        return memo[n]

n = int(input())

print(solve(n)%10007)