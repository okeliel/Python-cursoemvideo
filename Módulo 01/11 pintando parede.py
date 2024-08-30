#faça um programa que leia a largura e altura de parede em metros, 
#calcule a sua area e a quantidade de tinta necessaria para pintá-la, 
#sabendo que cada litro de tinta pinta uma area de 2m

'''largura=float(input('Largura:'))
altura=float(input('Altura:'))
area=largura*altura
tinta_gasta=area/2

print(f'Se a largura é {largura}, a altura é {altura}\ne sabendo que cada litro de tinta pinta 2 metros, a área pintada será de {area}m².')
print(f'Para pintar a parede será utilizado {tinta_gasta}l de tinta.')'''


a = float (input ('Altura: '))
l = float (input ('Largura: '))

area = a*l
t = area/2
print(30*'#')
print (f'\033[1;31mA altura é {a:.2f}\033[m')
print (f'\033[1;32mA largura é {l:.2f}\033[m')
print (f'\033[1;33mA Área é {area:.2f}\033[m')
print (f'\033[1;34mA tinta gasta sera de {t:.2f} litros\033[m')




