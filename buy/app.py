import pandas as pd
import os

df = pd.read_excel('list.xlsx')
base_list = df.values
list = []

for ele in base_list:
    aux = False
    aux_list = True
    ele = ele[0].split(' ')
    num = ''
    what = ''
    for part in ele:
        if not aux:
            num = part
            aux = True
        else:
            what = what + ' ' + part
    
    #change
    while aux_list:
        os.system('cls')
        print(str(num) + ' ' + what)
        print('\nn = next | d = delete | v = add | c = decrease')
        ans = input()
        if ans == 'n':
            list.append(num + ' ' + what)
            aux_list = False
        elif ans == 'd':
            pass
            aux_list = False
        elif ans == 'v':
            value = input('num: ')
            try:
                num = int(num) + int(value)
                
                print('confirm?  ' + str(num) + ' ' + what)
                yn = input ('n to cancel')
                if (yn != 'n'):
                    list.append(str(num) + ' ' + what)
                    aux_list = False
            except Exception as e:
                pass
            
        elif ans == 'c':
            value = input('num: ')
            try: 
                num = int(num) - int(value)
                
                print('confirm?  ' + str(num) + ' ' + what)
                yn = input ('n to cancel')
                if (yn != 'n'):
                    list.append(str(num) + ' ' + what)
                    aux_list = False
            except Exception as e:
                pass

os.system('cls')   
for ele in list:
    print(ele)