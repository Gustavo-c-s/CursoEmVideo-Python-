print('Resultado do aluno!!')
nota1 = float(input('Qual a nota do aluno? '))
nota2 = float(input('Qual a nota do aluno? '))
media = (nota2+nota1)/2
print(media)
if media >= 7 and media <= 10:
    print("O aluno foi aprovado com a media {}".format(media))
elif media <7 and media >= 5:
    print('Aluno em Recuperação com meida {}'.format(media))
elif media < 5 and media == 0:
    print('Aluno reprovado com media {}'.format(media))
else:
    print('Error!!\nTente novamente.')
