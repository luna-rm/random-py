from unit import Unit

class Pawn(Unit):
    
    def move_1_0(self, position_V, position_H, v_board):        
        if v_board[position_V+1][position_H] == 0:
            v_board[position_V][position_H] = 0
            v_board[position_V+1][position_H] = self
            
