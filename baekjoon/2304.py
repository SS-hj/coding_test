n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()
A = []
res = 0
height = 0
px = 0
idx = 0

for i, (x, y) in enumerate(arr):
    if height <= y:
        res += height*(x-px)
        height = y
        px = x
        idx = i
        
height = 0
px = arr[-1][0]
for i in range(len(arr)-1,idx-1,-1):
    x, y = arr[i]
    if height <= y:
        res += height*(px-x)
        height = y
        px = x
res += height        

print(res)