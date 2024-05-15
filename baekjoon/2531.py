n, d, k, c = map(int, input().split())
temp = [int(input()) for _ in range(n)]
arr = temp*2

while len(arr) < k*2:
    arr.extend(temp)

res = []
for i in range(n):
    temp = set(arr[i:i+k])
    if c in temp:
        res.append(len(temp))
    else:
        res.append(len(temp)+1)

print(max(res))