
def drawBoard(board,s):
    x=0
    print ('Column:', end='')
    for i in range(0, s):
        print('{:^5}'.format(str(i+1)), end='')
    print()
    for i in range (0,s):
        print ('Row'+ str(i+1)+ ': ', end='|')
        for j in range (0,s):
            print ('{:^4}'.format(str(board[i][j])), end='|')
        print ()
        print ('      ', end='')
        print ('|'+'-----'*(s-1) + '----' +'|')
        x=x+s

size = int(input("Size of grid?(X * X)"))
board=[['-' for i in range (0,size)]for j in range(0,size)]

drawBoard(board,size)

def XMove():
    x = [None] * 2
    print('Player1:')
    x[0] = int(input("Column to put X?"))
    x[1] = int(input("Row to put X?"))
    return x

def OMove():
    o = [None] * 2
    print('Player2:')
    o[0] = int(input("Column to put O?"))
    o[1] = int(input("Row to put O?"))
    return o

def check_rows(board, size, i):
    Ostreak = 0
    Xstreak = 0
    win = [None] * 2
    win[0] = size + 1
    win[1] = size + 1
    for j in range(0, size):

        if (board[i][j] == 'O'):
            Ostreak = Ostreak + 1

        if (board[i][j] == 'X'):
            Xstreak = Xstreak + 1

        if (Xstreak == size):
            win[0] = i
            return win
        if (Ostreak == size):
            win[1] = i
            return win
    return win

def almost_rows(board, size, i):
    Ostreak = 0
    Xstreak = 0
    win = [None] * 2
    win[0] = size + 1
    win[1] = size + 1
    for j in range(0, size):

        if (board[i][j] == 'O'):
            Ostreak = Ostreak + 1

        if (board[i][j] == 'X'):
            Xstreak = Xstreak + 1

        if (Xstreak == size-1 or Ostreak == size-1):
            win[0] = i
            win[1] = j
            return win
    return win

def almost_columns(board, size, i):
    Ostreak = 0
    Xstreak = 0
    win = [None] * 2
    win[0] = size + 1
    win[1] = size + 1
    for j in range(0, size):

        if (board[j][i] == 'O'):
            Ostreak = Ostreak + 1

        if (board[j][i] == 'X'):
            Xstreak = Xstreak + 1

        if (Xstreak == size-1 or Ostreak == size-1):
            win[0] = i
            win[1] = j
            return win
    return win



def check_columns(board, size, i):
    Ostreak = 0
    Xstreak = 0
    win = [None]*2
    win[0]=size+1
    win[1]=size+1
    for j in range(0, size):

        if (board[j][i] == 'O'):
            Ostreak = Ostreak + 1

        if (board[j][i] == 'X'):
            Xstreak = Xstreak + 1

        if (Xstreak == size):
            win[0]=i
            return win
        if (Ostreak == size):
            win[1]=i
            return win
    return win


while True:
    #Player 1 chooses place (X)
    while True:
        MX = XMove()
        if (board [MX[1]-1][MX[0]-1] == '-'):
            break
        else:
            print ('Place taken!')
    board [MX[1]-1][MX[0]-1] = 'X'
    drawBoard(board,size)
    for i in range (0,size):
        ro = (check_rows(board, size, i))
        col = (check_columns(board, size, i))
        if (ro[0] != size+1):
            print('Player 1 Wins!ROW'+str(ro[0]+1))
            exit()
        if (col[0] != size+1):
            print ('Player 1 Wins!COLUMN'+str(col[0]+1))
            exit()
    # Player 2 chooses place (O)
    # while True:
    #     OX = OMove()
    #     if (board[OX[1] - 1][OX[0] - 1] == '-'):
    #         break
    #     else:
    #         print ('Place taken!')
    # board[OX[1] - 1][OX[0] - 1] = 'O'
    # drawBoard(board, size)
    # for i in range(0, size):
    #     ro = (check_rows(board, size, i))
    #     col = (check_columns(board, size, i))
    #     if (ro[1] != size + 1):
    #         print('Player 2 Wins!ROW' + str(ro[1] + 1))
    #         exit()
    #     if (col[1] != size + 1):
    #         print('Player 2 Wins!COLUMN' + str(col[1] + 1))
    #         exit()


    while True:
        vb = board
        scoreboard = [[0 for i in range(0, size)] for j in range(0, size)]
        for i in range(0, size):
            for j in range(0, size):
                if (vb[i][j] == '-'):
                    vb[i][j] = 'O'
                    for i in range(0, size):
                        ro = (check_rows(vb, size, i))
                        col = (check_columns(vb, size, i))
                        if (ro[1] != size + 1):
                            print('Player 2 Wins!ROW' + str(ro[0] + 1))
                            exit()
                        if (col[1] != size + 1):
                            print('Player 2 Wins!COLUMN' + str(col[0] + 1))
                            exit()




    #AI?!

