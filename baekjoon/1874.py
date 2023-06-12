from collections import deque
n = int(input())
arr = deque (list(range(1,n+1)))
res = ["+"]
check = deque()
for _ in range(n):
    check.append(int(input()))
temp = [arr.popleft()]
while check and arr:
    while temp and check and temp[-1]==check[0]:
        res.append("-")
        temp.pop()
        check.popleft()
    if arr:
        res.append("+")
        temp.append(arr.popleft())
while temp and check and temp[-1]==check[0]:
        res.append("-")
        temp.pop()
        check.popleft()

if not check:
	for r in res:
		print(r)
else:
	print("NO")
