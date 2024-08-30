real = float(input('Digite o valor: R$'))
dolar = real/5.29
bolivar = real/0.63
libra = real/6.15
euro = real/5.27
rublo = real/0.083
iene = real/0.035
guarani = real/0.00071
franco = real/5.13
coroa = real/0.035
lira = real/0.28
print(f'Com {real} reais é possível comprar: ')
print('----------------------------')
print(f'{dolar :.2f} dólar(es) Americanos\n{bolivar :.2f} Bolívar(es) Venezuelano(s)')
print(f'{libra :.2f} libra(s) Inglesas\n{euro :.2f} Euro(s)\n{rublo :.2f} Rublo(s) Russo(s).')
print(f'{iene :.2f} Iene(s)\n{guarani :.2f} Guarani(s) Paraguaio(s)\n{franco :.2f} Franco(s) Suiço(s)\n{coroa :.2f} Coroa(s) Islândesa(s)')
print(f'{lira :.2f} Lira(s) Turca(s)')