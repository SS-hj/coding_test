import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(n):
    a, *temp, _ = map(int, input().split())
    for k in range(0,len(temp),2):
        adj[a].append((temp[k],temp[k+1]))

res, node = 0, 0
def move(now, d):
    global res, node
    for next, dist in adj[now]:
        if not visited[next]:
            visited[next] = True
            move(next, d+dist)
    if d > res:
        res = d
        node = now

visited = [False]*(n+1)
visited[1] = True
move(1, 0)

visited = [False]*(n+1)
visited[node] = True
move(node, 0)

print(res)