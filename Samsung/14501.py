import sys
input=sys.stdin.readline

n = int(input())
# 기간; arr[i][0], 금액; arr[i][1] 
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [0 for i in range(n+1)] # 뒤부터 누적 업데이트 될 상담 금액표

# 맨 뒤부터 0인덱스까지 거꾸로
for i in range(n-1,-1,-1):
    if i + arr[i][0] > n: # 해당 상담을 수행하는 경우, 기간이 n을 넘길 경우
        dp[i] = dp[i+1] # 이전 상담으로 i 업뎃
    else: 
        # arr[i][1] + dp[i + arr[i][0]] => i번째 상담을 하는 경우
        # 해당 상담을 하면 얻을 수 있는 금액 + 해당 상담이 걸리는 기간이 끝난 날의 상담의 금액
        # dp[i+1] => i 번째 상담을 안하는 경우
        dp[i] = max(arr[i][1] + dp[i + arr[i][0]], dp[i+1])

print(dp[0])