num = int(input('numero: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[35m', end='')
    print('{}'.format(c))