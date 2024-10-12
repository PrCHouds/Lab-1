BLACK = '\u001b[40m'
WHITE = '\u001b[48;5;255m'
END = '\u001b[0m'
def loop_symbol(k):
    print(f'{BLACK}{"  "*5}{WHITE}{"  "*2}{END}'*k)
    print(f'{BLACK}{"  "}{WHITE}{"  "*3}{BLACK}{"  "}{WHITE}{"  "*2}{END}'*k)
    print(f'{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "*3}{WHITE}{"  "*2}{END}'*k)
    print(f'{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "}{WHITE}{"  "*4}{END}'*k)
    print(f'{BLACK}{"  "}{WHITE}{"  "}{BLACK}{"  "*5}{END}'*k)
loop_symbol(7)

