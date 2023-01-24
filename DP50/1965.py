n = int(input())
arr = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    temp = [dp[j] for j in range(i) if arr[j] < arr[i]]
    temp.append(0)
    dp[i] += max(temp)
            
print(max(dp))