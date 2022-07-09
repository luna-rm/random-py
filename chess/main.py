import unit
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
    
    #space = unit(0)
    pawn = unit.unit(1)
    
    for aux1 in range(8):
        for aux2 in range(8):
            board[aux1][aux2] = pawn
            
    #for aux in range(8):

#call
create_units()
load_board()