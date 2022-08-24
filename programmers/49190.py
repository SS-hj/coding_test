from collections import defaultdict
def solution(arrows):
    d = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    x, y = 0, 0; adj = defaultdict(list); cnt = 0
    for i in arrows:
        for _ in range(2): # 기존 좌표에 없는 (1.5,1.5) 와 같은 교차를 판단하기위해 2번씩 진행
            nx, ny = x + d[i][0], y + d[i][1]
            # 해당 vertex는 이미 처리되었지만, edge는 처음인 경우에 cnt += 1
            if (nx,ny) in adj and (nx,ny) not in adj[(x,y)]:
                cnt += 1
            adj[(x,y)].append((nx,ny))
            adj[(nx,ny)].append((x,y))
            x, y = nx, ny
    return cnt