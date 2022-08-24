def solution(gems):
    size = len(set(gems)) ; N = len(gems)
    dic = {gems[0]:1}
    temp = [0, N - 1]
    start , end = 0, 0
    while True:
        if len(dic) == size:
            if end - start < temp[1] - temp[0]:
                temp = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == N: break
            if gems[end] in dic:
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    return [temp[0]+1, temp[1]+1]