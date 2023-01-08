import Dicionários as d
dados = []
lista_pessoas = []
maior = menor = 0
d.cabecalho('LISTA DE PESSOAS')
#Montando a lista dados através de inputs
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista_pessoas.append(dados[:]) 

#comparando os dados para descobrir o maior e o menor peso:
    if len(lista_pessoas) == 1:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados [1] < menor:
        menor = dados[1]
    dados.clear() #limpar a lista dados para que ela receba outro input
    escolha = d.quer_continuar()
    print('-='* 20)
    if escolha == False:
        break
    
#número de pessoas cadastradas:
print(f'Foram cadastradas: {len(lista_pessoas)} pessoa(s)')
#pessoas mais pesadas e mais leves:
print(f'O maior peso foi {maior}kg para: ')
for p in lista_pessoas:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi {menor}kg para: ')
for p in lista_pessoas:
    if p[1] == menor:
        print(f'{p[0]}')
d.rodape()