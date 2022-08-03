def solution(dirs):
    visited = set() # 중복 제거 <= 가본 길을 제외하기 위하여 사용
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x,y,nx,ny)) # 현재 위치 -> 이동 후 위치
            visited.add((nx,ny,x,y)) # 양방향 고려
            x, y = nx, ny # 이동 위치로 현재 위치 변경
    return len(visited)//2 # visited를 2로 나눴을 때 몫이 처음 걸어본 길이