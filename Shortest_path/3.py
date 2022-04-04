import sys
input=sys.stdin.readline
import heapq

# n: 도시의 개수, m: 통로의 개수, c: 메시지를 보내는 도시
n, m, c = map(int,input().split())

INF = int(1e9)
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # x에서 y로 갈 때, 걸리는 시간 z
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않으면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘 수행
dijkstra(c)
cnt = 0
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(n+1):
    if distance[i] != INF:
        cnt+=1
    else:
        distance[i] = 0

# 시작 노드는 제외해야 하므로, cnt-1을 출력 
print(cnt-1, max(distance))