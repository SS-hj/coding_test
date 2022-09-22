# x, y에서 쿼리를 역으로 적용 (queries를 역순으로 처리 + 공의 이동방향도 반대로)
def solution(n, m, x, y, queries):
    x1, y1, x2, y2, = x, y, x, y
    for d, dx in queries[::-1]:
        if d == 0: # 오른쪽으로 이동
            y2 = m-1 if y2+dx>m-1 else y2+dx
            if y1 != 0: 
                y1 += dx
        elif d == 1: # 왼쪽으로 이동
            y1 = 0 if y1-dx<0 else y1-dx
            if y2 != m-1: 
                y2 -= dx
        elif d == 2: # 아래로 이동
            x2 = n-1 if x2+dx>n-1 else x2+dx
            if x1 != 0: 
                x1 += dx
        else: # 위로 이동
            x1 = 0 if x1-dx<0 else x1-dx
            if x2 != n-1: 
                x2 -= dx
        # 배열의 크기를 넘어가게 된다면 해당 쿼리로 x, y 좌표에 도달 할 수 없음
        if x1>n or x2<0 or y1>m or y2<0:
            return 0
    return (x2 - x1 + 1) * (y2 - y1 + 1)