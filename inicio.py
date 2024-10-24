def inicio():
    print('Bem-vindo ao jogo do NIM!')
    print('Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato')
    escolha = int(input())
    while escolha != 1 and escolha !=2:
        print('Oops! Escolha inválida! Tente de novo.')
        print('Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato')
        escolha = int(input())
    if escolha == 1:
        print('Você escolheu uma partida isolada!')
        #partida()
    else:
        print('Você escolheu um campeonato!')
        #campeonato()


inicio()