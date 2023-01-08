from random import randint
import Dicionários as d
from time import sleep
d.cabecalho('JOGOS MEGA SENA')
#escolhendo a quantidade de vetores dentro da lista jogos
quantidade = int(input('Quantos jogos serão feitos? '))
jogos = []
numeros = []
anterior = 0
#sorteando os valores e preenchendo o vetor numeros para colocar dentro da lista jogos
for sorteios in range (0, quantidade):
    numeros.clear()
    while len(numeros) < 6:
        elemento = (randint(1,60))
        if elemento not in numeros: #fazendo o teste para saber se o número é repetido
            numeros.append(elemento)
    numeros.sort() #ordenando a lista do menor para o maior
    jogos.append(numeros[:])
print('-='* 20)
for n, item in enumerate(jogos):
    print(f'O {n + 1}º jogo é: {item}')
    sleep(0.75)
d.rodape()
        

