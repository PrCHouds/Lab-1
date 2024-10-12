import math as mt
RED = '\u001b[48;5;124m'
GREEN = '\u001b[48;5;22m'
END = '\u001b[0m'

with open('sequence.txt', 'r') as file:
    l = [abs(float(i)) for i in file.readlines()]
a = sum(l[:125]) 
b = sum(l[125:])
first_percent = mt.ceil(a/(a+b)*100)
second_percent = int(b/(a+b)*100)
print(f'{RED}{"  "}{END} - {first_percent} - процент суммы модулей первых 125 чисел')
print(f'{GREEN}{"  "}{END} - {second_percent} - процент суммы модулей следующих 125 чисел')
print(f'{RED}{" "*first_percent}{GREEN}{" "*second_percent}{END}')