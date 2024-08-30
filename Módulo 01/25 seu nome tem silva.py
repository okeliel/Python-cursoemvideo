'''nome = str (input('Nome completo: '))

n = 'silva' in nome

print(f'Seu nome tem "Silva": {n}')'''

# ---------------------------------------------------

'''nome = str (input('Nome completo: ')).strip()

p = 'silva' in nome.lower().split()
print(f'{p}')'''


#--------------------------------------------------
n = str (input ('Seu nome: ')).strip()
p = 'silva' in n.lower().split()

print (f'\033[0;30;44mSeu nome tem Silva: {p}\033[m')