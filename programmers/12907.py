def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    
    for num in money: # !! 무조건 money를 먼저 해야한다.
        for i in range(num,n+1):
            dp[i] += dp[i-num]
                
    return dp[-1]%1000000007