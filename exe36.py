valorcs = float(input('Qual o valor da casa? '))
salario = float(input('Qual é sua renda salarial ? '))
anos = int(input('Em quantas anos predente parcelar? '))
vezescs = anos*12
parcelas = valorcs/vezescs
print('A parcela da casa ficou {:.2f} reais por {:.0f} mes '.format(parcelas,vezescs))
aprovacao = salario * 0.3

if parcelas > aprovacao:
    print('O valor é muito alto para aprovação do emprestimo')

else:
    print('Seu empreestimo foi aprovado!')
