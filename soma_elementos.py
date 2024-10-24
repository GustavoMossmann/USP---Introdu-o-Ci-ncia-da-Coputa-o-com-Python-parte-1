def soma_elementos(lista):
    soma = 0 
    for num in lista:
        soma += num

    return soma

lista = [1,7,3,8,1,32]

soma = soma_elementos(lista)

print(soma)