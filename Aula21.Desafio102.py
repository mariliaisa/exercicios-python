def fatorial(n=1, show=False):
    """Função que calcula o fatorial de n
    O parâmetro 'show' se for alterado para True, mostra o cálculo"""
    f= 1
    for i in range(n, 0, -1):
        f*= i
        if show == True:
            if i > 1:
                print(f'{i} x', end=' ')
            else:
                print(f'{i} = ', end=' ')    
    return f

#PROGRAMA PRINCIPAL
n = int(input('Digtite um número para saber seu fatorial: '))
print('-'* 20)
print(f'{n}! é {fatorial(n)}')
print('-'* 20)
while True:
    calculo = str(input('Gostaria de ver o cálculo?[S/N] ')).strip().upper()
    if calculo in 'SN':
        break
if calculo == 'S':
    print(fatorial(n, True))
print()
print('FIM!')
#help(fatorial)
