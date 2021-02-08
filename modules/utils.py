import os

def Last_Num(table):
    if table == []:
        last_num = 1
    else:
        firstkey = list(table[0].keys())[0] #first key should always be the ID
        last_num = int((table[-1][firstkey]))
        last_num += 1
    return str(last_num)

def Clear(): #clears the screeen
    os.system("clear")