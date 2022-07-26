import pyautogui as pg
import pyperclip as pc
import time
import os
import pandas as pd

#pg.PAUSE = 0.1
DO_RANDOM = False 
PATH = r'words.xlsx'

def start():
    pg.press('win')
    time.sleep(1)
    
    pg.write('opera')
    time.sleep(1)
    
    pg.press('enter')
    time.sleep(1)
    
    pc.copy('artigo.app')
    time.sleep(1)
    
    pg.hotkey('ctrl','v')
    time.sleep(1)
    
    pg.press('enter')
    time.sleep(5)
    
    pg.click(x=840, y=192)
    time.sleep(1)
    
    if DO_RANDOM:
        random()
    
    pg.click(x=840, y=192)
    time.sleep(1)
    
    do()
    
def random():
    pg.click(x=1098, y=700)
    time.sleep(1)
    
    pg.click(x=1063, y=626)
    time.sleep(1)
    
    pg.click(x=785, y=368)
    time.sleep(1)
    
    pg.click(x=840, y=192)
    time.sleep(5)

def get_position():
    os.system('cls')
    time.sleep(5)
    print(pg.position())
    
def do():
    table = pd.read_excel(PATH)
    list = table.values
    print(list)
    for word in list:
        word = word[0].split('/')
        print(word[0])
        pc.copy(str(word[0]))
        pg.hotkey('ctrl','v')
        pg.press('enter')
    
start()
#get_position()
#do()