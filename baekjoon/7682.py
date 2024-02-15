bingos = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

while True:
    board = input()
    if board=='end':
        break
    X_win, O_win = 0, 0
    for i, j, k in bingos:
        X_win += board[i] == board[j] == board[k] == "X"
        O_win += board[i] == board[j] == board[k] == "O"
    Xcnt = board.count("X")
    Ocnt = board.count("O")
    if X_win>=1 and O_win==0 and Xcnt==Ocnt+1:
        print('valid')
    elif O_win==1 and X_win==0 and Xcnt==Ocnt:
        print('valid')
    elif X_win+O_win==0 and Xcnt==5 and Ocnt==4:
        print('valid')
    else:
        print('invalid')