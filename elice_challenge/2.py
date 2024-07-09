_, m = map(int, input().split())
arr = list(map(int, input().split()))
res = []

for _ in range(m):
    i, j, k = map(int, input().split())
    res.append(sorted(arr[i-1:j])[k-1])

for i in range(m):
    print(res[i])