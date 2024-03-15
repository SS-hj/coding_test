def solution(scores):
    ca, cb = scores[0]
    n = max(scores)[0]
    std = [0]*(n+1)
    for u, v in scores:
        std[u] = max(std[u], v)
    for i in range(n-1, -1, -1):
        std[i] = max(std[i], std[i+1])
    std.append(0)

    res = 1
    total = ca + cb
    for a, b in scores:
        if ca < a and cb < b:
            return -1
        if a+b > total and b >= std[a+1]:
            res += 1
    return res