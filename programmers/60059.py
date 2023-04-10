def solution(key, lock):
    m = len(key)
    n = len(lock)
    key_check = []
    lock_check = set()
    for r in range(m):
        for c in range(m):
            if key[r][c]==1:
                key_check.append((r,c))
    for r in range(n):
        for c in range(n):
            if lock[r][c]==0:
                lock_check.add((r,c))
    k = len(lock_check)

    # 열쇠는 회전과 이동이 가능
    for _ in range(4):
        for r in range(-m, n+m):
            for c in range(-m, n+m):
                cnt = 0
                for kr,kc in key_check:
                    nr,nc = kr+r, kc+c
                    # 자물쇠 영역을 벗어나지 않은 부분만 영향을 줌
                    if 0<=nr<n and 0<=nc<n:
                        # 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치
                        if (nr,nc) in lock_check:
                            cnt += 1
                        # 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됨
                        else:
                            break
                else:
                    # 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 함
                    if k==cnt:
                        return True
        # 회전
        for i in range(len(key_check)):
            r, c = key_check[i]
            key_check[i] = (c, m-1-r)
            
    return False