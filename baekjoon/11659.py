import sys
input = sys.stdin.readline

_, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_list = [0]
total = 0
for a in arr:
    total += a
    sum_list.append(total)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i - 1])