def solution(s, skip, index):
    arr = sorted(set('abcdefghijklnmopqrstuvwxyz')-set(skip))
    n = len(arr)
    check = dict(zip(arr,range(n)))
    res = ""
    for a in s:
        l = check[a]+index
        if l>=n:
            l %= n
        res += arr[l]
    return res