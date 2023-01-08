#FUNÇÃO PARA SORTEAR NÚMEROS, COLOCAR EM UMA LISTA E SOMAR OS PARES
from random import randint
from time import sleep
def sorteio():
    lista = []
    print('-='*20)
    print('Os números sorteados foram: ')
    for i in range(0,5):
        lista.append(randint(1,10))
        print(lista[i], end=' ', flush=True)
        sleep(0.5)
    print()
    print('-='*20)
    return lista

def somapar(arg):
    soma= 0
    for e in arg:
        if e % 2 == 0:
            soma += e
    print(soma)

#PROGRAMA PRINCIPAL
sorteado = sorteio()
print(f'Analisando os dados...')
sleep(0.6)
print(f'A soma dos números pares da lista {sorteado} é: ', end=' ')
somapar(sorteado)

