def solution(survey, choices):
    cnt = dict(zip('RTCFJMAN',[0]*8))
    for s, c in zip(survey, choices):
        if c<4:
            cnt[s[0]] += 4-c
        else:
            cnt[s[1]] += c-4
    res = ""
    for a, b in [['R','T'],['C','F'],['J','M'],['A','N']]:
        if cnt[a]>=cnt[b]:
            res += a
        else:
            res += b
    return res