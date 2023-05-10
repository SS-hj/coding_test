t = int(input())


for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    d0 = [[0]*n for _ in range(2)]
    d1 = [[0]*n for _ in range(2)]
    d0[0][0] = arr[0][0]
    d1[1][0] = arr[1][0]
    d1[0][1] = d1[1][0] + arr[0][1]
    d0[1][1] = d0[0][0] + arr[1][1]
    for i in range(2):
        for j in range(2,n):
            d0[i][j] = max(d0[1-i][j-1],d0[1-i][j-2]) + arr[i][j]
    print(max(d0))