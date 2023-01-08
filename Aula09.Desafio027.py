#PROGRAMA QUE MOSTRA O PRIMEIRO E O ÚLTIMO NOME
nome = input('Digite seu nome completo: ').strip().title().split()
print('Primeiro nome: {}'.format(nome[0]))
print('último nome: {}'.format(nome[len(nome)-1]))
