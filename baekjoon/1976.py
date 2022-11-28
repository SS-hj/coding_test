n = int(input())
m = input()
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
parent = list(range(n))

def find_parent(x):
    return x if parent[x] == x else find_parent(parent[x])

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            union(i, j)
            
check = find_parent(plan[0]-1)
for i in plan[1:]:
    p = find_parent(i-1)
    if check == p:
        check = p
    else:
        print("NO")
        break
else:
    print("YES")