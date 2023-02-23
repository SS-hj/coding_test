from collections import deque

def solution(x, y, n):
    q = deque()
    q.append((y, 0))
    while q:
        num, cnt = q.popleft()
        if num==x:
            return cnt
        elif num>x:
            if num%3 == 0:
                q.append((num/3, cnt+1))
            if num%2 == 0:
                q.append((num/2, cnt+1))
            q.append((num-n, cnt+1))
    return -1