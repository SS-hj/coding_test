import sys
n = int(sys.stdin.readline())
temp = []
for _ in range(n):
	check = sys.stdin.readline().rstrip()
	size = len(temp)
	if check=="pop":
		if size:
			print(temp.pop())
		else:
			print(-1)
	elif check=="size":
		print(size)
	elif check=="empty":
		if size==0:
			print(1)
		else:
			print(0)
	elif check=="top":
		if size:
			print(temp[-1])
		else:
			print(-1)
	else:
		temp.append(int(check.split()[-1]))
