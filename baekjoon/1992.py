n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
res = ""

def dfs(sr,er,sc,ec):
    global res
    total = sum(sum(arr[r][sc:ec]) for r in range(sr,er))
    if total == 0:
        res += "0"
    elif total == (er-sr)**2:
        res += "1"
    else:
        res += "("
        hr = sr+(er-sr)//2
        hc = sc+(ec-sc)//2
        dfs(sr,hr,sc,hc)
        dfs(sr,hr,hc,ec)
        dfs(hr,er,sc,hc)
        dfs(hr,er,hc,ec)
        res += ")"

dfs(0,n,0,n)

print(res)