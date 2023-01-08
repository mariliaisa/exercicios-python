import Dicionários as d
matriz = []
vetor = []
#colocando os valores dentro dos vetor três vetores e criando a lista com eles
for l in range (0,3):
    for c in range (0,3):
        vetor.append(int(input(f'Digite o valor da posição ({l}, {c}): ')))
    matriz.append(vetor[:])
    vetor.clear()
#mostrando os elementos da lista como uma matriz
for i, elementos in enumerate(matriz):
    print(f'[{matriz[i][0]:^5}]', end= '  ')
    print(f'[{matriz[i][1]:^5}]', end= '  ') 
    print(f'[{matriz[i][2]:^5}]', end= '  ') 
    print()