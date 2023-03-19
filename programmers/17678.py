from collections import deque
def solution(n, t, m, timetable):
    res = 0
    q = deque(sorted(int(t[:2])*60+int(t[3:]) for t in timetable))
    bustime = 540-t
    while q and n>0:
        bustime += t
        n -= 1
        getOn = m
        while q and getOn>0 and q[0]<=bustime:
            res = q.popleft() - 1
            getOn -= 1
    if n+getOn > 0: # 탈 수 있는 사람이 더 있는데 이미 전원 탑승되있는 경우
        res = bustime
    elif q and res==q[0]:
        res -= 1
    return str(res//60).zfill(2)+":"+str(res%60).zfill(2)