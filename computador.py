def computador_escolhe_jogada(n ,m):
    if m == 1:
        peca = 1
    else:
        if n % m ==0:
            peca = m - 1
        else:
            peca = m
            
    if peca == 1:
        print('O computador tirou uma peça.')
    else:
        print('O computador tirou', peca ,'peças.')
    if n - peca <= 0:
        return -2
    else:
        return peca