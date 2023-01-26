import sys

n = int(sys.stdin.readline())
dice = list(map(int,sys.stdin.readline().split()))
result = 0

if n==1:
    result = sum(dice) - max(dice)
else:
    one_face = min(dice)
    three_face = min(dice[0],dice[5])+min(dice[1],dice[4])+min(dice[2],dice[3])
    two_face = three_face - max(min(dice[0],dice[5]),min(dice[1],dice[4]),min(dice[2],dice[3]))

    result+=4*three_face
    result+=4*(2*n-3)*two_face
    result+=(n-2)*(5*n-6)*one_face


print(result)