'''n = str (input('Digite uma frase: ')).upper().strip()
#a = n.upper().find('a')
#b = n.upper().count('a')
print('A letra A aparece {} vezes na frase.'.format(n.count('A')))
print('A primeira letra A aparece na posição {}'.format(n.find('A')+1))
print('A última letra A aparece na posição {}'.format(n.rfind('A')))
print('===================================================================')'''

'''n = str (input ('Digite algo: ')).upper().strip()
print('A letra A aparece {} vezes.'.format(n.count('A')))
print('A letra A aparece pela primeira vez no número {}.'.format(n.find('A')+1))
print('A letra A aparece ela última vez no número {}.'.format(n.rfind('A')+1))
print('===================================================================')'''

'''n = str (input ('Digite: ')).upper().strip()
print(f'A letra "A" aparece  {n.count("A,Â")} vezes.')
print(f'A letra "A" aparece pela primeira vez no número {n.find("A")+1}.')
print(f'A letra "A" aparece pela última vez no número {n.rfind("A")+1}.')'''

'''from unidecode import unidecode
n = str (input('Digite: ')).upper().strip()
n1 = unidecode(n)
print (f'A letra "A" aparece {n1.count("A")}')'''

'''Com o unidecode é possível ler letras com acentos como se não tivessem.'''
#-----------------------------------------------------------------------------------

from unidecode import unidecode

p = str (input ('Digite algo: ')).upper().strip()
q = unidecode(p)
print (f'\033[0;33;47mA letra A foi citada {q.count("A")} vezes\033[m.')
