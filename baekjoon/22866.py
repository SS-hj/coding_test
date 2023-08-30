import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

res = [[0,0] for _ in range(n)]

left = []   # 건물 높이 기준에 따른 (높이, 인덱스)
# left
for i in range(n):
    while left and left[-1][0]<=arr[i]:
            left.pop()
    if left:
        res[i] = [len(left), left[-1][1]]
    left.append((arr[i],i+1))
    
right = []
# right
for i in range(n-1,-1,-1):
    while right and right[-1][0]<=arr[i]:
            right.pop()
    if right:
        if res[i][0]==0 or i+1-res[i][1]>right[-1][1]-(i+1):
            res[i][1] = right[-1][1]
        res[i][0] += len(right)
    right.append((arr[i],i+1))
    
for a, b in res:
    if a==0:
        print(0)
    else:
        print(a,b)