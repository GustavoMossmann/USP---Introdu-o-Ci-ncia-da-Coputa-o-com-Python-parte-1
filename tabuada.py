#repetições encadeadas
linha = 1
while linha <=10:
    print(f'\nTabuada do {linha:2}\n')
    coluna = 1
    while coluna <= 10:
        print(f'{linha:2} X {coluna:2} = {linha*coluna:3}')
        coluna += 1
    linha += 1
    