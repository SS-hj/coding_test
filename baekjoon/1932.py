n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1,0,-1):
    for j in range(i):
        arr[i-1][j] += max(arr[i][j], arr[i][j+1])
        
print(arr[0][0])