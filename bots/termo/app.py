import pyautogui as pg
import pyperclip as pc
import time
import os
import pandas as pd

pg.PAUSE = 2

def get_list():
    list = []
    df = pd.read_excel('words.xlsx')
    df = df.sample(frac = 1)
    base = df.values
    
    for word in base:
        word = word[0].split('/')
        if len(word[0]) == 5:
            list.append(word[0])
        
    return list

def new_list(list):
    pass

def do():
    list = get_list()
    word = 'areio'
    for _ in range(5):
        pg.write(word)
        pg.press('enter')
        
        time.sleep(1)
        
        for _ in range(5):
            pg.press('backspace')

        time.sleep(5)
        
        list = new_list(list)

def start():
    pg.press('win')
    pg.write('opera')
    pg.press('enter')
    pg.hotkey('ctrl','shift','n')
    pc.copy('https://term.ooo')
    pg.hotkey('ctrl','v')
    pg.press('enter')
    time.sleep(5)
    pg.click(x=1146, y=215) 

    do()

def get_position():
    os.system('cls')
    time.sleep(5)
    print(pg.position())
    
start()
#get_position() 