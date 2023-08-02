n, K = map(int,input().split())
color = [[] for _ in range(K)]
for _ in range(n):
    x,y,k = map(int,input().split())
    color[k-1].append((x,y))
minRes = 1e9

def dfs(k,minr,minc,maxr,maxc):
    global minRes
    res = (maxr-minr)*(maxc-minc)
    if res>=minRes:
        return
    if k>=K:
        minRes = min(minRes,res)
        return
    for r,c in color[k]:
        dfs(k+1,min(minr,r),min(minc,c),max(maxr,r),max(maxc,c))
    
for r,c in color[0]:
    dfs(1,r,c,r,c)
    
print(minRes)