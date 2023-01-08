print('\n{:*^50}'.format('TABUADA'))
while True:
    n = int(input('Digite um número para saber sua tabuada: '))
    if n < 0:
        print('\nOPERAÇÃO ENCERRADA.')
        break    
    for contador in range(1, 11):
        resultado = n * contador
        print(f'{n} x {contador:2} = {resultado}')
        contador += 1
    print('*' * 50)