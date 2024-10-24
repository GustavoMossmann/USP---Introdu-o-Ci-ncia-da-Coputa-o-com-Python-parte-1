numero = int(input('Digite um número inteiro: '))
verificador = True
while numero != 0:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    if unidade == dezena:
        print('sim')
        numero = 0
        verificador = False
    else:      
        numero = numero // 10
    
if verificador:
    print('não')