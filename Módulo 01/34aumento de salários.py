'''s = float (input ('Digite o salário: '))
if s > 1250:
    print(f'Com o aumento de 10%, você receberá R${s+(s*10/100):.2f}.') 
if s <= 1250:
    print(f'Com o aumento de 15%, você receberá R${s+(s*15/100):.2f}.')'''


s = int (input ('Digite o seu salário: '))
#a = int (input ('Digite qual porcentagem do aumento: '))
m = s*10
r = m/100
t = s+r

m2 = s*15
r2 = m2/100
t2 = s+r2

if s<=1250:
    print (f'\033[1;36;43m O seu salário será de R${t2 :.2f}\033[m')
    print ('\033[1;36;43m Seu aumento foi de 15%. \033[m')

if s>1250:
    print (f'\033[1;35;42m O seu salário será de R${t:.2f} \033[m')
    print ('\033[1;35;42m O seu aumento foi de 10%. \033[m')