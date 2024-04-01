n, m = map(int, input().split())
chicken = []
houses = []
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c]==1:
            houses.append((r,c))
        elif temp[c]==2:
            chicken.append((r,c))

def combinations(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], k-1):
                yield [arr[i]] + next

res = 1e9
for comb in combinations(chicken, m):
    total_dist = 0
    for hr,hc in houses:
        dist = 1e9
        for cr,cc in comb:
            dist = min(dist, abs(hr-cr)+abs(hc-cc))
        total_dist += dist
    res = min(res, total_dist)

print(res)