from operator import itemgetter
import Dicionários as d
from random import randint
from time import sleep

#criando o dicionário:
jogo = {'jogador 1': randint(1,6),
 'jogador 2': randint(1,6), 
 'jogador 3': randint(1,6), 
 'jogador 4': randint(1,6)
}
ranking = dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.75)

#ordenando o dicionario com a função itemgetter()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f'Em {i + 1}º: {v[0]} com {v[1]}.')
    sleep(0.5)