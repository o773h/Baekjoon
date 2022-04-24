memo = {
    1:1,
    2:1,
    3:1,
    4:2,
    5:2
}

def solve(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = solve(n-1)+solve(n-5)
        return memo[n]

t = int(input())

for _ in range(t):
    n = int(input())
    print(solve(n))