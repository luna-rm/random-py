import random
import os

cont = True
results = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

def show():
    bigger = [0,0]
    
    print('----')
    for aux in range(1,7):
        print(str(aux)+ ': ' + str(results[aux]))
    print('----')
    for aux in range(1,7):
        if results[aux] != 0:
            if results[aux] > bigger[0]:
                bigger[1] = aux
                bigger[0] = results[aux]
    
    if bigger[0] != 0:
        print('B: ' + str(bigger[1]))
    
def roll(asr):
    for _ in range(asr):
        roll = random.randint(1,6)
        #print(roll)
        results[roll] += 1

def stop():
    global cont
    cont = False

os.system('cls')
    
while cont:
    show()
    
    asr = input()
    
    os.system('cls')    
    
    if asr == 'e':
        stop()
        exit

    roll(int(asr))
