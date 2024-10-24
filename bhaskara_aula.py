from math import sqrt

a = float(input('Digite o valor a: '))
b = float(input('Digite o valor b: '))
c = float(input('Digite o valor c: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('Não possui raizes reais')
else:
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) / (2 * a )
    if delta == 0:
        print(f'Possui somente uma raiz: {raiz1:.2f}')
    else:
        print(f'Raiz 01: {raiz1:.2f}')
        print(f'Raiz 02: {raiz2:.2f}')

