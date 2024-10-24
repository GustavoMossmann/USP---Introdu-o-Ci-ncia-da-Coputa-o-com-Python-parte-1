a = 'banana'
b = 'banana'

#python armazena no mesmo lugar a string banana
print(a is b)

#todo elemento imutável é armazenado no mesmo local

origilist = [45, 76, 34, 55]

newlist = [origilist]*3
print(newlist)

lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]

res = lista1 is lista2
print(res)