def solution(board):
    def win(target):
        checkrow1 = 1 if board[0][0]==target and board[0][0]==board[0][1]==board[0][2] else 0
        checkrow2 = 1 if board[1][0]==target and board[1][0]==board[1][1]==board[1][2] else 0
        checkrow3 = 1 if board[2][0]==target and board[2][0]==board[2][1]==board[2][2] else 0
        checkcol1 = 1 if board[0][0]==target and board[0][0]==board[1][0]==board[2][0] else 0
        checkcol2 = 1 if board[0][1]==target and board[0][1]==board[1][1]==board[2][1] else 0
        checkcol3 = 1 if board[0][2]==target and board[0][2]==board[1][2]==board[2][2] else 0
        checkcross1 = 1 if board[0][0]==target and board[0][0]==board[1][1]==board[2][2] else 0
        checkcross2 = 1 if board[0][2]==target and board[0][2]==board[1][1]==board[2][0] else 0
        return checkrow1+checkrow2+checkrow3+checkcol1+checkcol2+checkcol3+checkcross1+checkcross2
    Owin = win("O")
    Xwin = win("X")
    Ocnt = 0
    Xcnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                Ocnt += 1
            elif board[i][j] == "X":
                Xcnt += 1
    return 0 if (Xwin>2 or Owin>2 or (Xwin>=1 and Owin>=1) or Xcnt+2<=Ocnt or Ocnt<Xcnt or (Owin and Ocnt==Xcnt) or (Xwin and Ocnt!=Xcnt)) else 1