numero1 = int(input('Digite o primeiro inteiro: '))
numero2 = int(input('Digite o segundo inteiro: '))
numero3 = int(input('Digite o terceiro inteiro: '))

if numero1 < numero2 and numero2 < numero3:
    print('crescente')
else:
    print('não está em ordem crescente')