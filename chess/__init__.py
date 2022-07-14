from units.pawn import Pawn
import os

class Space:
    type = 0

board = [
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
]

def load_board():
    os.system('cls')
    str_board = ''
    for aux1 in range(8):
        for aux2 in range(8):
            str_board = str_board + str(board[aux1][aux2].type) + ' '
        str_board = str_board + '\n'
    
    print(str_board)

def create_units():
    
    for aux0_1 in range(8):
        for aux0_2 in range(8):
            board[aux0_1][aux0_2] = Space()
            
    for aux1 in range(8):
        board[1][aux1] = Pawn(1,True)
        board[6][aux1] = Pawn(1,False)

#call
create_units()
load_board()