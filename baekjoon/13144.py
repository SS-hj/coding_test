n = int(input())
arr = list(map(int, input().split()))
cnt = 0

visited = set()
start = 0
for end in range(n):
    while arr[end] in visited:
        cnt += len(visited)
        visited.remove(arr[start])
        start += 1
    visited.add(arr[end])
    
l = len(visited)
for _ in range(start,n):
    cnt += l
    l -= 1

print(cnt)