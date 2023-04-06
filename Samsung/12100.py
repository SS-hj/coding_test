from collections import deque
from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0
def up(A):
    for c in range(n):
        q = deque()
        alreadySum = False
        for r in range(n):
            if A[r][c]:   # 빈칸이 아닐 경우
                if q and not alreadySum and q[-1]==A[r][c]:
                    q.append(A[r][c]+q.pop())
                    alreadySum = True
                else:
                    q.append(A[r][c])
                    alreadySum = False
        for r in range(n):
            if q:
                A[r][c] = q.popleft()
            else:
                A[r][c] = 0
    return A

def down(A):
    for c in range(n):
        q = deque()
        alreadySum = False
        for r in range(n-1,-1,-1):
            if A[r][c]:   # 빈칸이 아닐 경우
                if q and not alreadySum and q[-1] == A[r][c]:
                    q.append(A[r][c] + q.pop())
                    alreadySum = True
                else:
                    q.append(A[r][c])
                    alreadySum = False
        for r in range(n-1,-1,-1):
            if q:
                A[r][c] = q.popleft()
            else:
                A[r][c] = 0
    return A

def left(A):
    for r in range(n):
        q = deque()
        alreadySum = False
        for c in range(n):
            if A[r][c]:  # 빈칸이 아닐 경우
                if q and not alreadySum and q[-1] == A[r][c]:
                    q.append(A[r][c] + q.pop())
                    alreadySum = True   # 이미 합쳐진 블록
                else:
                    q.append(A[r][c])
                    alreadySum = False
        for c in range(n):
            if q:
                A[r][c] = q.popleft()
            else:
                A[r][c] = 0
    return A

def right(A):
    for r in range(n):
        q = deque()
        alreadySum = False
        for c in range(n-1,-1,-1):
            if A[r][c]:  # 빈칸이 아닐 경우
                if q and not alreadySum and q[-1] == A[r][c]:
                    q.append(A[r][c] + q.pop())
                    alreadySum = True
                else:
                    q.append(A[r][c])
                    alreadySum = False
        for c in range(n-1,-1,-1):
            if q:
                A[r][c] = q.popleft()
            else:
                A[r][c] = 0
    return A

def dfs(A, k):
    global res
    if k==5:
        for i in range(n):
            res = max(res, max(A[i]))
    else:
        dfs(up(deepcopy(A)), k+1)
        dfs(down(deepcopy(A)), k+1)
        dfs(right(deepcopy(A)), k+1)
        dfs(left(deepcopy(A)), k+1)

dfs(arr, 0)

print(res)