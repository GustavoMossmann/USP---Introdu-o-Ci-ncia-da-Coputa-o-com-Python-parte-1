def tempF(celsius):
    fahre = celsius * 9/5 + 32
    return fahre

def tempCel(fah):
    cel = (fah - 32)* 5/9
    return cel

celsius = tempCel(120)
print(celsius)

fahre = tempF(38)
print(fahre)


