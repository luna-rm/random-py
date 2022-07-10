class Unit:
    
    idF = 0
    idT = 0
    
    def __init__(self, type, side):
        self.type = type
        self.move = []
        self.id = 0

        if side == False:
            self.id = self.idF
            self.idF += 1
            
        elif side == True:
            self.id = self.idT
            self.idT += 1
        
        
