'''celcius=float(input('Celcius:'))
f=celcius*1.8+32
print(f'Temperatura em Celcius: {celcius}C°\nTemperatua em Fahrenheit: {f}F°')'''


c = float (input ('Digite os celcius: '))

f = c * 1.8 + 32

print (f'\033[1;30;49mTemperatura em Celcius: {c}C°\033[m')
print (f'\033[7;39;40mTemperatura em Fahrenheit: {f}F°\033[m')