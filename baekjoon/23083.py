n, m = map(int, input().split())
k = int(input())
hole = set()
for _ in range(k):
    a, b = map(int, input().split())
    hole.add((a-1,b-1))
d1 = [(-1,1), (0,1), (1,0)] # 짝수일때
d2 = [(0,1), (1,1), (1,0)]  # 홀수일때
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1

for c in range(m):
    for r in range(n):
        d = d2
        if c%2==0:
            d = d1
        for i in range(3):
            nr, nc = r+d[i][0], c+d[i][1]
            if 0<=nr<n and 0<=nc<m and (nr,nc) not in hole:
                dp[nr][nc] += dp[r][c]

print(dp[n-1][m-1]%1000000007)