'''m=float(input('Digite:'))
print(f'Você digitou: {m}')
cm=m*10*10
mm=m*10*10*10
print(f'Os centímetros de {m} metros é {cm} cm;')
print(f'os milímetros de {m} metros é {mm} mm.')'''

m = float (input ('Digite os metros quadrados: '))

cm = m*200
km = m/300

print (f'\033[1;33m Os m² são: {m:.2f} \033[m')
print (f'\033[1;34m Os cm² são: {cm:.2f} \033[m')
print (f'\033[1;35m Os km² são: {km:.2f} \033[m')
