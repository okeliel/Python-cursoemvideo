'''n1 = float (input ('Digite um número: '))
n2 = float (input ('Digite outro número: '))
n3 = float (input ('Digite mais um número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
    
maior = n1 
if n2>n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

print (f'O menor número é {menor}')
print (f'O maior número é {maior}')'''






'''a = int (input ('Digite um número: '))
b = int (input ('Digite outro número: '))
c = int (input ('Digite mais um número: '))

maior = a
if b > a and b > c:
    maior = b

if c > b and c > a:
    maior = c

    menor = a 
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c 
print (f' O maior número é {maior}')
print (f'O menor número é {menor}')'''







a = int  (input ('Digite o primeiro número: '))
b = int  (input ('Digite o segundo número: '))
c = int (input ('Digite o terceiro número: '))

maior = a
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c

menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c    

print (f'O maior é {maior}')
print (f'O menor é {menor}')





































