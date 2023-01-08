import Dicionários as d
print('-' * 20)
maiores_idade = homens = mulheres_under20 = total_pessoas = 0
while True:
    print('=' * 50)
    idade = int(input('Digite sua idade: '))
    while True:
        sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
        if sexo == 'F' or sexo == 'M':
            break
    while True:   
        continuar = str(input('Deseja continuar a cadastrar pessoas [S/N]? ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
    total_pessoas += 1
    if idade >= 18:
        maiores_idade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_under20 += 1
    if continuar == 'N':
        break
       
print('\n{:*^50}'.format('FIM DO PROGRAMA'))
print("""PARTICIPARAM DA PESQUISA: {} PESSOA(S)

{}1- TOTAL DE PESSOAS MAIORES DE 18 ANOS: {}{}
{}2- TOTAL DE HOMENS CADASTRADOS: {}{}
{}3- TOTAL DE MULHERES COM MENOS DE 20 ANOS: {}{}""".format(total_pessoas, d.cor['amarelo'], maiores_idade, d.cor['limpa'], d.cor['lilás'],homens, d.cor['limpa'], d.cor['verde'], mulheres_under20, d.cor['limpa']))