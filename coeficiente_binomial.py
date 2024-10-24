
def fatorial(num):
    fat = 1
    if num == 0:
        return fat
    else:
        while num > 0:
            fat *= num
            num -= 1
        return fat
    
def numero_binomial(n, k):
    num_binomial = fatorial(n)/(fatorial(k)*fatorial(n - k))
    return num_binomial



n = int(input('Digite o valor de n: '))
k = int(input('Digite o valor de k: '))

num_binomial = numero_binomial(n, k)

print(num_binomial)