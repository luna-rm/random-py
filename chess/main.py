from Unit import Unit
import os

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
    
    space = Unit(0)
    pawn = Unit(1)
    
    for aux0_1 in range(8):
        for aux0_2 in range(8):
            board[aux0_1][aux0_2] = space
            
    for aux1 in range(8):
        board[1][aux1] = pawn
        board[6][aux1] = pawn

#call
create_units()
load_board()