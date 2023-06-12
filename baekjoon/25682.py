n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
res = 1e9

arr1 = [[0]*(m+1) for _ in range(n+1)] # i+j가 짝수일 때 흑
arr2 = [[0]*(m+1) for _ in range(n+1)] # i+j가 홀수일 때 흑
for i in range(1,n+1):
    for j in range(1,m+1):
        if ((i+j) % 2 == 0 and board[i-1][j-1] == 'B') or ((i+j) % 2 == 1 and board[i-1][j-1] == 'W'):
            arr1[i][j] = arr1[i-1][j] + arr1[i][j-1] - arr1[i-1][j-1]
            arr2[i][j] = arr2[i-1][j] + arr2[i][j-1] - arr2[i-1][j-1] + 1
        else:
            arr1[i][j] = arr1[i-1][j] + arr1[i][j-1] - arr1[i-1][j-1] + 1
            arr2[i][j] = arr2[i-1][j] + arr2[i][j-1] - arr2[i-1][j-1]
for i in range(k, n+1):
    for j in range(k, m+1):
        res = min(res, arr1[i][j] - arr1[i-k][j] - arr1[i][j-k] + arr1[i-k][j-k])
        res = min(res, arr2[i][j] - arr2[i-k][j] - arr2[i][j-k] + arr2[i-k][j-k])
        
print(res)