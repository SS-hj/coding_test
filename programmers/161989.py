from collections import deque
def solution(n, m, section):
    cnt = 0
    q = deque(section)
    while q:
        v = q.popleft()
        cnt += 1
        while q and q[0] < v+m:
            q.popleft()
    return cnt