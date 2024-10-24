def calcula_wal(lista_palavras):
    '''Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.'''
    tamanhos_palavras = 0
    for palavras in lista_palavras:
        tamanhos_palavras += len(palavras)
    wal = tamanhos_palavras / len(lista_palavras)
    return wal

lista = ['abacaxi', 'coco', 'maça', 'papaia']
wal = calcula_wal(lista)
print(wal)