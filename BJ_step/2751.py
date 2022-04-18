n = int(input())
arr = []
for _ in range(n):
    arr += [int(input())]
    
arr.sort()

for i in arr:
    print(i)