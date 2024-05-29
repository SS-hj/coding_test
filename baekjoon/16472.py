n = int(input())
arr = list(input())
start, end = 0, 0
res = 0
d = {}

while end < len(arr):
    if arr[end] in d:
        d[arr[end]] += 1
    else:
        d[arr[end]] = 1
    while len(d)>n:
        d[arr[start]] -= 1
        if d[arr[start]] == 0:
            del d[arr[start]]
        start += 1
    end += 1
    res = max(res, end-start)
    
print(res)