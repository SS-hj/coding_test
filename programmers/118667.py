from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(), deque()
    n = len(queue1)
    target = (sum(queue1)+sum(queue2))//2
    for i in range(n):
        q1.append(queue1[i])
        q2.append(queue2[i])
    cnt = 0
    check = sum(q1)
    while check != target:
        if cnt > n*3:
            return -1
        cnt += 1
        if check > target:
            check -= q1[0]
            q2.append(q1.popleft())
        else:
            check += q2[0]
            q1.append(q2.popleft())
    return cnt