lista = []
for i in range (0,5):
    lista.append(int(input(f'Digite o valor da posição {i+1}: ')))
maior = max(lista)
menor = min(lista)
print(f'A lista formada pelos valores digitados foi: {lista}')
print(f'\nO maior valor foi: {maior}, na(s) posição(s): ', end=' ')
for c, itens in enumerate(lista):
    if itens == maior:
        print(c + 1, end=' ')
print(f'\nO menor valor foi: {menor} na(s) posição(s): ', end=' ')
for c, itens in enumerate(lista):
    if itens == menor:
        print(c + 1, end=' ')