import sys
from copy import deepcopy
import heapq
input = sys.stdin.readline

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
checked = {1: deepcopy(arr)}
h = []
heapq.heappush(h, 1)

def mul(a, b):
    A = [[0]*n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            A[r][c] = sum(a[r][i]*b[i][c] for i in range(n))%1000
    return A

now = 1
while now < b:
    for i in range(len(h)-1,-1,-1):
        if now+h[i]<=b:
            arr = mul(deepcopy(arr), deepcopy(checked[h[i]]))
            now += h[i]
            checked[now] = deepcopy(arr)
            heapq.heappush(h, now)
            break

for r in range(n):
    for c in range(n):
        print(arr[r][c]%1000, end=" ")
    print()