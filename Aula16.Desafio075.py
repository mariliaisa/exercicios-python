par = virgula = 0
tupla = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))
print('*-' * 20)
print(f'Você digitou os valores: {tupla}')
if 9 in tupla:
    print(f'\nQuantas vezes apareceu o número 9? {(tupla.count(9))}')
else:
    print('O número 9 não aparece na lista.')
if 3 in tupla:
    print(f'Em que posição foi digitado o número 3? {tupla.index(3) + 1}ª posição')
else:
    print('O número 3 não aparece na lista.')
print(f'Quais foram os números pares?')
for n in (tupla):
    if n % 2 == 0:
        if virgula == 1: 
            print(',', end= ' ')
        print(n, end='')
        par += 1
        virgula = 1
if par == 0 :
    print('Não há números pares na lista.')
