def usuario_escolhe_jogada(n, m):
    peca = int(input('\nQuantas peças você vai tirar? '))
    while peca > m or peca < 1 or peca > n or m > n:
        print('\nOops! Jogada inválida! Tente de novo.')
        peca = int(input('\nQuantas peças você vai tirar? '))
    if peca == 1:
        print('Você tirou uma peça.')
    else:
        print('Você tirou', peca ,'peças.')
    return peca

def computador_escolhe_jogada(n , m):
    if m == 1:
        peca = 1
    elif n == m:
        peca = m
    elif n < m:
        peca = n
    elif n > m:
        for i in range(1, m + 1):
            if (n - i) % (m + 1) == 0:
                peca = i
    else:
        peca = m     
    if peca == 1:
        print('\nO computador tirou uma peça.')
    else:
        print('\nO computador tirou', peca ,'peças.')
    return peca

def partida():
    n = int(input('\nQuantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    if n % (m+1) == 0:
        print('\nVocê começa!')
        peca = usuario_escolhe_jogada(n, m)
        n -= peca
        if n == 0:
            print('\nFim do jogo! Você ganhou!\n')
            return -1
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print('Agora restam', n ,'peças no tabuleiro.')
    else:
        print('\nComputador começa!')
    while n !=0:
        peca = computador_escolhe_jogada(n, m)
        n -= peca
        if n == 0:
            print('\nFim do jogo! O computador ganhou!\n')
            return 1
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print('Agora restam', n ,'peças no tabuleiro.')
        peca = usuario_escolhe_jogada(n, m)
        n -= peca
        if n ==0:
            print('\nFim do jogo! Você ganhou!')
            return 0
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            print('Agora restam', n ,'peças no tabuleiro.')

def campeonato():
    count = 1
    computador = 0
    usuario = 0
    while count < 4:
        print('\n*** Rodada ',count ,'***')
        res = partida()
        if res == 1:
            computador += 1
        elif res == 0:
            usuario += 1
        count += 1
    print('\n**** Final do campeonato ****')
    print('\nPlacar: Você', usuario ,'x', computador ,'Computador\n')

def inicio():
    print('\nBem-vindo ao jogo do NIM!')
    print('\nEscolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato')
    escolha = int(input())
    while escolha != 1 and escolha !=2:
        print('\nOops! Escolha inválida! Tente de novo.')
        print('\nEscolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato')
        escolha = int(input())
    if escolha == 1:
        print('\nVocê escolheu uma partida isolada!')
        partida()
    else:
        print('\nVocê escolheu um campeonato!')
        campeonato()
         
inicio()
