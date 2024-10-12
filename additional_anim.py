import os
import time

GRAY = '\u001b[48;5;245m'
END = '\u001b[0m'
RED = '\u001b[41m' 
YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'

Colors = [RED,YELLOW,GREEN]
Traffic_Size = 5

def light(color):
    for i in range(Traffic_Size):
        if i < 1 or i > 3:
            print(f'\t{"  "*(Traffic_Size//4)}{color}{"  "*(Traffic_Size//2 + 1)}{END}')
        else: 
            print(f'\t{color}{"  "*Traffic_Size}{END}')
    print('\n')
        
while True:
    for cadr in range(3):
        if cadr == 0:  
            light(RED)
            light(GRAY)
            light(GRAY)
        if cadr == 1:
            light(GRAY)
            light(YELLOW)
            light(GRAY)
        if cadr == 2:
            light(GRAY)
            light(GRAY)
            light(GREEN)
        time.sleep(1)
        os.system("cls")