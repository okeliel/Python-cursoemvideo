'''preço=float(input('Digite:'))
#pd=preço-(preço*5/100) # Preço com desconto
d=preço-(preço*5/100)
print(f'Preço Original: R${preço :.2f}\nPreço com Desconto: R${d}\nDesconto: {d :.2f}.')'''

p = float (input ('Digite um valor em R$: '))

pd = p - (p*5/100)

print (30*"#")
print (f'\033[1;36mO valor original é: R${p:.2f}\033[m')
print (f'\033[1;38mO valor com 5% de desconto é: {pd:.2f}\033[m')