def minimo(lista):
    min = lista[0]
    i = 0
    while i < len(lista):
        if lista[i] < min:
            min = lista[i]
        i += 1
    return min

mini = minimo([1, 3, 4, 5, 1, 8, 4, 2, 0, 3, -1, 5, 3])
print(mini)

