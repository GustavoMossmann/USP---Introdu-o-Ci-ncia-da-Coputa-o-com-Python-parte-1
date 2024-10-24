def maior_primo(num):
    primo = False
    if num == 2:
        return num
    else:
        while not primo:
            i = 2
            while i < num:
                if num % i == 0:
                    primo = False
                    i = num 
                else:
                    i += 1
                    if i == num:
                        return num
            num -= 1
    return num


numero1 = maior_primo(100)      
print(numero1)

numero2 = maior_primo(7)      
print(numero2)
             