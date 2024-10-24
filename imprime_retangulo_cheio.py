largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
i = 1
while i <= altura:
    x = 1
    while x <= largura:
        print('#', end='')
        x += 1
    print('')
    altura -= 1
