from collections import deque
import math
def solution(progresses, speeds):
    progresses = deque(progresses); speeds = deque(speeds); res = []
    temp = [math.ceil((100-progresses.popleft())/speeds.popleft())]
    while progresses:
        speed = math.ceil((100-progresses.popleft())/speeds.popleft())
        if temp[0] >= speed:
            temp.append(speed)
        else:
            res.append(len(temp))
            temp = [speed]
    if temp: res.append(len(temp))
    return res