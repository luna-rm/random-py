from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyshadow.main import Shadow
import os
import time
import random
import pandas as pd

word = 'areio';
ansr = [-1,-1,-1,-1,-1]
answ = [-1,-1,-1,-1,-1]
ansg = [-1,-1,-1,-1,-1]
aux = 0
                                                    
def get_list():
    table = pd.read_excel('words.xlsx')
    table = table.sample(frac = 1)
    list = table.values
    
    for word in list:
        word = word[0].split('/')
        word = word[0]
        
        if word.leght != 5:
            pass
        
        print(word)
                                                    
def change_rules(aux_main, w):
    for aux_cr in range(5):
        ele = shadow.find_element("div#hold>wc-row[termo-row='"+str(aux_main)+"']>div[lid='"+str(aux_cr)+"']").get_attribute('class')
        print(ele)
        if 'right' in ele:
            ansr[aux_cr] = w[aux_cr]
            print(ansr)
        if 'place' in ele:
            answ[aux_cr] = w[aux_cr]
            print(answ)
        if 'wrong' in ele:
            ansg[aux_cr] = w[aux_cr]
            print(ansg)

#calc()

os.system('cls')
print('run')

nav = webdriver.Firefox()
shadow = Shadow(nav)
""" nav.get('https://term.ooo')

nav.find_element('xpath', '/html/body/wc-modal/div').click()

for aux_main in range(6):
    
    nav.find_element('xpath', '/html/body').send_keys(word)
    nav.find_element('xpath', '/html/body').send_keys(Keys.ENTER)
    time.sleep(5);
    change_rules(aux_main, word);  """
get_list();

        


