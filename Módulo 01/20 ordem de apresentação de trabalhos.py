#'//Como mostrar a ordem sorteada em Python?'

'''from random import shuffle

a1=input('Aluno 1: ')
a2=input('aluno 2: ')
a3=input('Aluno 3: ')
lista= [a1,a2,a3]
shuffle(lista)
print ('A ordem será: ')
print(lista)'''

'''from random import shuffle
a1=input('digite:')
a2=input('Digite:')
a3=input('Digite:')
lista=[a1,a2,a3]
shuffle(lista)
print('A ordem é:  ')
print(lista)'''

'''from random import shuffle

a1=str(input('digite: '))
a2=str(input('Digite: '))
a3=str(input('Digite:' ))
lista=[a1,a2,a3]
shuffle(lista)
print('Ordem: ')
print(lista)'''



from random import shuffle

a = (input ('Digite o 1° nome: '))
b = (input ('Digite o 2° nome: '))
lista = [a,b]
r = shuffle(lista)
print (f'\033[1;37m A ordem de apresentação será a seguinte: {lista} \033[m')