# 별 찍는 재귀 함수
def draw_star(n) :
    global s
    
    if n == 3 :
        s[0][:3] = s[2][:3] = [1]*3
        s[1][:3] = [1, 0, 1]
        return

    a = n//3
    
    # 3 X 3 뭉텅이 단위로 가로 먼저 채우고
    # 다음 줄 넘어가 가로로 채우는 식
    # 작은 범위들 먼저 채우고 그 다음 제곱 재귀함수를 호출하게 됨
    draw_star(n//3)
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 : # 빈공간 생성하도록
                continue
            for k in range(a) :
                s[a*i+k][a*j:a*(j+1)] = s[k][:a] # 핵심 아이디어

N = int(input())      

# 메인 데이터 선언
s = [[0] * (N) for _ in range(N)]

draw_star(N)

for i in s :
    for j in i :
        if j : # 1 이면 *
            print('*', end = '')
        else : # 0 이면 공백
            print(' ', end = '')
    print()