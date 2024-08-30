nome = str(input ('Digite o seu nome: '))
conta = nome.split()
print ('Analisando o texto...')

print (f'Seu nome em letras maiúsculas:  {nome.upper()}')
print (f'Seu nome em letras minúsculas: {nome.lower()}')
print (f'O seu nome tem {len(nome.replace("  " , " "))} letras.')
print (f'O seu primeiro nome é {(conta[0])} e ele tem {len(conta[0])} letras.')


nome = str(input ('Escreva o nome: '))
contagem = nome.split()
print('Analizando o nome..')

print(f'O nome em letras minusculas: {(nome.lower())}')
print(f'O nome em letras maiúsculas: {(nome.upper())}')
print(f'Quantas letras o nome completo possui: {len(nome.replace(" " , " "))} letras')
print(f'O primeiro nome é {contagem[0]} e ele Possui {len(contagem[0])} letras.')

print('-'*30)

print(f'O segundo nome é {contagem[1]} e ele possui {len(contagem[1])} letras.')
print(f'Os terceiro nome é {contagem[2]} e ele possui {len(contagem[2])} letras.')
print(f'O terceiro nome é {contagem[3]} e ele possui {len(contagem[3])} letras.')


