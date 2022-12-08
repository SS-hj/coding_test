def solution(k, ranges):
    res = []
    temp = k
    while k > 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = k*3 + 1
        a = min(temp, k)
        b = max(temp, k)
        res.append(a+(b-a)/2)
        temp = k
    n = len(res)
    ans = []
    for start, end in ranges:
        end += n
        if start < end:
            ans.append(sum(res[start:end]))
        elif start == end:
            ans.append(0.)
        else:
            ans.append(-1.)
    return ans