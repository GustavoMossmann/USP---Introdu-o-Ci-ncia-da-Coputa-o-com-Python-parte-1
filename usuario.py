def usuario_escolhe_jogada(n, m):
    peca = int(input('\nQuantas peças você vai tirar? '))
    while peca > m or peca < 1 or peca > n:
        print('\nOops! Jogada inválida! Tente de novo.')
        peca = int(input('\nQuantas peças você vai tirar? '))
    if peca == 1:
        print('Você tirou uma peça.')
    else:
        print('Você tirou', peca ,'peças.')
   
    return peca
    
usu = usuario_escolhe_jogada(3, 5)
print(usu)