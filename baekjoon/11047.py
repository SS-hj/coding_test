n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse = True)
res = 0
for coin in coins:
    if k==0:
        break
    res += k//coin
    k %= coin
    
print(res)