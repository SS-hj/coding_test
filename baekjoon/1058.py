n = int(input())
arr = [list(input()) for _ in range(n)]
graph = [[1e9]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        elif arr[i][j] == "Y":
            graph[i][j] = graph[j][i] = 1 # 양방향 처리

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

maxCnt = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i==j:
            continue
        if 0 <= graph[i][j] <= 2:
            cnt += 1
    maxCnt = max(maxCnt, cnt)
    
print(maxCnt)