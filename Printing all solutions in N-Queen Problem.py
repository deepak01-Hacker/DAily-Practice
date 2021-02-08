def isSafe(board,row,col):
    for i in range(col):
        if board[row][i]:
            return False
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] :
            return False
        i -= 1
        j -= 1
    
    i = row 
    j = col

    while j>= 0 and i < 4:
        if board[i][j]:
            return False
        i += 1
        j -= 1
    return True


def queenUtil(board,i,col):
    if col == 4:
        print(board)
    res = False
    for i in range(4):
        if (isSafe(board,i,col)):
            board[i][col] = 1
            res = queenUtil(board,i,col+1)
            board[i][col] = 0
    return res


def NQueen(board):
    queenUtil(board,0,0)

     
