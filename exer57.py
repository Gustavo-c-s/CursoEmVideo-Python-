sexo = str(input('sexo [M ou F]')).strip().lower()[0]
while sexo not in 'mf':
    sexo= str(input('nao reconhecido, insira novamenro o sexo [M ou f]'))


if sexo == 'f':
    print('Você selecionou Feminino')
if sexo == 'm':
    print('Você selecionou Masculino')