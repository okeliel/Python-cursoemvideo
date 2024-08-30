'''n1=float(input('Nota 1:'))
n2=float(input('Nota 2:'))
s= (n1+n2)/2
#print('A nota 1 é {:.1f}; a nota 2 é {:.1f}; e a soma é {:.1f}'.format(n1,n2,s))
print(f'A nota 1 é {n1:.1f}; a nota 2 é {n2:.1f}; e o resultado é {s:.1f}')'''

#--------------------------------------------------------------------------------
'''nome = str (input ('Qual é seu nome? '))
if nome == 'Gustavo':
    print (f'Você acertou!')
else:
    print ('Você ERROU!')'''

'''n1 = float (input ('Digite uma nota: ')) 
n2 = float (input ('Digite outra nota: '))

n3 = (n1+n2)/2

if n3>= 5.0:
    print ('Parabéns, você passou!')
else:
    print ('Sinto muito, mas você não foi aprovadp.')'''


'''n1 = float (input ('Digite uma nota: '))
n2 = float (input ('Digite outra nota: '))
n3 = (n1+n2)/2
print (f'PARABÉNS' if n3 >= 6.0 else 'Estude mais!')'''
#-----------------------------------------------------------

n1 = float (input ('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota:' ))
n3 = float (input ('Digite a terceira nota: '))
n4 = float (input ('Digite a quarta nota: '))
t = (n1+n2+n3+n4)/4
print (f'Nota do 1° Bimestre: \033[1;31m{n1:.2f}\033[m')
print (f'Nota do 2° Bimestre: \033[1;32m{n2:.2f}\033[m')
print (f'Nota do 3° Bimestre: \033[1;34m{n3:.2f}\033[m')
print (f'Nota do 4° Bimestre: \033[1;35m{n4:.2f}\033[m')
print (f'Nota final: \033[1;36m{t:.2f}\033[m')























