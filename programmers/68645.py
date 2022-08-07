def solution(n):
    ans = [[0 for j in range(i)] for i in range(1, n+1)] # 삼각형
    # 처음 x +1로 되기 때문에 0, 0 이 되려면 -1, 0에서 시작
    x, y = -1, 0 ; num = 1 
    for i in range(n):
        for j in range(i,n):
            if i%3==0: # 아래로
                x+=1
            elif i%3==1: # 오른쪽으로
                y+=1
            else: # 위로
                x-=1
                y-=1
            ans[x][y] = num
            num += 1
    return sum(ans, []) # 2차원 배열을 1차원으로 변환