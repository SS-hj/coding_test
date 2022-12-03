def solution(k, d):
    cnt = 0; check = d**2
    for x in range(0,d+1,k):
        y = int((check - x**2)**0.5)
        cnt += y//k+1
    return cnt