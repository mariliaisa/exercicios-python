import Dicionários as d
lista_num = [[],[]]

d.cabecalho('LISTA PAR OU ÍMPAR?')
#separando os elementos em pares e impares
for i in range(0,7):
    numero = int(input(f'Digite o {i + 1}º número: '))
    if numero % 2 == 0:
        lista_num[0].append(numero)
    else:
        lista_num[1].append(numero)
#ordenando a lista_num para ordem crescente
lista_num[0].sort()
lista_num[1].sort()
#mostrando os resultados
print(f' A lista digitada foi: {lista_num}')
print(f'Os números ímpares digitados: {lista_num[1]}')
print(f'Os números pares digitados: {lista_num[0]}')
d.rodape()