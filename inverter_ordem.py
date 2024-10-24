def inverte_ordem(lista):
    i = -1
    cont = 0
    while cont < len(lista):
        print(f'{lista[i]}', end=', ')
        i -= 1
        cont += 1


print('Início do Programa - 0 para sair\n')
n = int(input('Digite um número inteiro positivo: '))
lista = []
while n != 0:
    if n not in lista:
        lista.append(n)
    n = int(input('Digite um número inteiro positivo: '))

print('Números digitados na ordem inversa:')
inverte_ordem(lista)

print('\nFim do Programa\n')