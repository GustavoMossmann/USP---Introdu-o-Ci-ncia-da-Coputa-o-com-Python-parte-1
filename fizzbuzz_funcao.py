def fizzbuzz(num):
    if num % 3 == 0 and num % 5 != 0:
        return 'Fizz'
    elif num % 3 != 0 and num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    else:
        return num
    
print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(4))

