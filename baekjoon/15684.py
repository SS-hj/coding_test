# i번 세로선의 결과가 i번이 나와야
# 두 가로선이 연속하거나 서로 접하면 안 된다. 
# 추가해야 하는 가로선 개수의 최솟값
n, m, h = map(int, input().split())

def check(y, x):
    for i in range(x, h):
        if not line[y][i]:
            continue
        else:
            if y < n-1 and line[y+1][i]:
                check(y+1, i)
            else:
                check(y-1, i)
            break
    else:
        return y
    
def dfs(y):
    for x in range(h):
        if y == 0:
            if line[y][x] or line[y+1][x]:
                continue
            else:
                line[y][x] = 1
                line[y+1][x] = 1
        elif y > 0 and line[y][x] or line[y+1][x]:
            continue
        else:
            line[y][x] = 1
            line[y+1][x] = 1
            break
    else:
        return False # there's no line to change
    return True

if not m:
    print(0)
else:
    line = [[0]*h for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        line[b-1][a-1] = 1
        line[b][a-1] = 1
    cnt = 0
    for i in range(n-1):
        if check(i) != i:
            dfs(i)
    print(cnt)

[[1, 0, 0, 0, 1, 0], 
 [1, 0, 1, 0, 1, 0], 
 [0, 1, 1, 0, 0, 0], 
 [0, 1, 0, 0, 1, 0], 
 [0, 0, 0, 0, 1, 0]]