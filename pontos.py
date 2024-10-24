import math

x1 = float(input('Digite o valor para x1: '))
y1 = float(input('Digite o valor para y1: '))
x2 = float(input('Digite o valor para x2: '))
y2 = float(input('Digite o valor para y2: '))

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if d >= 10:
    print('longe')
else:
    print('perto')