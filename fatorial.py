n = int(input('Digite o valor de n: '))
fat = 1
if n == 0:
    print(fat)
else:
    while n > 0:
        fat *= n
        n -= 1
    print(fat)

    
