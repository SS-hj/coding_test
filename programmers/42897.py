def solution(money):
    N = len(money)
    dp1 = [0] * N
    dp2 = [0] * N
    for i in range(N - 1): 
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    for i in range(1, N):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    return max(dp1[-2], dp2[-1])