def solution(A, B):
    res = ''

    while A + B > 0:
        if A == 0:
            return 'b'*B + res
        elif B == 0:
            return res + 'a'*A
        elif A > B:
            res += 'aab'
            A -= 2
            B -= 1
        elif A == B:
            return res + 'ab'*A
        else:
            res += 'abb'
            A -= 1
            B -= 2
            
    return res