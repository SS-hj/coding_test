from collections import deque

def solution(m, n, board):
    cnt = 0
    arr = [list(b) for b in board]
    while True:
        temp = set()
        for r in range(m-1):
            for c in range(n-1):
                if arr[r][c] and arr[r][c]==arr[r+1][c]==arr[r][c+1]==arr[r+1][c+1]:
                    temp.update([(r,c),(r+1,c),(r,c+1),(r+1,c+1)])
        if not temp:
            break
        for r, c in temp:
            arr[r][c] = ""
            cnt += 1
        for c in range(n):
            temp = deque()
            for r in range(m-1,-1,-1):
                if arr[r][c]:
                    temp.append(arr[r][c])
            for r in range(m-1,-1,-1):
                try:
                    arr[r][c] = temp.popleft()
                except:
                    arr[r][c] = ""
    return cnt