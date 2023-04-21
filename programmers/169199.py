from collections import deque
def solution(board):
    n, m = len(board), len(board[0])
    q = deque()
    visited = [[False]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if board[r][c] == "R":
                q.append((r,c,0))
    while q:
        r, c, d = q.popleft()
        if board[r][c] == 'G':
            return d
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r, c
            while 0<=nr+dr<n and 0<=nc+dc<m and board[nr+dr][nc+dc]!="D":
                nr, nc = nr+dr, nc+dc
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and board[nr][nc]!="D":
                visited[nr][nc] = True
                q.append((nr,nc,d+1))
    return -1