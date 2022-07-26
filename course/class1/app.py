import pyautogui as pg
import pyperclip as pc
import time
import os
import pandas as pd

pg.PAUSE = 0.5
DO_DAYLY = False 

def enter():
    pg.press('win')
    time.sleep(1)
    pg.write('opera')
    pg.press('enter')
    time.sleep(1)
    pc.copy('artigo.app')
    pg.hotkey('ctrl','v')
    pg.press('enter')
    time.sleep(5)
    pg.click(x=840, y=192)
    
    if DO_DAYLY:
        dayly()
    else:
        random()
    
def random():
    pg.click(x=1098, y=700)
    pg.click(x=1063, y=626)
    pg.click(x=785, y=368)
    pg.click(x=840, y=192)
    time.sleep(5)
    
def dayly():
    pass

def get_position():
    os.system('cls')
    time.sleep(5)
    print(pg.position())

def do():
    pd.read_e
    
enter()
#get_position()