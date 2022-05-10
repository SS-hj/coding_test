
'''
5가지 테트로미노 중 하나를 NxM 종이에 적절히 놓아서
테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성
* 이때 테트로미노는 회전, 대칭 가능

모든 노드들 마다 이를 돌면서 최대값을 리턴
1. 현재 노드의 상하좌우를 살펴 최대값에 연결
2. 다음 노드에서도 이를 계속적으로
----입력
N, M  (4 ≤ N, M ≤ 500)
N개의 줄에 종이에 쓰여 있는 수 ( <=1000)
----출력
max(칸에 쓰여 있는 수들의 합)
'''

import sys
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans # 결과값 변수
    # 현재의 dfs에서 남은 블록이 모두 최대값에 해당하더라도, 현재 ans를 넘기지 못한다면 미리 종료
    if ans >= total + max_val * (3 - idx):
        return
    # 4개의 블록을 모두 사용했으면
    if idx == 3:
        # 현재의 dfs 한 값과 이전까지의 최대값(ans)을 비교하여 더 큰 값을 반환하고 종료
        ans = max(ans, total)
        return
    # 4개의 블록을 아직 다 사용하지 않았다면
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 이동 위치가 배열안에 있고, 방문한 적이 없다면
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                # 2개의 블록을 선택한 상황이라면
                # 기존 블럭에서 탐색하도록 하여 ㅗ 모양을 만들수있도록
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc]) # 방문처리 장소에서 dfs 재귀호출
                    visit[nr][nc] = 0
                visit[nr][nc] = 1 # 방문처리
                dfs(nr, nc, idx + 1, total + arr[nr][nc]) # 방문처리 장소에서 dfs 재귀호출
                visit[nr][nc] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr)) # 2차원 arr 배열의 최대값 구하기

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)