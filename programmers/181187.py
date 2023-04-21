import math
def solution(r1, r2):
    cnt = 0
    x1, x2 = r1*r1, r2*r2
    for x in range(1, r2+1):
        d = x*x
        if x1>=d:
            y1 = (x1-d)**0.5
        else:
            y1 = 0
        y2 = (x2-d)**0.5
        cnt += int(y2)-math.ceil(y1)+1
    return cnt*4