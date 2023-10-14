def solution(targets):
    answer = 1
    targets.sort()
    end = targets[0][-1]
    for ns, ne in targets:
        if ns>=end:
            answer += 1
            end = ne
        elif ne<end:
            end = ne
    return answer