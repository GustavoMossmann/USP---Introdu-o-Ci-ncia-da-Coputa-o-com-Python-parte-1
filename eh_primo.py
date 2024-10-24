def eh_primo(n):
    i = 2
    if n == 2:
        return True
    while i < n:
        if n % i == 0:
            return False
        i += 1
        if i == n:
            return True

n = 1
print('Início do programa\n')
n = int(input('Digite um número inteiro: '))
while n > 0:
    if n == 0:
        break
    primo = eh_primo(n)
    if primo:
        print(f'{n} é primo!')
    else:
        print(f'{n} não é primo!')
    n = int(input('Digite um número inteiro: '))

print('\nFim do programa\n')