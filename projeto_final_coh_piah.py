import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("\nBem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

#-----------------------------------------------------
#calculo do tamanho médio das palavras
def calcula_wal(lista_palavras):
    '''Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras'''
    tamanhos_palavras = 0
    for palavras in lista_palavras:
        tamanhos_palavras += len(palavras)
    wal = tamanhos_palavras / len(lista_palavras)
    return wal

#-----------------------------------------------------
#calculo Relação Type-Token
def calcula_ttr(lista_palavras):
    '''Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras'''
    num_palavras_diferentes = n_palavras_diferentes(lista_palavras)
    ttr = num_palavras_diferentes / len(lista_palavras)
    return ttr

#-----------------------------------------------------
#calculo Razão Hapax Legomana
def calcula_hlr(lista_palavras):
    '''Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. '''
    num_palavras_unicas = n_palavras_unicas(lista_palavras)
    hlr = num_palavras_unicas / len(lista_palavras)
    return hlr

#-----------------------------------------------------
#calculo tamanho medio da sentença
def calcula_sal(lista_sentenças):
    '''Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças '''
    total_caracteres = 0
    for sentencas in lista_sentenças:
        total_caracteres += len(sentencas)
    sal = total_caracteres / len(lista_sentenças)
    return sal

#-----------------------------------------------------
#calculo Complexidade de sentença
def calcula_sac(lista_frases, lista_sentencas):
    '''Complexidade de sentença é o número total de frases divido pelo número de sentenças.'''
    sac = len(lista_frases) / len(lista_sentencas)
    return sac


#-----------------------------------------------------
#calculo tamanho médio da frase
def calculo_pal(lista_frases):
    '''Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto'''
    total_caracteres = 0
    for frases in lista_frases:
        total_caracteres += len(frases)
    sal = total_caracteres / len(lista_frases)
    return sal


#-------------------------------------------------- 
#compara as assinaturas
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    total = 0
    i = 0
    while i < len(as_a):
        sim = abs(as_a[i] - as_b[i])
        total += sim 
        i +=1
    res_similaridade = total/6
    return res_similaridade



def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #01---texto entrou na função
    #02---tratamento do texto
    #separar sentença
    lista_sentencas = separa_sentencas(texto)
    
    #separar frase
    lista_frases = []
    for frases in lista_sentencas:
        frase = separa_frases(frases)
        lista_frases += frase
        
    #separar palavras
    lista_palavras = []
    for palavras in lista_frases:
        palavra = separa_palavras(palavras)
        lista_palavras += palavra

    #03 calculos para assinatura
    #---- wal - Tamanho médio de palavra
    wal = calcula_wal(lista_palavras)

    #---- ttr - Relação Type-Token
    ttr = calcula_ttr(lista_palavras)

    #---- hlr - Razão Hapax Legomana
    hlr = calcula_hlr(lista_palavras)

    #---- sal - Tamanho médio da sentança
    sal = calcula_sal(lista_sentencas)

    #---- sac - complexidade média da sentença
    sac = calcula_sac(lista_frases, lista_sentencas)

    #---- pal - tamanho medio de frase
    pal = calculo_pal(lista_frases)

    return [wal, ttr, hlr, sal, sac, pal]
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    lista_assinaturas = []
    for texto in textos:
        ass = calcula_assinatura(texto)
        lista_assinaturas.append(ass)

    grau_similaridade = []
    for assinaturas in lista_assinaturas:
        similaridade = compara_assinatura(assinaturas, ass_cp)
        grau_similaridade.append(similaridade)


    menor = min(grau_similaridade)
    posicao = grau_similaridade.index(menor) + 1
    return posicao
    

#---- Inicio do Programa ------
#01 --- ler a assinatura
assinatura_padrao = le_assinatura()

#02 --- ler os textos
lista_textos = le_textos()

#03 --- armazena calculo de assinatura de textos
#04 --- grau de similaridade
#05 --- saida do resultado
res = avalia_textos(lista_textos, assinatura_padrao)
print('\nO autor do texto', res ,'está infectado com COH-PIAH')

