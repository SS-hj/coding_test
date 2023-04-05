T = int(input())

dr = [1,-1,0,0]
dc = [0,0,-1,1]

for t in range(T):
    n = int(input())
    phase1 = dict()
    for _ in range(n):
        c, r, d, k = map(int, input().split())
        phase1[(r*2,c*2)] = (k,d)   # 두배씩 하여 -2000에서 2000으로 좌표 범위 수정 (0.5초간격 처리하도록)
    total = 0
    for time in range(4001):
        if not phase1:
            break
        boom = set()
        phase2 = dict()
        for r, c in phase1:
            k, d = phase1[(r,c)]
            nr, nc = r+dr[d], c+dc[d]
            if (nr, nc) in boom:    # 현재 시간에 충돌한 원자들이 있는 좌표인 경우
                total += k          # 현재 원자도 같이 충돌하여 에너지 방출
            elif (nr,nc) in phase2: # 원자들 출동 사고
                total += phase2[(nr,nc)][0]+k   # 충돌된 원자들 에너지 방출
                boom.add((nr,nc))   # 원자들 출동 사고 기록
                del phase2[(nr,nc)] # 충돌한 원자들은 소멸
            else:
                phase2[(nr,nc)] = (k,d) # 충돌 안한 경우 0.5초 뒤의 원자 정보 입력
        phase1 = phase2
    print(f"#{t+1} {total}")
