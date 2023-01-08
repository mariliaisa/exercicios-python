from random import randint
tupla = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(f'\nOs números sorteados são: {tupla}')
print(f'O menor valor é: {sorted(tupla)[0]}')
print(f'O maior valor é: {max(tupla)}')

