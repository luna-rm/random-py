import numpy as np
import pandas as pd

def new_key(table):
    letter = "A"
    while letter in table.keys():
        letter = chr(ord(letter) + 1)
    return letter

def f_no(table, key):
    letter = new_key(table)
            
    table[letter] = np.copy(table[key])
    for i in range(len(table[letter])):
        if table[letter][i] == 1:
            table[letter][i] = 0
        else:
            table[letter][i] = 1
    
    return letter, table

def f_or(table, key1, key2):
    letter = new_key(table)
            
    table[letter] = np.copy(table[key1])
    for i in range(len(table[letter])):
        if table[letter][i] == 0 and table[key2][i] == 1:
            table[letter][i] = 1
    
    return letter, table

def f_and(table, key1, key2):
    letter = new_key(table)
            
    table[letter] = np.copy(table[key1])
    for i in range(len(table[letter])):
        if table[letter][i] == 1 and table[key2][i] == 0:
            table[letter][i] = 0
    
    return letter, table

def f_xor(table, key1, key2):
    letter = new_key(table)
            
    table[letter] = np.copy(table[key1])
    for i in range(len(table[letter])):
        if table[letter][i] == 0 and table[key2][i] == 1:
            table[letter][i] = 1
        elif table[letter][i] == 1 and table[key2][i] == 1:
            table[letter][i] = 0
    
    return letter, table

def resol(expre, table, start, end):
    print("\n", end="")
    for ele in expre:
        print(ele, end="")
    print("\n" + str(table))

    if len(expre) == 1:
        return table
    
    for i in range(len(expre)):
        try:
            if expre[i] == "(":
                j = i
                while expre[j] != ")":
                    j += 1
                expre.pop(j)
                expre.pop(i)
                resol(expre[i:j-1], table, start, end)
            if expre[i] == "'":
                new_letter, table = f_no(table, expre[i-1])
                expre.pop(i)
                expre.pop(i-1)
                expre.insert(i-1, new_letter)
            elif expre[i] == "." and expre[i+1] != "(":
                if i+2 < len(expre):
                    if expre[i+2] == "'":
                        continue
                new_letter, table = f_or(table, expre[i-1], expre[i+1])
                expre.pop(i)
                expre.pop(i)
                expre.pop(i-1)
                expre.insert(i-1, new_letter)
            elif expre[i] == "x" and expre[i+1] != "(":
                if i+2 < len(expre):
                    if expre[i+2] == "'":
                        continue
                new_letter, table = f_and(table, expre[i-1], expre[i+1])
                expre.pop(i)
                expre.pop(i)
                expre.pop(i-1)
                expre.insert(i-1, new_letter)
            elif expre[i] == "^" and expre[i+1] != "(":
                if i+2 < len(expre):
                    if expre[i+2] == "'":
                        continue
                new_letter, table = f_xor(table, expre[i-1], expre[i+1])
                expre.pop(i)
                expre.pop(i)
                expre.pop(i-1)
                expre.insert(i-1, new_letter)
        except:
            break
                        
    resol(expre, table, start, end)

print("\ninsert a problem")
print("ex.: A'.(BxC)\n")

DIE = list(input()) 
ESPECIAL_CHAR = [".", "'", "x", "^", "(", ")"]
num_var = [0, []]

for ele in DIE:
    if ele in num_var[1]:
        continue
    if ele in ESPECIAL_CHAR:
        continue
    num_var[1].append(ele)
    num_var[0] += 1

print(num_var)

aux_table = np.zeros((num_var[0], 2**num_var[0]), dtype=int)
for i in range(len(aux_table)):
    for j in range((2**i), len(aux_table[i])):
        if aux_table[i][j-(2**i)] == 0:
            aux_table[i][j] = 1 
            
table = {}#A'.(BxC)

for i in range(num_var[0]):
    table[num_var[1][i]] = aux_table[i]


print(table)

#table = resol(DIE, table, 0, len(DIE))

try:
    resol(DIE, table, 0, len(DIE))
    print()
    print(pd.DataFrame(data=table))    
except Exception as e:
    print()
    print(e)
    print()
    print("\nmelhore.\n")