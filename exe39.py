import datetime
print('Alistamento Militar!!')
ano = int(input('Qual ano você nasceu ?'))
servi = datetime.date.today().year - ano
if servi==18:
    print('Você tem {} anos ja esta na hora de servi ao seu pais! '.format(servi))
elif servi>18:
    print('Você tem {} anos se você ainda nao se alistou, saiba que ja passou do tempo de se alistar'.format(servi))
elif servi<18:
    print('Você yte {} ainda talta {} anos para servi.'.format(servi,(18-servi)))
else:
    print('Erro!!\nTente novamente')