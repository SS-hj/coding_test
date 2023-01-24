n = int(input())
arr = list(map(int,input().split()))
dp = [0]*n
dp[0]=1

for i in range(1,n):
    l = []
    for j in range(i):
        if arr[j]<arr[i]:
            l.append(j)
    try:
        dp[i]=max(dp[k] for k in l)+1
    except:
        dp[i]=1
        
print(max(dp))