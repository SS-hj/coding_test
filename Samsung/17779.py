from collections import defaultdict
n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
mindiff = 1e9

def make_index(x, y, d1, d2):
    # 딕셔너리로 해당 행 열 어디부터 어디까지인지
    d = defaultdict(list)
    index = set()
    for i in range(d1+1):
        d[x + i].append(y - i)
        d[x + d2 + i].append(y + d2 - i)
    for i in range(d2+1):
        d[x + i].append(y + i)
        d[x + d1 + i].append(y - d1 + i)
    # 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구
    for r in d:
        a = d[r]
        for c in range(min(a),max(a)+1):
            index.add((r,c))
    return index

def cal(x, y, d1, d2):
    global mindiff
    cnt = [0, 0, 0, 0, 0]
    area5 = make_index(x, y, d1, d2)
    for r in range(1, n+1):
        for c in range(1, n+1):
            if (r,c) in area5:                          # 5번 선거구
                cnt[4] += A[r-1][c-1]
            elif 1 <= r < x+d1 and 1 <= c <= y:         # 1번 선거구
                cnt[0] += A[r-1][c-1]
            elif 1 <= r <= x+d2 and y < c <= n:         # 2번 선거구
                cnt[1] += A[r-1][c-1]
            elif x+d1 <= r <= n and 1 <= c < y-d1+d2:   # 3번 선거구
                cnt[2] += A[r-1][c-1]
            else:                                       # 4번 선거구
                cnt[3] += A[r-1][c-1]
    mindiff = min(mindiff, max(cnt)-min(cnt))

for x in range(1, n+1):
    for y in range(1, n+1):
        # 기준점 (x, y)
        d1 = 1
        while 1<=d1<=y:
            d2 = 1
            while 1<=d2<=n-y and d1+d2<=n-x:
                cal(x, y, d1, d2)
                d2 += 1
            d1 += 1

print(mindiff)