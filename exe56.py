somaidade = 0
mediai = 0
maioridade = 0
mulher = 0
for p in range(1, 5):
    print('{}º'.format(p))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    somaidade += i

    if s == 'F' and i <= 20:
        mulher += 1

    if p == 1:
        maioridade = n

    else:
        if p < i and s == 'M':
            maioridade = n

mediai = somaidade/4

print('Temos no grupo uma media de idade de {};\nO mais velho é o {};\nTemos {} mulheres com menos de 20 anos no grupo.'.format(mediai,maioridade,mulher))