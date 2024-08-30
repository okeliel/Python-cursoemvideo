'''from random import choice

a1=input('Aluno 1: ')
a2=input('Aluno 2: ')
a3=input('Aluno 3: ')
a4=input('Aluno 4: ')
lista = [a1,a2,a3,a4]
escolhido=choice(lista)
print(f'O escolhido foi: {escolhido}')'''

'''from random import choice
a1=input('Digite: ')
a2=input('digite: ')
lista=[a1,a2]
esc=choice(lista)
print(f'EScolhido: {esc}')'''




from random import choice

a = (input ('Digite o nome:'))
b = (input ('Digite o segundo nome: '))

lista = [a,b]

e = choice(lista)

print (f'\033[1;37m O escolhido foi: {e} \033[m')


