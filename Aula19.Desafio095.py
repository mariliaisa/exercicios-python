import Dicionários as d
aproveitamento = dict()
gols = []
totGols = 0
listaJogadores = list()
while True:
    aproveitamento.clear()
    gols.clear()
    aproveitamento["nome"] = str(input('Nome do jogador: ')).strip().capitalize()
    aproveitamento["Nº partidas"] = int(input('Partidas jogadas: '))
    for g in range (0, aproveitamento['Nº partidas'] ):
        gols.append(int(input(f'Quantos gols na partida {g + 1}?: ')))
        totGols += gols[g]
    aproveitamento["Gols"] = gols.copy()
    aproveitamento["Total"] = totGols
    listaJogadores.append(aproveitamento.copy())
    escolha = d.quer_continuar()
    if escolha == False:
        break
#colocando na formatação correta
print('-='* 30)
print('cod', end=' ')
for elemento in aproveitamento.keys():
    print(f'{elemento:<20}', end=' ')
print()
print('-=' * 50)
for j, dados in enumerate(listaJogadores):
    print(f'{j:>3}', end=' ')
    for i in dados.values():
        print(f'{str(i):<20}', end=' ')
    print()
print('-=' * 50)

#solicitando os dados individuais do jogador
while True:
    n = int(input('Deseja ver o aproveitamento de qual jogador? (999 interrompe): '))
    if n == 999:
        break
    elif n not in range(0,len(listaJogadores)):
        print('Opção inválida!')
    else:
        print(f'Aproveitamento do jogador {listaJogadores[n]["nome"]}:')
        for e in range(1, listaJogadores[n]["Nº partidas"] + 1):
            print(f'No jogo {e} fez {listaJogadores[n]["Gols"][e-1]} gols.')
