from collections import deque

A,B,C = sorted(map(int, input().split()))
q = deque()
visited = set()
q.append((A,B,C))
visited.add((A,B,C))

while q:
    a, b, c = q.popleft()
    if a==b==c:
        print(1)
        break
    for i in [(a*2,b-a,c),(a*2,b,c-a),(a,b*2,c-b)]:
        a,b,c = sorted(i)
        if (a,b,c) not in visited:
            q.append((a,b,c))
            visited.add((a,b,c))
      
else:
    print(0)