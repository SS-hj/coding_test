def solution(m, n, puddles):
    map = [[0]*n for _ in range(m)]
    for p in puddles:
        x,y = p
        map[x-1][y-1] = -1
    def dfs(r,c):
        if r<0 or c<0 or map[r][c] < 0: return 0
        if map[r][c] > 0: return map[r][c]
        # 각 칸에 출발지점에서 해당 지점까지 오는 경우의 수를 계산
        map[r][c] = (dfs(r,c-1) + dfs(r-1,c))%1000000007
        return map[r][c]
    map[0][0] = 1 # 출발하는 경우 1
    return dfs(m-1,n-1) # 최종 도착지점까지 오는 경우의 수