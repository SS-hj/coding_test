def solution(m, n, board):
    cnt = 0
    turn = True
    board = [list(board[r]) for r in range(m)]
    def check(turn):
        turn = False
        visited = set()
        for r in range(m-1):
            for c in range(n-1):
                if board[r][c] and board[r][c]==board[r][c+1]==board[r+1][c]==board[r+1][c+1]:
                    visited.add((r,c))
                    visited.add((r,c+1))
                    visited.add((r+1,c))
                    visited.add((r+1,c+1))
        if visited:
            delete(visited)
            turn = True
        return turn
    def delete(visited):
        nonlocal cnt
        for r, c in visited:
            cnt += 1
            board[r][c] = ''
        for c in range(n):
            temp = []
            for r in range(m):
                if board[r][c]:
                    temp.append((board[r][c]))
                    board[r][c] = ''
            for r in range(m-1,-1,-1):
                if not temp:
                    break
                board[r][c] = temp.pop()
    while turn:
        turn = check(turn)
    return cnt