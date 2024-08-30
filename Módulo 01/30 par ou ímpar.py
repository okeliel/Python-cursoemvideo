#Ex: 30

# Pares: 0,2,4,6,8
# ÍMPARES: 1,3,5,7,9

'''n = int (input ('Digite algum número: '))
p = n % 2
if p==0:
    print (f'{n} é PAR!')
else:
    print (f'{n} é ÍMPAR!')'''

# Se o resto da divisão for 0, o número será par, caso contrário será ímpar.


n =int (input('Digite um número: '))

r = n%2

if r==1:
    print (f'\033[3;35;43m{n} é ímpar.\033[m')
if r == 0:
    print (f'\033[3;34;46m{n} é par.\033[m')
