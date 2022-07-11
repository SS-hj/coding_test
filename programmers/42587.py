from collections import deque

def solution(priorities, location):
    end = (priorities[location],location)
    q = deque(priorities)
    check = deque()
    [check.append(i) for i in range(len(priorities))] 
    res = []
    while q:
        checker = q.popleft()
        c = check.popleft()
        if not q or checker >= max(q):
            res.append((checker,c))
        else:
            q.append(checker)
            check.append(c)
    return res.index(end)+1