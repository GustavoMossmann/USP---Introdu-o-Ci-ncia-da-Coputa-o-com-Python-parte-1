def é_hipotenusa(n):
    i = 1
    while i < n:
        j = 1
        while j < n:
            if n**2 == i**2 + j**2:
                return True
            j += 1
        i += 1

    return False
    
def soma_hipotenusas(n):
    soma = 0
    while n > 0:
        hipo = é_hipotenusa(n)
        if hipo == True:
            soma += n
        n -= 1
    return soma


s = soma_hipotenusas(25)
print(s)