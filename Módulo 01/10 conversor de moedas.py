'''real=float(input('digite: R$'))
print(f'Você possui {real}R$.')
r=real/5.16
print('Com R${:.2f}, você poderia comprar {:.2f} dólares.'.format(real,r))'''


real = float (input ('Quantos reais brasileiros você tem: '))

print (f'Você tem: R${real:.2f}')
r = real/5.19

print(f'\033[1;32m Com R${real:.2f} Reais, você pode comprar US${r:.2f} Dólares.\033[m')

