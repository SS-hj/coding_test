n, m = map(int,input().split())

parent = [i for i in range(n+1)]
graph = [[0,0]]

def find_parent(x):
    return x if parent[x] == x else find_parent(parent[x])

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(n):
    graph.append(list(map(int,input().split())))
    
for i in range(m):
    a, b = map(int,input().split())
    union_parent(a, b)
    
temp = []
for a in range(1, n+1):
    for b in range(a+1, n+1):
        if find_parent(a) != find_parent(b):
            x1, y1 = graph[a]
            x2, y2 = graph[b]
            cost = ((x1-x2)**2 + (y1-y2)**2)**0.5
            temp.append((cost, a, b))

temp.sort()

res = 0
for cost, a, b in temp:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += cost
        
print(format(res,".2f"))