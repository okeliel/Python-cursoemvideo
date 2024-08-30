# print ('\033[1;33;43mOlá, mundo.\033[m')


'''a = 2
b = 4
print (f'OS valores de A é \033[1;33;42m{a}\033[m e B é \033[1;35;46m{b}!')'''

'''nome = 'Marques'
print(f'O seu nome é \033[1;31m{nome}\033[m!')'''

'''nome = 'Marques'
print (f'O seu nome é {"\033[32m"} {nome} {"\o33[m"}')''' # não funciona

nome = 'Marques'
print ('O seu nome é {}{}.{}'.format('\033[1;31m',nome,'\033[m'))

