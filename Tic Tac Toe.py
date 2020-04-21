#Global Variables
#Game Board
board=['-','-','-',
       '-','-','-',
       '-','-','-']
#Game Is not Done
gameIsOn=True
#Winner or Tie
Winner=None
#Current Player
currentJocky="X"
def display_board():
    print(board[0]+ '|'+board[1]+'|'+board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
def playgame():
    #Display Initial Board
    display_board()
    while gameIsOn:
        handleturn(currentJocky)
        checkIfGameDone()
        changeJocky()
        #Endgame
    if Winner=="X" or Winner=="0":
        print(Winner + " Won.")
    elif Winner==None:
        print("Tie")
def handleturn(player):
    print(player + "'s turn")
    position=input('Choose your position between 1-9: ')
    valid=False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid! Choose a position from 1-9: ")
        position=int(position)-1
        if board[position] == "-":
            valid = True
        else:
            print("Choose different place!")
    board[position]=player
    display_board()
def checkIfGameDone():
    CheckWin()
    CheckTie()
def CheckWin():
    global Winner
    #check Rows
    rowwin=rowcheck()
    #Check Columns
    colwin=colcheck()
    #Check Diagonals
    diagonalwin=diagonalcheck()
    if rowwin:
        Winner=rowwin
    elif colwin:
        Winner=colwin
    elif diagonalwin:
        Winner=diagonalwin
    else:
        Winner=None
    return
def rowcheck():
    global gameIsOn
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        gameIsOn=False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return
def colcheck():
    global gameIsOn
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        gameIsOn = False
    if col1:
        return board[0]
    if col2:
        return board[1]
    if col3:
        return board[2]
    return
def diagonalcheck():
    global gameIsOn
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        gameIsOn = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return
def CheckTie():
    global gameIsOn
    if '-' not in board:
        gameIsOn=False
    return
def changeJocky():
    global currentJocky
    if currentJocky =="X":
        currentJocky="0"
    elif currentJocky =="0":
        currentJocky="X"
    return

playgame()
#board
#display board
#play game
#handle turns
# check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player
#GGGGGGG