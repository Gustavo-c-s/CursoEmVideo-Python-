altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
print('{:.2f}'.format(imc))
if 18.5>imc:
    print('Você esta abaixo do peso!')
elif imc > 30:
    print('Voc esta com obesidade!')
else:
    print('Você esta na faixa de peso normal')