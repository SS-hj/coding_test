n = int(input())
arr = sorted(map(int, input().split()))
visit = {}

cnt = 0
for i in range(n):
    if arr[i] in visit:
        if visit[arr[i]]: # 이전에 가능하다고 처리됐었으면
            cnt += 1
    # 아직 방문 안했으면
    else:
        start, end = 0, n-1
        while start<end:
            mid = arr[start]+arr[end]
            if mid<arr[i] or i==start:
                start += 1
            elif mid>arr[i] or end==i:
                end -= 1
            else:
                cnt += 1
                visit[arr[i]] = True
                break
        else:
            visit[arr[i]] = False
print(cnt)