n1 = int(input('insira um numero '))
n2 = int(input('insira outro numero '))
op = 0
while op !=5:
    print('''
    [1] somar
    [2] multiplicar
    [3] dividir
    [4] novos numeros 
    [5] sair''')
    op = int(input('Selecione a opção!'))
    if op == 1:
        soma = n1+n2
        print(f'{n1}+{n2}={soma}')
    elif op ==2:
        mul = n1 * n2
        print(f'{n1}x{n2}={mul}')
    elif op== 3:
        div = n1 / n2
        print(f'{n1}/{n2}={div}')
    elif op == 4:
        n1 = int(input('insira um numero '))
        n2 = int(input('insira um numero '))
    elif op ==5 :
        break
    else:
        print('opção invalida!!\nEscolha novamente')
