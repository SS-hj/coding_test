def solution(sticker):
    n = len(sticker)
    if n==1:
        return sticker[0]
    dp1 = [0] * n
    dp2 = [0] * n
    for i in range(n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    for i in range(1, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])
    return max(dp1[-2], dp2[-1])