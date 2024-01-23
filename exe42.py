r1 = float(input('um lado '))
r2 = float(input('outro lado '))
r3 = float(input('ultimo lado '))
if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('Seguimentos forma um trinagulo! ')
    if r1 == r2 == r3:
        print('um Equilatero')
    elif r1 != r2 != r3 != r1:
        print('um Escaleno ')
    else:
        print('Isólsceles')
else:
    print('Nao forma um triangulo!')