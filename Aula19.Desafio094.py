cadastro = dict()
listaPessoas = list()
contP = somaP = 0
import Dicionários as d
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        cadastro['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
        if cadastro['sexo'] in 'FM':
            break
    cadastro['idade'] = int(input('Idade: '))
    contP += 1
    somaP += cadastro['idade']
    listaPessoas.append(cadastro.copy())
    escolha = d.quer_continuar()
    if escolha == False:
        break
media = somaP/contP
print('-=' * 30)
print(f'a) Nº de pessoas cadastradas: {len(listaPessoas)}')
print(f'b) A média de idade do grupo é: {media}')
print(f'c) A lista de mulheres cadastradas é: ')
for i, elemento in enumerate(listaPessoas):
    if listaPessoas[i]['sexo'] == 'F':
        print(listaPessoas[i]['nome'])
print(f'd) A lista de pessoas com idade acima da média é: ')
for i, elemento in enumerate(listaPessoas):
    if listaPessoas[i]['idade'] > media:
        print(listaPessoas[i]['nome'])