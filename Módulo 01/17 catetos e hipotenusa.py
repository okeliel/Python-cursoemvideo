'''from math import sqrt
cateto1=float(input('Cateto A: '))
cateto2=float(input('Cateto B: '))
hipotenusa = (cateto1 * cateto1) + (cateto2 * cateto2)
print(f'O Cateto A: {cateto1}\nO Cateto B: {cateto2}\nHipotenusa: {sqrt(hipotenusa)}')'''

'''from math import ceil, floor
cateto1 = float (input ('Cateto A: '))
cateto2 = float (input ('Cateto B: '))
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
print (f'Cateto A: {cateto1}\nCateto B: {cateto2}\nHipotenusa: {floor(hipotenusa)}')'''

'''from math import hypot
cateto1 = float (input ('Cateto A: '))
cateto2 = float (input ('Cateto B: ') )
hipotenusa = hypot(cateto1, cateto2)
print (f'Cateto A: {cateto1}\nCateto B: {cateto2}\nHipotenusa: {hipotenusa}')'''

#------------------------------------------------------------------------------------

# H² = Co² + Ca²

'''co = float (input ('Cateto Oposto: '))
ca = float (input ('Cateto Adjacente: '))
p = (co**2)+(ca**2)
rq = p**(1/2)
print (f'A hipotenusa entre Cateto Oposto {co} e do Cateto Adjacente {ca} é {rq:.2f}')'''

'''import math
co = float (input('Cateto Oposto: '))
ca = float (input('Cateto Adjacente: '))
h = math.hypot(co,ca)
print (f'A Hipotenusa entre o Cateto Oposto {co} e o Cateto Adjacente {ca} é: {h:.2f}')'''

'''from math import hypot

co = float (input('Cateto Oposto: '))
ca = float (input ('Cateto Adjacente: '))
h = hypot(co,ca)
print (f'O Cateto Oposto é: {co}')
print (f'O Cateto Adjacente é: {ca}')
print (f'A Hipotenusa é: {h:.2f}')'''

from math import hypot
co = float (input ('Digite o Cateto Oposto: '))
ca = float (input ('Digite o Cateto Adjacente: '))
h = hypot(co,ca)
print (30 * '\033[1;36m #')
print (f' \033[1;34m O Cateto Oposto é: {co:.2f} \033[m')
print (f' \033[1;39m O Cateto Adjacente é: {ca:.2f} \033[m')
print (f' \033[1;32m A Hipotenusa é: {h:.2f} \033[m')







