import datetime
ano = int(input('Qual ano você nasceu? '))
categoria = datetime.date.today().year-ano
print('Voce tem {} anos'.format(categoria))

if categoria < 9:
    print('Você é da categorai mirim.')
elif categoria < 14 and categoria >= 9:
    print('Você é da categoria Infatil.')
elif categoria <= 18 and categoria >= 14:
    print('Você é da categoria Júnior.')
elif categoria >= 19:
    print('Você é da categoria Sênior.')
else:
    print('ERROR!!')
