import sys
input=sys.stdin.readline
import heapq

v, e = map(int,input().split())
k = int(input())

INF = int(1e9)
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(v+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (v+1)

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(e): # 간선의 개수 동안
    # x에서 y로 갈 때, 가중치 w
    x, y, w = map(int, input().split())
    graph[x].append([y, w])

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않으면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드보다 가중치가 크면 무시 (continue)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, d in graph[now]:
            next_dist = dist + d
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(q,(next_dist,next_node))

# 다익스트라 알고리즘 수행
dijkstra(k)
for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])