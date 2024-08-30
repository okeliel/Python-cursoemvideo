'''n1 = int (input ('Digite um número: ')) 
n2 = int (input ('Digite o segundo número:  '))
n3 = int (input ('Digite o terceiro número: '))

m = n1 + n2 #> n3
m2 = n1 + n3 #> n2
m3 = n2 + n3 #> n1

if m > n3 and m2 > n2 and m3 > n1:
    print(f'Parabéns! Você conseguiu formar um triângulo com os números {n1}, {n2} e {n3}!')
else:
    print (f'Sinto muito, mas não foi possível formar um triângulo com os números {n1}, {n2} e {n3}.')'''

#---------------------------------------------------------------


n1 = float (input ('Digite o primero número: '))
n2 = float (input ('Digite o segundo número: '))
n3 = float (input ('Digite o terceiro número: '))

m1 = n2 + n3
m2 = n1 + n3
m3 = n1 = n2

if m1>n1 and m2>n2 and m3>n3:
    print (f'\033[1;34;42m Parábens! Você conseguiu formar um triângulo com os números {n1}, {n2} e {n3}.\033[m')
else:
    print (f'\033[1;32;44m Você não conseguiu formar o triângulo com os números {n1}, {n2} e {n3}. Tente novamente! \033[m')

