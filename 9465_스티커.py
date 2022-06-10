# 스티커는 위 아래 좌우 연속해서 사용할 수 없다
# (50) 10 (100) 20  40
#  30 (50) 70   10 (60)
# 예제의 경우 이렇게 선택하는 경우가 최대의 경우이다.
# 동적계획법을 이용하여 n번째의 최댓값을 구한다
# 1)n-1번째에서 대각선으로 선택
# 2)n-2번째에서 대각선으로 선택
# 최종적으로 0행과 1행의 마지막 값을 비교하여 더 큰 경우가 최댓값이 된다.

t = int(input()) #테스트 케이스의 개수

for _ in range(t):
    n = int(input()) #스티커의 개수는 총 2n개
    score =[]
    for _ in range(2):
        score.append(list(map(int,input().split())))
    if n>1:    
        score[0][1] += score[1][0]
        score[1][1] += score[0][0]
        for i in range(2,n):
            score[0][i] = max(score[1][i-2]+score[0][i],score[1][i-1]+score[0][i])
            score[1][i] = max(score[0][i-2]+score[1][i],score[0][i-1]+score[1][i])
    print(max(score[0][-1],score[1][-1]))