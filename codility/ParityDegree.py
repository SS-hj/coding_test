def solution(N):
    res, k = 0, 0
    while N >= 2**k:
        if N % (2**k) == 0:
            res = k
        k += 1
    return res