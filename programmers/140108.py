def solution(s):
    cnt1, cnt2 = 0,0
    check = s[0]
    n = len(s)
    res = 0
    for i in range(n):
        if s[i]==check:
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            res += 1
            cnt1, cnt2 = 0, 0
            if i+1<n:
                check = s[i+1]
    if cnt1+cnt2>0:
        res += 1
    return res