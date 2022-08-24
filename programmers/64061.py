def solution(board, moves):
    N = len(board); stack = []; cnt = 0
    for m in moves:
        for i in range(N):
            if board[i][m-1]:
                stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
        while len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                cnt += 2
            else: break
    return cnt