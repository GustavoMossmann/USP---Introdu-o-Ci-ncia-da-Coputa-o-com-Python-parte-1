largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
i = 1
while i <= altura:
    x = 1
    if i == 1 or i == altura:
        while x <= largura:
            print('#', end='')
            x += 1
    else:
        while x <= largura:
            if x == 1 or x == largura:
                print('#', end='')
            else:
                print(' ', end='')
            x += 1
            
    print('')
    i += 1
    