def solution(ingredient):
    check = [1,2,3,1]
    arr = []
    res = 0
    for ig in ingredient:
        arr.append(ig)
        if arr[-4:]==check:
            res += 1
            arr.pop()
            arr.pop()
            arr.pop()
            arr.pop()
    return res