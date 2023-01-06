n=int(input())
s=[int(input()) for _ in range(n)]
dp =[]

if n < 3:
    print(sum(s))
else:
    dp.append(s[0])
    dp.append(max(s[0]+s[1],s[1]))
    dp.append(max(s[0]+s[2],s[1]+s[2]))
    dp.extend(max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i]) for i in range(3,n))
    print(dp[-1])