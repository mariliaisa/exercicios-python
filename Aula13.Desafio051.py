n1 = int(input('Digite o prmeiro termo da sequência que você deseja: '))
r = int(input('Digite a razão da PA: '))
termo = int(input('Digite a quantidade de termos da PA: '))
n_termo = n1 + (termo - 1) * r
print('Os 10 primeiros termos da PA com 1º termo {} e razão {} são:'.format(n1, r))
for c in range(n1, n_termo + 1, r):
    print(c, end=' → ')


#minha resolução
"""for termos in range(1,11):
    print(n1, end=' ')
    n1 = n1 + n2"""
    
