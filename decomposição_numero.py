n = int(input('Digite um numero inteiro maior que 1: '))
fator = 2
while n > 1:
    multiplicidade = 0
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0:
        print(f'Fator {fator} Multiplicidade {multiplicidade}')
    fator += 1
