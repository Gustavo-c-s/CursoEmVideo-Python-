numero = int(input('Digite um numero: '))
print('Qual a forma voce deseja: \n[1]Binario\n[2]Octal\n[3]Hexadecimal')
escolha = int(input('Qual alternativa? '))
if escolha==1:
    print('{} convertido para Binario é {}'.format(numero,bin(numero)))
if escolha==2:
    print('{} convertido para Octal é {}',format(numero,oct(numero)))
if escolha==3:
    print('{} convertido para Hexadecimal é {}'.format(numero,hex(numero)))
else:
    print('Error!!\nescolha entre 1,2 e 3 por favor')
