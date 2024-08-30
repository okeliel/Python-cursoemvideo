# Exercício 16

'''from math import trunc
numreal=float(input('Digite: '))
numint=trunc(numreal)
print(f'O número real é {numreal} e o seu inteiro é {numint}')'''


n = float (input('Digite um número: '))
r = n//1
print (f' \033[1;36m Você digitou {n} \033[m')
print (f' \033[1;34m A porção inteira de {n:.2f} é: {r:.0f} \033[m')