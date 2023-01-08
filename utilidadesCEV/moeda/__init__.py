def escreva(texto):
    print('=' * (len(texto) + 2))
    print('{:^10}'.format(texto ))
    print('=' * (len(texto) + 2))


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def dobro(x, mostrar = False):
    dobrado = 2 * x
    if mostrar == False:
        return dobrado
    else:
        return moeda(dobrado)


def metade(x, mostrar = False):
    meio = x/2
    if mostrar == False:
        return meio
    else:
        return moeda(meio)


def aumenta(a=0, b=0, mostrar = False):
    juros = (1 + b/100) * a
    if mostrar == False:
        return juros
    else:
        return moeda(juros)


def diminui(a=0, b=0, mostrar = False):
    desconto = (1 - b/100) * a
    if mostrar == False:
        return desconto
    else:
        return moeda(desconto)


def resumo(preco=0, aumento=0, reducao=0):
    print('='* 40)
    print(f'Análise do valor'.center(30))
    print('='* 40)
    print(f'Preço analisado: \t{(moeda(preco))}')
    print(f'O dobro do preço: \t{dobro(preco, mostrar = True)}')
    print(f'A metade do preço: \t{metade(preco, mostrar =True)}')
    print(f'{aumento}% do preço: \t\t{aumenta(preco, aumento, mostrar = True)}')
    print(f'{reducao}% do preço: \t\t{diminui(preco, reducao, mostrar=True)}')
    print('='* 40)
    print()
   