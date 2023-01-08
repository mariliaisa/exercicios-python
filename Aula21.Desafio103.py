def jogo(jogador='', gols=0):
    if jogador == '':
        jogador = 'Desconhecido'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s).')


#PROGRAMA PRINCIPAL
jogador = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Gols marcados: '))
jogo(jogador, gols)
