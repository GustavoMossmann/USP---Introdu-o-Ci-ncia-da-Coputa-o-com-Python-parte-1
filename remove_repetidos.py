def remove_repetidos(lista):
    i = 0
    while i < len(lista):
        pos = 0
        while pos < len(lista):
            if lista[i] == lista[pos] and i != pos:
                del lista[pos]
                continue
            pos += 1

        i += 1

    lista_ord = sorted(lista)
    return lista_ord

lista = [1,2,3,3,3,4]
res = remove_repetidos(lista)
print(res)