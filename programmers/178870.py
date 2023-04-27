def solution(sequence, k):
    start, end, check = 0,0,sequence[0]
    n = len(sequence)
    rs, re = 0, n-1
    while end < n:
        if check==k and re-rs>end-start:
            rs, re = start, end
        if check > k:
            check -= sequence[start]
            start += 1
        else:
            end += 1
            if end<n:
                check += sequence[end]
    return [rs, re]