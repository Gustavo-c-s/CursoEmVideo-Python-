from random import randint
escolha = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('[0]Pedra\n[1]Papel\n[2]Tesoura')
play = int(input('Qual você escolhe: '))
print('O computador jogou {} e você jogou {}' .format(escolha[pc],escolha[play]))
if pc == 0:
    if play==0:
     print('Vcs empataram!!')
    elif play == 1:
        print('Você ganhou')
    elif play == 2:
        print('Você Perdeu')
    else :
        print('Jogada invalida')
elif pc == 1:
    if play == 1:
     print('Vcs empataram!!')
    elif play == 2:
        print('Você ganhou')
    elif play == 0:
        print('Você Perdeu')
    else :
        print('Jogada invalida')
elif pc == 2:
        if play == 2 :
            print('Vcs empataram!!')
        elif play == 0 :
            print('Você ganhou')
        elif play == 1 :
            print('Você Perdeu')
        else:
            print('Jogada invalida')
else:
    print('Jogada invalida')
