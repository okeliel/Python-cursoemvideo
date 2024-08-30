# EX 30



'''km = float (input ("Quantos km's foram percorridos: "))

preco = km * 0.50 if km <=200 else km * 0.45

print (f'O preço da sua passagem é R${preco:.2f}. Boa viagem!')'''

#--------------------------------------------------------------------

# ex 30

#p = float (input ('Preço da passagem: '))
'''print ('-=-' * 20)
v = float ( input ('Quantos km de viagem: '))
print ('-=-' * 20)
conta = v*0.50
conta2 = v*0.45
print (f'Você gastou {v}km de viagem')
print ('-=-' * 20)
if v <= 200:
    print (f'A sua conta final é de R${conta:.2f}. Boa viagem!')
if v > 200:
    print (f'A sua conta final é de R$ {conta2:.2f}. Boa viagem!')
print ('-=-' * 20)'''

#--------------------------------------------------------------

n = float (input ('Quantos km foram percorridos: '))

if n<= 200:
    print (f'\033[3;36;42mA sua viagem custará R${n*0.50 :.2f} sendo considerado R$0,50 por km.\033[m')
if n>200:
    print (f'\033[3;31;49mA sua viagem custará R${n*0.45 :.2f} sendo considerado R$0,45 por km.\033[m') 



















