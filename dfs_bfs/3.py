n, m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# 0인 부분들을 노드라고 봄
def dfs(x,y):
    # 범위를 벗어나는 경우
    if x <=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 방문하지 않은 노드의 경우
    if graph[x][y]==0:
        # 노드 방문처리
        graph[x][y]=1
        # 0과 연결된 상 하 좌 우 부분 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

res=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            print(dfs(i,j),i,j)
            res+=1
print(res)
