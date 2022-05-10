'''
하나의 줄기 세포는 가로, 세로 크기가 1인 정사각형 형태로 존재
!!생명력이라는 수치!!
초기 - 줄기 세포들은 비활성 상태
!!활성화된 줄기 세포는 첫 1시간 동안 상, 하, 좌, 우 네 방향으로 동시에 번식
!!두 개 이상의 줄기 세포가 하나의 그리드 셀에 동시 번식하려고 하는 경우 생명력 수치가 높은 줄기 세포가 해당 그리드 셀을 혼자서 차지
----입력
초기 상태에서 줄기 세포가 분포된 영역의 넓이는 세로 크기 N, 가로 크기 M (1≤N≤50, 1≤M≤50)
배양 시간 K (1≤K≤300)
줄기 세포의 초기 상태 정보
*줄기 세포의 생명력 X(1≤X≤10)
----출력
K시간 후 살아있는 줄기 세포(비활성 상태 + 활성 상태)의 총 개수
*비활성 상태 + 활성 상태 == 총 줄기세포 - 죽은 줄기세포
'''
dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())

for t in range(1, T + 1):
    n, m, k = map(int, input().split())
    # !리스트 범위 설정 주의!
    # live; 생명력의 정보 ; 죽은 세포는 -1로표현, 0은 아무것도 안 담긴 상태
    live = [[0] * (m + 2 * k + 2) for _ in range(n + 2 * k + 2)]
    # check; 활성과 비활성 상태 ; 양수에는 활성화 상태, 음수에는 비활성 상태, 0은 안 담기거나 죽은 상태
    check = [[0] * (m + 2 * k + 2) for _ in range(n + 2 * k + 2)]
    for i in range(n): # 한 행씩 데이터를 처리
        data = list(map(int, input().split()))
        for j in range(m):
            live[i][j] = data[j] # live에 저장
            if data[j] > 0:
                check[i][j] = -(data[j]) # 초기에는 전부 비활성 상태

    for _ in range(k):
        l = [[0] * (m + 2 * k + 2) for _ in range(n + 2 * k + 2)]
        for i in range(n + 2 * k + 2):
            for j in range(m + 2 * k + 2):
                if live[i][j] == 0 or live[i][j] == -1:
                    continue
                if check[i][j] < 0:
                    if check[i][j] == -1:
                        check[i][j] = live[i][j] # 비활성 -> 활성
                    else:
                        check[i][j] += 1
                elif check[i][j] > 0:
                    x, y = i, j
                    for p in range(4):
                        nx = (x + dx[p]) % (n + k * 2 + 2)
                        ny = (y + dy[p]) % (m + k * 2 + 2)
                        # 죽거나 원래 세포가 존재하는 곳이 아닌 곳
                        if live[nx][ny] == -1 or live[nx][ny] > 0:
                            continue
                        # 그곳에 아무것도 존재하지 않는다면 해당 곳에 생명력값을 넣어주고 비활성상태로
                        if l[nx][ny] == 0:
                            l[nx][ny] = live[x][y]
                            check[nx][ny] = -live[x][y]
                        # 죽은세포나 원래 세포가 존재하진 않지만 새로운 세포가 생명력이 크다면 변경
                        elif l[nx][ny] < live[x][y]:
                            l[nx][ny] = live[x][y]
                            check[nx][ny] = -live[x][y]
                    # 번식한 새 세포들 말고, 기존의 세포의 업데이트 사항 #
                    # 활성상태가 1이라면 다음은 죽은 세포로 변경되므로 값을 live에 죽은세포(-1) 값, check에 죽은 세포(0)으로 변경
                    if check[i][j] == 1:
                        live[i][j] = -1
                        check[i][j] = 0
                    else:
                        check[i][j] -= 1
        # 모든 행과 열을 돌아서 세포 번식 한 정보를 담은 l 리스트로 기존 생명력을 담은 live에 갱신
        for i in range(n + 2 * k + 2):
            for j in range(m + 2 * k + 2):
                if l[i][j] > 0 and live[i][j] == 0:
                    live[i][j] = l[i][j]

    cnt = 0
    for i in range(n + 2 * k + 2):
        for j in range(m + 2 * k + 2):
            if check[i][j] != 0:
                cnt += 1
    print('#'+str(t), cnt)