def solution(t, p):
    cnt = 0
    n = len(p)
    check = int(p)
    for i in range(len(t)-n+1):
        if int(t[i:i+n]) <= check:
            cnt+=1
    return cnt