frase = str(input('Digite: ')).strip().upper()
palavra = frase.split()
junta = ''.join(palavra)
inverso = junta[::-1]; '''Modo fatiado'''
'''for l in range(len(junta)-1,-1,-1):
    inverso += junta[l]'''
print('Voce escreveu {}, ela inversa é {} '.format(frase,inverso))
if inverso == junta:
    print('Voce escreveu uma palindromo!!')
else:
    print('Nao é um palindromo ')

