n = int(input())
arr = list(map(int, input().split()))
cnt = [0]*n

# 다른 고층 빌딩을 지나거나 접하지 않는 두 선분을 이을 수 있는 경우 => 기울기 계속 커져야 함
for i in range(n-1):
    sx, sy = i, arr[i]
    slope = -1e9
    for j in range(i+1,n):
        nx, ny = j, arr[j]
        ns = (sy-ny)/(sx-nx)
        if slope<ns:
            cnt[i] += 1
            cnt[j] += 1
            slope = ns
            
print(max(cnt))