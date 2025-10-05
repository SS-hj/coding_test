n = int(input())
s = [int(input()) for _ in range(n)]
# 가장 긴 부분증가수열을 구하면 됨
dp = [1]*n

for i in range(n):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(n-max(dp))