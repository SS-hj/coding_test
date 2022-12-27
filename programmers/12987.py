def solution(A, B):
    A.sort(reverse=True)
    B.sort()
    score = 0
    for a in A:
        if a < B[-1]:
            score += 1
            B.pop()
    return score