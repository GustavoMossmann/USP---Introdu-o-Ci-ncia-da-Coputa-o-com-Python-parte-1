n = int(input('Digite um número inteiro: '))
i = 2
primo = False
if n < 2:
    print('não primo')
else:
    if n == 2:
       print('primo')
    else:
        while i < n:
            primo = True
            if n % i == 0:
                print('não primo')
                primo = False
                i = n   
            i +=1
            

if primo:
    print('primo')  




    
