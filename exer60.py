from math import factorial
n = int(input('digiti um numero para o seu Fatorial: '))
f = factorial(n)
c=n
print(f'o fatorial de {n}! é')
while c>0:

    print(f'{c}', end='' 'x' if c>1 else '='f'{f}')
    c-=1
