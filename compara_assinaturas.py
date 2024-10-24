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

ass1 = [4.34, 0.05, 0.02, 12.81, 2.16, 0.0]
ass2 = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]
res = compara_assinatura(ass1, ass2)

print(res)