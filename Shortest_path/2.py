import sys
input=sys.stdin.readline

# n: 회사의 개수, m: 경로의 개수
n, m = map(int,input().split())

INF = int(1e9)
# 2차원 리스트를 생성, 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 양방향 간선 연결
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

x, k = map(int,input().split())

# 플로이드 워셜 점화식 사용하여 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# 1번 -> k번 -> x번 가는 최소 이동시간
d = graph[1][k] + graph[k][x]

# 불가능 하면 -1 출력
if d >= INF:
    print(-1)
else:
    print(d)