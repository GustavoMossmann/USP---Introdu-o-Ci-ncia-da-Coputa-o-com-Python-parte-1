import re
def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

texto = 'Em pleno século XXI é salutar refletir sobre a importância de preservação do meio ambiente, bem como atuar em prol de uma sociedade mais consciente e limpa. Já ficou mais que claro que a maioria dos problemas os quais enfrentamos atualmente nas grandes cidades, foram gerados pela ação humana. De tal modo, podemos pensar nas grandes construções, alicerçadas na urbanização desenfreada, ou no simples ato de jogar lixo nas ruas. A poluição gerada e impregnada nas grandes cidades foi, em grande parte, fruto da urbanização desenfreada ou da atuação de indústrias; porém, deveres não cumpridos pelos homens também proporcionaram toda essa "sujidade". Nesse sentido, vale lembrar que pequenos atos podem produzir grandes mudanças se realizados por todos os cidadãos.'
sent = separa_sentencas(texto)

print(sent)