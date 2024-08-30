'''km=float(input('Quilometros rodados:'))
dia=int(input('Dias alugado:'))
resultado=(dia*60)+(km*0.15)

print(f'O quilometro rodado foi {km}\nFoi alugado por {dia} dias.')
print(f'O carro custa R$60,00 por dia e R$0,15 por quilometro rodado.')
print(f'O valor total a pagar é de R${resultado :.2f}')'''

km = float (input (f'\033[1;39mDigite os quilometros percorridos:\033[m '))
d = float (input ('\033[1;36mQuantos dias alugado:\033[m '))
va = float (input ('\033[1;34mQuanto custa o aluguel por dia:\033[m '))
vq = float (input ('\033[1;31mQual é o valor por quilometro percorrido:\033[m '))
r = (d*va) + (km*vq)

print (f'\033[1;30mO valor do aluguel do carro será de R${r:.2f}\033[m')
