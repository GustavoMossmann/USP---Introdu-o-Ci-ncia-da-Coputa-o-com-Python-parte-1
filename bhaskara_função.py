from math import sqrt

 #calculo delta  
def cal_delta(a, b, c):
    delta = b ** 2 - 4 * a * c
    return delta
  
#calcular raiz 01
def calcular_raiz01(delta_f, a, b):
    raiz1 = (-b + sqrt(delta_f)) / (2 * a)
    return raiz1

#calcular raiz 02
def calcular_raiz02(delta_f, a, b):
    raiz2 = (-b - sqrt(delta_f)) / (2 * a)
    return raiz2

#entrada de dados
a = float(input('Digite o valor a: '))
b = float(input('Digite o valor b: '))
c = float(input('Digite o valor c: '))

#calculo delta
delta = cal_delta(a, b, c)

#condições
if delta < 0:
    print('esta equação não possui raízes reais')
else:
    if delta == 0:
        raiz1 = calcular_raiz01(delta, a, b)
        print('a raiz desta equação é', raiz1)
    else:
        raiz1 = calcular_raiz01(delta, a, b)
        raiz2 = calcular_raiz02(delta, a, b)
        if raiz1 < raiz2:
            print('as raízes da equação são', raiz1 ,'e', raiz2 )
        else:
            print('as raízes da equação são', raiz2 ,'e', raiz1 )

