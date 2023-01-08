import Dicionários as d
lista_de_alunos = list()
notas = []
nome_e_notas = []
media = []
#Preenchendo as listas notas, nome_e_notas e lista_de_alunos e média por inputs e append:
while True:
    notas.clear()
    nome_e_notas.clear()
    nome_e_notas.append((str(input('Nome do aluno: '))))
    notas.append(float(input('1º Nota: ')))
    notas.append(float(input('2ª Nota: ')))
    media.append((notas[0] + notas[1])/2)
    nome_e_notas.append(notas[:])
    lista_de_alunos.append(nome_e_notas[:])
    escolha = d.quer_continuar()
    if escolha == False:
        break

#Mostrando na formatação pedida
d.cabecalho('BOLETIM')
print('{:<10}{:<10}{:>10}'.format('Nº', 'Aluno', 'Média'))
print('-'* 40)
for n, aluno in enumerate(lista_de_alunos):
    print('{:<10}{:<10}'.format(n, lista_de_alunos[n][0]), end='')
    print('{:>10}'.format(media[n]))
print('-'* 40)

#Mostrando as notas individuais
while True:
    n = int(input('Deseja ver a nota de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    elif n not in range(len(lista_de_alunos)):
        print('Opção inválida!')
    else:
        print(f'As notas de {lista_de_alunos[n][0]} foram {lista_de_alunos[n][1][0]} e {lista_de_alunos[n][1][1]}')

d.rodape()