def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    n = len(score)-1
    check = m-1
    while check <= n:
        answer += score[check]*m
        check += m
    return answer