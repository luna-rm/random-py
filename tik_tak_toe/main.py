import os
import time
import sys

sys.setrecursionlimit(1500)
end = 0
player = 1
INFINITY = 10000
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0] ]

def load_board():
    os.system('cls')
    
    v_board = [['-','-','-'],
               ['-','-','-'],
               ['-','-','-']]
        
    for aux_row in range(3):
        for aux_lane in range(3):
            if board[aux_row][aux_lane] == 1:
                v_board[aux_row][aux_lane] = 'X'
            elif board[aux_row][aux_lane] == -1:
                v_board[aux_row][aux_lane] = 'O'
            
    
    print(v_board[0][0] + ' ' +  v_board[0][1] + ' ' + v_board[0][2])
    print(v_board[1][0] + ' ' +  v_board[1][1] + ' ' + v_board[1][2])
    print(v_board[2][0] + ' ' +  v_board[2][1] + ' ' + v_board[2][2])
    
def make_play():
    global player
    row = int(input('row? '))
    lane = int(input('lane? '))

    if(row < 4 and row > 0):
        if (lane < 4 and lane > 0):
            if (board[row-1][lane-1] == 0):
                board[row-1][lane-1] = player
                player = -1
                return

    print('invalid input')            
    time.sleep(2.0)
    
def minimax(v_board, depth, maximizing):
    state = verif()
    
    if state == 1:
        #print('aaaaa')
        return -1
    elif state == 2:
        #print('bbbbbbb')
        return 1
    elif state == 3:
        #print('ccc')
        return 0
    
    
    if maximizing:
        best_score = INFINITY
        #score = -INFINITY

        for aux1 in range(3):        
            for aux2 in range(3):    
                if(v_board[aux1][aux2] == 0):
                    v_board[aux1][aux2] = -1
                    score = minimax(v_board, 0, True)
                    v_board[aux1][aux2] = 0

                    if (score < best_score):
                        best_score = score
                
        return best_score
        
    else:
        best_score = -INFINITY
        #score = INFINITY

        for aux1 in range(3):        
            for aux2 in range(3):    
                if(v_board[aux1][aux2] == 0):
                    v_board[aux1][aux2] = 1
                    score = minimax(v_board, 0, False)
                    v_board[aux1][aux2] = 0

                    if (score > best_score):
                        best_score = score
                
        return best_score
        
def comp_play():
    global player
   
    v_board = board
    
    best_score = INFINITY
    best_mov_1 = 0
    best_mov_2 = 0   
    
    for aux1 in range(3):        
        for aux2 in range(3):    
            score = INFINITY
            if(v_board[aux1][aux2] == 0):
                v_board[aux1][aux2] = -1
                score = minimax(v_board, 0, True)
                
                if (score < best_score):
                    best_score = score
                    best_mov_1 = aux1
                    best_mov_2 = aux2
                    
                v_board[aux1][aux2] = 0
                
    print('exisad')
    board[best_mov_1][best_mov_2] = -1
    print(best_score)
    player = 1
    
def win(p):   
    load_board()
    
    if p == 1:
        print('\nPlayer X won!')
    elif p == 2:
        print('\nPlayer 0 won!') 
    elif p == 3:
        print('\nTie!')
    
def verif():
    #vertivcal and horizontal
    for aux1 in range(3):
        aux_win_row = 0
        aux_win_lane = 0
        
        for aux2 in range(3):            
            aux_win_row += board[aux1][aux2]
            aux_win_lane += board[aux2][aux1]
            
            if (aux_win_row == 3 or aux_win_lane == 3):
                return 1
            elif (aux_win_row == -3 or aux_win_lane == -3):
                return 2

    #diagnoal
    if(board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3):
        return 1
    if(board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3):
        return 2

    is_full = True
    for aux1 in range(3):        
        for aux2 in range(3): 
            if board[aux1][aux2] == 0:
                is_full = False
    
    if is_full:
        return 3
            
    return 0

while end == 0:
    load_board()
    if player == 1:
        make_play()
    elif player == -1:
        comp_play()
    end = verif()

win(end)