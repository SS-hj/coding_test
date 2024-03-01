n, k = map(int, input().split())
arr = list(map(int, input().split()))
check = [0] * (max(arr) + 1)
start = 0
res = 0

for end in range(n):
    if check[arr[end]] >= k:
        res = max(res, end-start)
        while check[arr[end]]==k:
            check[arr[start]] -= 1
            start += 1
    check[arr[end]] += 1
res = max(res, end-start+1)

print(res)