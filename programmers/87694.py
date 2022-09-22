def solution(rectangle, characterX, characterY, itemX, itemY):
    MAXNUM = 102
    board = [[0 for j in range(MAXNUM)] for i in range(MAXNUM)]
    for c1, r1, c2, r2 in rectangle : 
        for i in range(2*r1, 2*r2+1) :
            for j in range(2*c1, 2*c2+1) : 
                board[i][j] = 1
    for c1, r1, c2, r2 in rectangle :             
        for i in range(2*r1+1, 2*r2) : 
            for j in range(2*c1+1, 2*c2) :  
                board[i][j] = 0
    chR, chC, itR, itC = 2*characterY, 2*characterX, 2*itemY, 2*itemX
    stack = [(0, chR, chC)]
    while stack : 
        w, chR, chC = stack.pop(0)
        board[chR][chC] = -1
        if board[itR][itC]<0 : return w//2
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)] : 
            if board[chR+dr][chC+dc]>0 : 
                stack.append((w+1, chR+dr, chC+dc))