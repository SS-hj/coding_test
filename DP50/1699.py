n = int(input())
dp = [0]*(n + 1)
square = [i * i for i in range(1, 317)] # int(100000**0.5)+1 = 317

for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j]) # 제일 핵심이 되는 dp 식
    dp[i] = min(s) + 1
print(dp[n])