BLACK = '\u001b[40m'
WHITE = '\u001b[48;5;255m'
END = '\u001b[0m'
X_COUNT = 11
for x in range(X_COUNT, 0, -1):
    y = 2*x + 3
    print(f'{y}\t{WHITE}{'  '*(x-1)}{BLACK}{"  "}{WHITE}{'  '* ((X_COUNT-1) - (x-1))}{END}')
for x in range(X_COUNT+1):
    if x == 0:
        print('0\t', end = '')
    else: print(str(x), end = ' ')
