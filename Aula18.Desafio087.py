import Dicionários as d
matriz = [[], [], []]
d.cabecalho('MATRIZ')
soma_pares = soma_3_coluna = maior = 0
#colocando os valores dentro dos vetor três vetores e criando a lista com eles
for l in range (0,3):
    for c in range (0,3):
        vetor = (int(input(f'Digite o valor da posição ({l}, {c}): ')))
        matriz[l].append(vetor)
#mostrando os elementos da lista como uma matriz
for l in range(0,2):
    for c in (0,2):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
#soma de todos os valores pares:
for elemento in matriz:
    for i in elemento:
        if i % 2 == 0:
            soma_pares += i
#soma da terceira coluna:
for i, elementos in enumerate(matriz):
    soma_3_coluna +=  matriz[i][2]                
maior = max(matriz[1])
print()
print('-='*20)
print(f'\nA soma dos elementos pares: {soma_pares}')
print(f'A soma dos elementos da terceira coluna: {soma_3_coluna}')
print(f'O maior elemento da segunda linha: {maior}')
d.rodape()
