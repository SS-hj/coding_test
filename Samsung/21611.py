from collections import deque

n, m = map(int, input().split())
sr, sc = n//2, n//2
arr = [list(map(int, input().split())) for _ in range(n)]
t = [list(map(int, input().split())) for _ in range(m)]

# 달팽이 인덱스 리스트 생성
dir = [(0,-1), (1,0), (0,1), (-1,0)]
move = []
r, c = sr, sc
num, k = 1, 0
while num < n:
    for _ in range(2):
        for _ in range(num):
            r, c = r+dir[k%4][0], c+dir[k%4][1]
            move.append((r,c))
        k+=1
    num += 1
for _ in range(num-1):
    r, c = r+dir[k%4][0], c+dir[k%4][1]
    move.append((r,c))

ans = [0,0,0,0]

q = deque()

dir = [(-1,0), (1,0), (0,-1), (0,1)]
def magic(d, s):
    global arr
    r, c = sr, sc
    for _ in range(s):
        r, c = r+dir[d][0], c+dir[d][1]
        arr[r][c] = 0
        
def blast():
    global q
    global ans
    # 빈공간 메우기 & 4개 이상 연속시 구슬 폭발
    check = True
    cnt = 0
    while check and q:
        st = []
        num = q[0]
        cnt = 0
        check = False
        while q:
            x = q.popleft()
            if num!=x:
                if cnt >= 4:
                    check = True
                    ans[st[-1]] += cnt
                    while cnt:
                        st.pop()
                        cnt -= 1
                cnt = 0
                num = x
            cnt += 1
            st.append(x)
        for x in st: # 빈공간 메우기
            q.append(x)
    if cnt >= 4:    # 4개 이상이면서 다른 값을 안만나고 끝난 경우 (예외처리)
        ans[st[-1]] += cnt
        while cnt:
            q.pop()
            cnt -= 1
        
def change(num, cnt, res):
    global arr
    global q

    while q:
        x = q.popleft()
        if num!=x:
            res.append(cnt)
            res.append(num)
            num = x
            cnt = 0
        cnt += 1
    res.append(cnt)
    res.append(num)

    idx = 0
    for x in res:
        if idx>n*n-2:
            break
        r, c = move[idx]
        arr[r][c] = x
        idx += 1
    else: # break 안됐으면
        for i in range(idx, n*n-1):
            r, c = move[i]
            arr[r][c] = 0

for d, s in t:
    # 구슬 파괴
    magic(d-1,s)
    
    for r, c in move: # 빈공간 메우기
        if arr[r][c]>0:
            q.append(arr[r][c])
            
    # 빈공간 메우기 & 4개 이상 연속시 구슬 폭발 
    blast()
        
    # 구슬 변화 (연속하는 그룹)
    if q:   # 구슬이 있다면
        change(q[0], 0, [])

print(ans[1]+2*ans[2]+3*ans[3])