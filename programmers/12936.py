import math
def solution(n, k):
    if n == 1: return [1]
    arr = [i for i in range(1,n+1)]; res = []
    for i in range(n-1,-1,-1):
        t = math.factorial(i)
        if k%t!=0:
            res.append(arr.pop(k//t))
        else:
            res.append(arr.pop(k//t-1))
        k = k%t
    return res