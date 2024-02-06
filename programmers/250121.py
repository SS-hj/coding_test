def solution(data, ext, val_ext, sort_by):
    d = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    answer = [a for a in data if a[d[ext]] < val_ext]
    return sorted(answer, key = lambda x : x[d[sort_by]])