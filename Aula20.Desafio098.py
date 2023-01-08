#FUNÇÃO PARA CRIAR UMA SEQUÊNCIA (PA)
from time import sleep
#CRIAÇÃO DA FUNÇÃO
def contador(inicio, fim, passo):
    if passo < 0:
        intervalo = passo
        partida = max(inicio, fim)
        final = min(inicio, fim) - 1     
    else:   
        if passo == 0:
            intervalo = 1
            passo = 1
        if inicio < fim:
            intervalo = passo
            partida = inicio
            final = fim + 1
        else:
            intervalo = passo * -1
            partida = inicio
            final = fim - 1
    print('-'* 40)
    print(f'Contagem de {inicio} a {fim}, de {passo} em {passo}: ')
    for i in range(partida, final, intervalo):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print()
    print('-'*40)
    sleep(0.4)

#PROGRAMA    
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez! Defina os parâmetros: ')
inicio = int(input('Início da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo da contagem: '))
contador(inicio, fim, passo)