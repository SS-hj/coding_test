def solution(genres, plays):
    n = len(plays)
    d = dict(zip(genres, [0]*n))
    for g, p in zip(genres,plays):
        d[g] += p
    arr = list(zip(genres,plays,range(n)))

    sortedArr = sorted(arr, key = lambda x : (-d[x[0]], -x[1], x[2]))
    cnt = dict(zip(genres, [0]*n))
    res = []
    for genre, _, i in sortedArr:
        if cnt[genre] < 2:
            res.append(i)
            cnt[genre] += 1
    return res