def converte_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = ((segundos % 3600) % 60 )
    print(f'{horas}h {minutos}m {segundos_restantes}s')


#converte_segundos(7895)

a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
aux = a
a = b
b = aux
print(a)
print(b)