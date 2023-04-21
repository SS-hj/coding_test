def solution(N, number):
    dp = [set() for _ in range(9)]
    for cnt in range(1,9):
        for i in range(1,cnt):
            for a in dp[cnt-i]:
                for b in dp[i]:
                    dp[cnt].add(a+b)
                    dp[cnt].add(a*b)
                    if b>0:
                        dp[cnt].add(a//b)
                    dp[cnt].add(a-b)
        dp[cnt].add(int(str(N)*cnt))
        if number in dp[cnt]:
            return cnt
    return -1