board = {1:' ',2:' ',3:' ',
         4:' ',5:' ',6:' ',
         7:' ',8:' ',9:' '}

def printBoard(board):
    print()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    #print('---------')

#printBoard(board)


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def checkForDraw(board):
    for key in board.keys():
        if board[key]==' ':
            return False
    return True


def checkForWin(board):
    if board[1]==board[2] and board[1]==board[3] and board[1]!=' ':
        return True
    if board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    if board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True

    if board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    if board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    if board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True

    if board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    if board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    return False


def insertLetter(position, letter):
    if spaceIsFree(position):
        board[position] = letter

        if checkForWin(board):
            print(letter+' wins!')
            exit()

        if checkForDraw(board):
            print("That's a tie!")
            exit()

    else:
        print('That position is not free!\nPlease try another position: ')
        position= int(input())
        insertLetter(position)


def playerMove():
    position = int(input('Enter position for X: '))
    insertLetter(position,'X')

def botMove():
    position = int(input('Enter position for O: '))
    insertLetter(position, 'O')

printBoard(board)

while not checkForWin(board):
    playerMove()
    printBoard(board)
    botMove()
    printBoard(board)