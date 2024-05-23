import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dp = [[1]*n for _ in range(n)]

for i in range(n-1):
    if arr[i]!=arr[i+1]:
        dp[i][i+1] = 0
for k in range(n-2):
    for i in range(n-2-k):
        j = i+2+k
        if arr[i]!=arr[j] or dp[i+1][j-1]==0:
            dp[i][j] = 0

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])