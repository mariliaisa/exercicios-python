lista_produtos = ('Iphone', 3000, 'Notebook', 4500, 'Mouse', 37.50, 'Alexa', 100, 'Airbuds', 280.96)
print('='* 50)
print('{:*^50}'.format('LISTA DE PRODUTOS'))
print('='* 50)
print('Os ítens da lista são:')
for c in (lista_produtos):
    indice = lista_produtos.index(c)
    if indice % 2 == 0:
        print(f'{c:.<40}R$ {lista_produtos[indice + 1]}')
print(f'*'* 50)      