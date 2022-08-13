from collections import deque
def solution(msg):
    res = []; num = 27; q = deque(msg); temp = q.popleft()
    d = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,27)))
    while q:
        while q and temp in d:
            temp = temp + q.popleft()
        if temp not in d:
            res.append(d[temp[:-1]])
            d[temp] = num
            num += 1
            temp = temp[-1]
    if temp: res.append(d[temp]) # 남아있는 문자 압축처리
    return res