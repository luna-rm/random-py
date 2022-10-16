from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyshadow.main import Shadow
import os
import time
import pandas as pd

word = 'areio';
ansr = [-1,-1,-1,-1,-1]
answ = [-1,-1,-1,-1,-1]
ansg = [-1,-1,-1,-1,-1]
words = []
                                                    
def get_word():
    table = pd.read_excel('words.xlsx')
    table = table.sample(frac = 1)
    list = table.values
    
    for word in list:
        right = True
        word = word[0].split('/')
        word = word[0]
        
        if len(word) != 5:
            continue

        word = word.replace('ã','a')
        word = word.replace('á','a')
        word = word.replace('â','a')
        word = word.replace('í','i')
        word = word.replace('ç','c')  

        for aux in range(5):
            if ansr[aux] == -1:
                pass
            elif word[aux] != ansr[aux]:
                right = False
            
            if word[aux] == answ[aux]:
                right = False
                
            if answ[aux] == -1:
                pass
            elif not answ[aux] in word:
                right = False
            
            if ansg[aux] == -1:
                pass
            elif ansg[aux] in word:
                right = False
            
            if word in words:
                right = False
                
        if right:
            print(word)
            words.append(word)
            return word
                
                                                    
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

os.system('cls')
print('run')

nav = webdriver.Firefox()
shadow = Shadow(nav)
nav.get('https://term.ooo')

nav.find_element('xpath', '/html/body/wc-modal/div').click()

for aux_main in range(6):
    nav.find_element('xpath', '/html/body').send_keys(word)
    nav.find_element('xpath', '/html/body').send_keys(Keys.ENTER)
    time.sleep(5);
    change_rules(aux_main, word);
    word = get_word()

        


