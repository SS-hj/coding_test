N, K = map(int, input().split())    # 물품의 수 N, 버틸 수 있는 무게 K
stuff = [[0,0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
    weight, value = stuff[i]
    for j in range(1, K + 1):       # 가능한 무게인 동안
        if j < weight:              # 현재 weight가 지금 가능한 무게 j보다 크면
            # 가장 최근에 업데이트했던 지금 가능한 무게 j에서의 value를 가져옴
            dp[i][j] = dp[i - 1][j]
        else:                       # 현재 weight가 지금 가능한 무게 j보다 작으면
            # 현재 value+지금 가능한 무게 j-weight에서의 value와 비교
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[N][K])