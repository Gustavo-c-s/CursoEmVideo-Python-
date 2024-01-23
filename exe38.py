print('Qual sera o numero sera o maior? ')
nun1 = float(input('Digite um numero: '))
nun2 = float(input('Digite outro numero: '))
maior = nun1
if nun1>nun2:
    maior=nun1
    print('{} é o numero maior!!'.format(maior))
elif nun2>nun1:
    maior=nun2
    print('{} é o numero maior!!'.format(maior))
elif nun2==nun1:
    print('Numeros iguais não tem maior')
else:
    print('Error! nao sei oq é ')