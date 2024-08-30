# EX 28

'''from random import randint

n = int (input ('Digite: '))
a = randint(0,5)
if n == a:
    print (f'Parabéns! Você acertou...')
else:
    print(f'Você errou...')    
print (f'O número escolhido foi: {a}')'''



#---------------------------------------------------
'''from random import sample

frase = input('Informe a frase: ')
quantidade = int(input('Informe a quantidade: '))
posições = sample(range(len(frase)), quantidade)

resultado = ''

for posição, letra in enumerate(frase):
  if posição in posições:
    letra = letra.swapcase()
  resultado += letra

print(resultado)'''

# Código estranho que encontrei.

#-------------------------------------------------------
'''from random import randint

from time import sleep

print ('-=-' * 20)
a = int (input ('Digite um número entre 1 e 50: '))
b = randint (0,50)
print ('-=-' * 20)
print ('Processando...')
print ('-=-' * 20)
sleep(4)
if a == b:
  print (f'Você acertou!')
else:
    print (f'Você ERROU!')'''


# O método sleep da biblioteca time permite que você faça o 
# computador aguardar pelos segundos que quiser.

#------------------------------------------------------------

from random import randint
from time import sleep

p = int (input('Digite um número:'))

q = randint(0,50)
sleep(5)
print (f'\033[1;38;43mProcessando...\033[m')
if p == q:
    print (f'\033[1;38;43mVocê acertou!\033[m')
else:
    print (f'\033[1;32;49mVocê errou!\033[m')



































