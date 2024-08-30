# EX 29


'''80 km é o limite.
A multa é R$7,00 por km acima do limite.'''

'''a = float (input ('Velocidade percorrida: '))
limite = float (input ('Limite de velocidade: '))
m = float (input ('Valor da multa: '))
ultrapassada = a-limite
multa = ultrapassada*m
if a == limite:
    print (f'Você não efetuou nenhuma ultrapassagem irregular.')
else:
    print (f'Você foi multado no valor de  R${multa:.2f}.')'''


n = float (input ('Quilometros percorridos: '))
h = float (input ('Qual é o limite: '))
limite = n-h
multa = limite*7

if n<h:
    print ('\033[3;35;47mParabéns, dirija com cuidado!\033[m')
if n>h:
    print (f'\033[3;32;45mVocê foi MULTADO no valor de R${multa:.2f}\033[m')
