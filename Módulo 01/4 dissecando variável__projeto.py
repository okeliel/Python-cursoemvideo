'''e=input('Digite:')
print(f'Foi digitado: {e}')
print('Tipo:',type(e))
print('É alphanumérico:',e.isalnum())
print('É uma letra maiúscula:',e.isupper())
print('É uma letra:',e.isalpha())
print('É um digito:',e.isdigit())
print('É um decimal:',e.isdecimal())
print('É um indentificador:',e.isidentifier())
print('É uma letra minúscula:',e.islower())
print('É numérico:',e.isnumeric())
print('É imprimível:',e.isprintable())
print('É um espaço:',e.isspace())
print('A primeira letra é maiúscula:',e.istitle())
print('Possui caracteres ASCII:',e.isascii())'''

e = input('Digite: ')
print(f'Foi digitado: {e}')
print(f'É UM NÚMERO: \033[1;33;43m',e.isnumeric()"\033[m")

# Não funcionou