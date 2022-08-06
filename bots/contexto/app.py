from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import random
import os

def do():
    table = pd.read_excel('words.xlsx')
    table = table.sample(frac = 1)
    list = table.values
    
    for word in list:
        word = word[0].split('/')
        word = word[0]
        #print(word)
        
        nav.find_element('xpath', '/html/body/div/div/form/input').send_keys(word)
        nav.find_element('xpath', '/html/body/div/div/form/input').send_keys(Keys.ENTER)
        
        time.sleep(0.75)
        
        text = nav.find_element('xpath', '/html/body/div/div/form/input').get_attribute('value')

        for _ in text:
            nav.find_element('xpath', '/html/body/div/div/form/input').send_keys(Keys.BACK_SPACE)


os.system('cls')

nav = webdriver.Firefox()
nav.get('https://contexto.me/')

do() 


    
