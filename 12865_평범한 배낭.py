n,k = map(int,input().split()) #물품의 수 n, 가방에 최대 담을 수 있는 무게 k

wv = [[0,0]] #각 물건의 무게(w)와 물건의 가치(v)를 저장할 배열
for i in range(n):
    wv.append(list(map(int,input().split())))
#1번 index부터 n번 index까지 차례로 물건의 정보를 저장

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
#동적 계획법을 이용하여 문제 풀이
#가방의 무게가 1일 경우, 2일 경우, ... n-1일 경우 최대의 가치를 구하여
#이를 이용하여 최종적으로 가방의 무게가 n일 경우 최대 가치를 구할 수 있다.


for i in range(1,n+1): #첫번째 물품부터 n번째 물품까지의 반복문
    weight = wv[i][0] #i번째 물품의 무게
    value = wv[i][1] #i번째 무품의 가치

    for j in range(k+1): #무게가 j일경우 최대로 넣을 수 있는 물품의 가치를 구하기 위한 반복문
        if weight<=j: #만약 현재(i번째) 물품의 무게가 j 이하이면 가방에 넣을 수 있으므로
            #i번째 물품을 넣거나(weight만큼의 무게가 필요함) 넣지 않는 경우
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][-1])