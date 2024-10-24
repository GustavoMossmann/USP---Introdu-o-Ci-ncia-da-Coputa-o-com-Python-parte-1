def maior_elemento(lista):
    maior = lista[0]
    for num in lista:
        for i in range(len(lista)):
            if num > lista[i] and num > maior:
                maior = num

    return maior

lista = [1]

maior = maior_elemento(lista)

print(maior)