from collections import deque

n,m = map(int,input().split())
arr=[[0]*n for _ in range(n)]
graph = [[]*n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    graph[r-1].append(c-1)
    graph[c-1].append(r-1)

def dfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if i!=start and not arr[start][i]:
                queue.append(i)
                arr[start][i]+=(arr[start][now]+1)

for i in range(n):
    dfs(i)

answer=[0]*n
for i in range(n):
    answer[i]=sum(arr[i])
    
print(answer.index(min(answer))+1)