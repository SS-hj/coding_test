def solution(A, B, C):
    A, B, C = str(format(A,'b')).zfill(30), str(format(B,'b')).zfill(30), str(format(C,'b')).zfill(30)
    acnt, bcnt, ccnt, abcnt, accnt, bccnt, abccnt = 0,0,0,0,0,0,0
    for a, b, c in zip(A,B,C):
        if a == '0':
            acnt += 1
        if b == '0':
            bcnt += 1
        if c == '0':
            ccnt += 1
        if a == '0' and b == '0':
            abcnt += 1
        if a == '0' and c == '0':
            accnt += 1
        if b == '0' and c == '0':
            bccnt += 1
        if a == '0' and b == '0' and c == '0':
            abccnt += 1
    
    return 2**acnt + 2**bcnt + 2**ccnt - 2**abcnt - 2**accnt - 2**bccnt + 2**abccnt