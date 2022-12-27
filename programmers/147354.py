def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col-1], -x[0]))
    res = 0
    for i in range(row_begin-1, row_end):
        res = res ^ sum([num%(i+1) for num in data[i]])
    return res