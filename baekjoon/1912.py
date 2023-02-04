n = int(input())
arr = list(map(int, input().split()))

maxSum = 0
res = [max(arr)]
for n in arr:
    maxSum += n
    if maxSum >= 0:
        res.append(maxSum)
    else:
        maxSum = 0
print(max(res))