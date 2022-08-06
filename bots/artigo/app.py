import pyautogui as pg
import pyperclip as pc
import time
import os
import pandas as pd
from random import shuffle

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
    aux = False
    aux2 = False
    end = False
    table = pd.read_excel(PATH)
    list = table.values
    #shuffle(list)
    
    pg.click(x=840, y=192, button='right')
    time.sleep(1)

    pg.click(x=951, y=581)
    time.sleep(3)
    
    pg.click(x=883, y=289)
    time.sleep(1)
    
    pg.click(x=895, y=306)
    time.sleep(1)
    
    pg.click(x=1089, y=324)
    time.sleep(1)
    
    pg.hotkey('ctrl', 'c')
    
    pg.click(x=264, y=697)
    time.sleep(1)
       
    how_long = pc.paste()
    char_num = ''
    
    for ele in how_long:
        if ele == 'h':
            aux2 = True
            
        if aux2 == True:
            if ele == r'"':
                if aux == False:
                    aux = True
                elif aux:
                    aux = False
                    end = True 
                           
        if aux and end == False:
            #print(ele)

            for num in range(10):
                if ele == str(num):
                    char_num = char_num + ele
    
    print(char_num)
    print(list.shape)
    for word in list:
        word = word[0].split('/')
        if len(word[0]) == int(char_num):
            pass
            #print(word[0]) 

            pc.copy(str(word[0]))
            pg.hotkey('ctrl','v')
            pg.press('enter')  
    
start()
#get_position()
#do()
