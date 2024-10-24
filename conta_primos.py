def n_primos(n):
    qtd_primos = 1
    while n > 2:
        i = 2
        while i < n:
            if n % i == 0:
                break
            i += 1
            if i == n:
                qtd_primos += 1
        n -= 1
    return qtd_primos

primos = n_primos(121)

print(primos)