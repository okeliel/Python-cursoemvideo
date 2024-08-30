'''n = str (input('Digite: ')).upper().strip()
n1 = n.split()
print (f'O seu primeiro nome é {n1[0]}')
print (f'O seu último nome é {n1[len(n1)-1]}')'''


'''n = str (input ('Digite: '))
n1 = n.split()
print (f'O seu primeiro nome é {n1[0]}')
print (f'O seu último nome é {n1[-1]}')'''

#----------------------------------------------

p = str (input ('digite: '))

q = p.split()

print (f'\033[1;32;45mO primeiro nome é {q[0]}\033[m')
print (f'\033[1;36;42mO último nome é {q[-1]}\033[m')
