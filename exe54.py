from datetime import date
ano = date.today().year
maior = 0
menor = 0
for pess in range(1,8):
    p1 = int(input('Em q ano {}º nasceu? '.format(pess)))
    idade = ano - p1
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Temos {} pessoas maiores de idade e {} menores de idade '.format(maior,menor))