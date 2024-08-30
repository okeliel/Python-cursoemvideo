
'''co=float(input('Cateto Oposto: '))
hi=float(input('Hipotenusa: '))
ca=float(input('Cateto Adjacente: '))

seno=co/hi
cosseno= ca/hi
tangente= co/ca

print(f'Valor do Seno: {seno :.2f}')
print(f'Valor do Cosseno: {cosseno :.2f}')
print(f'Valor da Tangente: {tangente :.2f}')'''

'''from math import sin,cos,tan,radians
angulo = float(input('Digite o Ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O Ângulo tem {angulo}°\nO Seno é {seno}\nO Cosseno é {cosseno} e a Tangente é {tangente}')'''

'''import math
ang = float (input('Digite o Ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'Ângulo: {ang :.2f}°')
print(f'Seno: {seno :.2f}')
print(f'Cosseno: {cos:.2f}')
print(f'Tangente: {tan:.2f}')'''




from math import sin,cos,tan,radians

a = float (input ('Digite o valor do Ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print (30*'\033[1;31;m #$#\033[m')
print (f'\033[1;36m O Ângulo é: {a} \033[m')
print (f'\033[1;38m O Seno é: {s} \033[m')
print (f'\033[1;33m O Cosseno é: {c} \033[m')
print (f'\033[1;37m A Tangente é: {t} \033[m')
