board=['-','-','-',
       '-','-','-',
       '-','-','-']
def display_board():
    print(board[0]+ '|'+board[1]+'|'+board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])
def playgame():
    #Display Initial Board
    display_board()
    handleturn()
def handleturn():
    position=input('Choose your position between 1-9: ')
    position=int(position)-1
    board[position]="X"
    display_board()
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