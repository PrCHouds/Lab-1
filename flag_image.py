import math as m
RED = '\u001b[48;5;124m'
GREEN = '\u001b[48;5;22m'
END = '\u001b[0m'
SIZE = 15
OFFSET = 4

for i in range(SIZE):
    if (0 < i < SIZE) and (i <= SIZE//2):
        print(f'{GREEN}{"  " * (SIZE - OFFSET - i)}{RED}{'  '* 2*i}{GREEN}{"  "*(SIZE+ OFFSET - i)}{END}')
    elif (0 < i < SIZE) and (i > SIZE//2):
        print(f'{GREEN}{"  " * (SIZE -OFFSET- (SIZE-1-i))}{RED}{'  '* 2*(SIZE-1-i)}{GREEN}{"  "*(SIZE+ OFFSET- (SIZE-1-i))}{END}')
    else:
        print(f'{GREEN}{"  " * (2*SIZE)}{END}')