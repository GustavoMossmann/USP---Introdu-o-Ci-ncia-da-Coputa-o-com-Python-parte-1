#função para verificar qtd de digitos digitados
def verificar_qtd_digitos(numeroTxt):
    while len(numeroTxt) < 8:
        numeroTxt = input('Verifique o número e digite novamente: ')
        if len(numeroTxt) >= 8:
            break
    numero = int(numeroTxt)
    return numero

#função para verificar presença de numeros adjacentes semalhantes
def verificar_num_semelhantes(numero):
    numero02 = numero
    while numero02 != 0:
        #print(numero)
        unidade = numero02 % 10
        dezena = (numero02 // 10) % 10
        if unidade == dezena:
            print('Esse número possui números adjacentes semelhantes.')
            return verificar_qtd_digitos('1234')
            
        numero02 = numero02 // 10
        if numero02 == 0:
            print('Numero OK')
            return numero


numero_digitado = input('Digite um numero com 8 digitos: ')
numero_verificado = verificar_qtd_digitos(numero_digitado)

numero_verificado2 = verificar_num_semelhantes(numero_verificado)
#print(numero_verificado2)