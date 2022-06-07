n, m = map(int,input().split())
arr = list(map(int,input().split()))
length = len(arr)

res = 0
i = 0
while i < length:
    cnt = arr[i:].count(arr[i])
    res += length - i - cnt
    i += 1
print(res)