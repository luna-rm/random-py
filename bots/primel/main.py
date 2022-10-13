from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random

primes = []
next_num = 12347
ansr = [-1,-1,-1,-1,-1]
answ = [-1,-1,-1,-1,-1]
ansg = [-1,-1,-1,-1,-1]
aux = 0

def get_num():
    for ioooo in range(9):
        ioooo = ioooo+1
        if (ansr[0] != -1 and ioooo != ansr[0] or ioooo == answ[0]):
            pass
        else:  
            for oiooo in range (10):
                if (ansr[1] != -1 and oiooo != ansr[1] or oiooo == answ[1]):
                    pass 
                else:      
                    for ooioo in range(10):
                        if (ansr[2] != -1 and ooioo != ansr[2] or ooioo == answ[2]):
                            pass
                        else:
                            for oooio in range(10):
                                if (ansr[3] != -1 and oooio != ansr[3] or oooio == answ[3]):
                                    pass
                                else:
                                    for ooooi in range(10):
                                        if (ansr[4] != -1 and ooooi != ansr[4] or ooooi == answ[4]):
                                            pass
                                        else:
                                            num = str(ioooo)+str(oiooo)+str(ooioo)+str(oooio)+str(ooooi)   
                                            contain = True                                         
                                            for aux_answ in range(5):
                                                if (answ[aux_answ] != -1 and not str(answ[aux_answ]) in str(num)):
                                                    contain = False
                                            if contain:                                            
                                                prime =  True
                                                for div in range(int(num)//2):
                                                    if (div == 0 or div == 1):
                                                        pass
                                                    elif (int(num)%div == 0):
                                                        prime = False
                                                        
                                                if(prime):
                                                    if (num == '00000' or num == '00001'):
                                                        pass
                                                    else:
                                                        print(num)
                                                        return num
                                                    
def alt_get_num():
    number = [0,0,0,0,0]
    global next_num
    ret = True
    
    for aux_dig in range(5):
        if ansr[aux_dig] != -1:
            number[aux_dig] = ansr[aux_dig]
        else:
            while True:
                kg = False
                dig = random.randint(1,9)
                if dig != answ[aux_dig]:
                    for aux_ansg in range(5):
                        if (ansg[aux_ansg] == dig):
                            kg = True
                if not kg:        
                    number[aux_dig] = dig
                    print(aux_dig)
                    break
            
    num = str(number[0]) + str(number[1]) + str(number[2]) + str(number[3]) + str(number[4])
    
    for div in range(int(num)//2):
        if (div == 0 or div == 1):
            pass
        elif (int(num)%div == 0):
            ret = False        
    
    for aux_answ in range(5):
        if (answ[aux_answ] != -1 and not str(answ[aux_answ]) in str(num)):
            ret = False
    
    if ret:
        print(num) 
        next_num = int(num)
        return
    else:
        alt_get_num()                                         
                                                    
def click(aaa):
    for aux in range(len(aaa)):
        char = aaa[aux]
        #print(char)
        if char == '1':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[1]').click()
        elif char == '2':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[2]').click()
        elif char == '3':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[3]').click()
        elif char == '4':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[4]').click()
        elif char == '5':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[5]').click()
        elif char == '6':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[6]').click()
        elif char == '7':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[7]').click()
        elif char == '8':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[8]').click()
        elif char == '9':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[9]').click()
        elif char == '0':
            nav.find_element('xpath', '/html/body/div/div/div[3]/div[1]/div[10]').click()
            
    nav.find_element('xpath', '/html/body/div/div/div[3]/div[2]/div[1]').click()

def change_rules(aux_main, number):
    number = str(number)
    for aux_cr in range(5):
        if 'green' in nav.find_element('xpath', '/html/body/div/div/div[2]/div['+str(aux_main)+']/div['+str(aux_cr+1)+']').get_attribute('class'):
            ansr[aux_cr] = int(number[aux_cr])
            print(ansr)
        if 'yellow' in nav.find_element('xpath', '/html/body/div/div/div[2]/div['+str(aux_main)+']/div['+str(aux_cr+1)+']').get_attribute('class'):
            answ[aux_cr] = int(number[aux_cr])
            print(answ)
        if 'slate' in nav.find_element('xpath', '/html/body/div/div/div[2]/div['+str(aux_main)+']/div['+str(aux_cr+1)+']').get_attribute('class'):
            ansg[aux_cr] = int(number[aux_cr])
            print(ansg)

""" def calc():
    for i in range(100000):
        prime = True
        for div in range(i//2):
            if (div == 0 or div == 1):
                pass
            elif (i%div == 0):
                prime = False
        
        if(prime):
            primes.append(i)
    
    if 'green' in nav.find_element('xpath', '/html/body/div/div/div[2]/div[1]/div[4]').get_attribute('class'):
        ansr[3] = aaa[3]
        print(ansr)

click('12347')
if 'green' in nav.find_element('xpath', '/html/body/div/div/div[2]/div[1]/div[4]').get_attribute('class'):
    print('aaaaaaaaaaaaa') """

#calc()

os.system('cls')

nav = webdriver.Firefox()
nav.get('https://converged.yt/primel/')

for aux_main in range(6):
    click(str(next_num))
    change_rules(aux_main+1, next_num)
    alt_get_num()
    
    
alt_get_num()
print(next_num)

        


