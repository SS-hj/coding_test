n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

for c  in range(1, m):
    dp[0][c] += dp[0][c-1]
    
for r in range(1, n):
    l2r = dp[r][:]
    r2l = dp[r][:]
    l2r[0] += dp[r-1][0]
    r2l[m-1] += dp[r-1][m-1]
    for c in range(1, m):
        l2r[c] += max(dp[r-1][c], l2r[c-1])
        r2l[m-c-1] += max(dp[r-1][m-c-1], r2l[m-c])
    for c in range(m):
        dp[r][c] = max(l2r[c],r2l[c])

print(dp[n-1][m-1])