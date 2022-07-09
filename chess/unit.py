class Unit:
    
    def __init__(self, type):
        self.type = type
        self.move = self.set_move(type)
    
    def set_move(self,type):
        #1-pawns 2-bishops 3-knights 4-hooks 5-queen 6-king  
        move_set = None
        
        if type == 1:    
            move_set = [ [1],
                         [2],
                         [1,1] ]
            
        return move_set