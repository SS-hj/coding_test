n, k = map(int, input().split())
arr = list(map(int, input().split()))
step = 0
cnt = 0
visited = [False]*n

# 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
while cnt < k:
    step += 1
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    arr = [arr[-1]] + arr[:-1]
    visited = [False] + visited[:-2] + [False]
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    for i in range(n-2,-1,-1):
        # 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상
        if visited[i] and not visited[i+1] and arr[i+1]>=1:
            visited[i] = False
            visited[i+1] = True
            arr[i+1] -= 1
            if arr[i+1]==0: 
                cnt += 1
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if arr[0]:
        visited[0] = True
        arr[0] -= 1
        if arr[0]==0: 
            cnt += 1
print(step)