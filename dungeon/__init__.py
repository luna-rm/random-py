import map

x = 4
y = 1
map.MAP[x][y] = 'x'


def move(side):
    global x
    global y
    
    if side == 'a':
        if [x-1][y] != '.':
            return
        
        map.MAP[x][y] = '.'
        x =- 1
        map.MAP[x][y] = 'x'
        
    elif side == 'w':
        if [x][y+1] != '.':
            return
        
        map.MAP[x][y] = '.'
        y =+ 1
        map.MAP[x][y] = 'x'
        
        
    elif side == 's':
        if [x-1][y-1] != '.':
            return
        
        map.MAP[x][y] = '.'
        x =- 1
        y =- 1
        map.MAP[x][y] = 'x'
    elif side == 'd':
        if [x-1][y-1] != '.':
            return
        
        map.MAP[x][y] = '.'
        x =- 1
        y =- 1
        map.MAP[x][y] = 'x'
    
#w = [][-1][]
#a = [][][-1]
#s = [][+1][]
#d = [][][+1]
while True:
    map.show_map()
    action = input('move: ')
    move(action)