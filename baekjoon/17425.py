import sys
input = sys.stdin.readline

MAX = 1000001
T = int(input())
dp = [0]*MAX

for i in range(1,MAX):
    j = 1
    while i * j < MAX:
        dp[i * j] += i
        j += 1
    dp[i] = dp[i-1]+dp[i]
ans = []

for _ in range(T):
    n = int(input())
    ans.append(dp[n])

print('\n'.join(map(str, ans))+'\n')