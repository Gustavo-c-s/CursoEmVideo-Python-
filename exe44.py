produto= float(input('Digite o Valor do produto: '))
print('Qual a forma de pagamento\n[1]Dineheiro ou cheque,\n[2]Cartao de Debito,\n[3]Cartao de Credito.')
escolha = int(input('Foma de pagamento: '))
if escolha == 1:
    print('Você ganhou 10% de desconto no produto de R${:.2f} q saia a R${:.2f} com desconto! '.format(produto,produto-(produto*0.1)))
elif escolha == 2:
    print('No debito tem 5% de desconto no produto de R${:.2f} q saia a R${:.2f} com desconto! '.format(produto,produto-(produto*.05)))
elif escolha ==3:
    vez = int(input('Em quantas vezes deseja fazer ? '))
    if vez == 2:
        print('O produtode R${:.2f} em 2 vez fica em R${:.2f}'.format(produto,produto/2))
    elif vez >= 3:
        print('Produto acima de 3 vezes tem um juros de 20% saindo a R${:.2f} voce pagara {:.0f} párcelas de R${:.2f}'.format(produto+(produto*.2),vez,(produto+(produto*.2))/vez))
else:
    print('Nao aceitamos essa forma de pagamento!')