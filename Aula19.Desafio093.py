aproveitamento = dict()
gols = []
totGols = 0
aproveitamento["nome"] = str(input('Nome do jogador: ')).strip().capitalize()
aproveitamento["Número de partidas"] = int(input('Partidas jogadas: '))
for g in range (0, aproveitamento['Número de partidas'] ):
    gols.append(int(input(f'Quantos gols na partida {g + 1}?: ')))
    totGols += gols[g]
aproveitamento["Gols por partida"] = gols[:]
aproveitamento["Total de Gols marcados"] = totGols
print('-=' * 30)
print(f'O jogador {aproveitamento["nome"]} jogou {aproveitamento["Número de partidas"]} partidas.')
for p, g in enumerate(gols):
    print(f'=> Na partida {p + 1} fez {g} gol(s).')
print(f'Fez um total de {totGols} gol(s)')