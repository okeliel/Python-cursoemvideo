'''salario=float(input('Digite o salário: R$'))
aumento = salario+(salario*15/100)
print(f'O aumento foi de R${aumento :.2f}')'''


s = float (input ('\033[2;39;46mQual é o seu salário: \033[m'))
a = s + (s*5/100)

print (f'\033[1;39mO salário original é de R${s:.2f}\033[m')
print (f'\033[1;31mCom o aumento de 5%: R${a:.2f}\033[m')