def from10to2():
    y = bin(x)
    print('при переводе из 10-ной системы в 2-ную получится:',y)

def from10to8():
    y = oct(x)
    print('при переводе из 10-ной системы в 8-ную получится:',y)



x = int(input('введите число:'))
sistema = int(input('введите целевую систему счисления:'))
if sistema == 2:
    from10to2()
elif sistema == 8:
    from10to8()




