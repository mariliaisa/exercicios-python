soma = 0
cont = 0
for c in range(1,501):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
        cont+= 1
print('A soma de todos os {} valores é igual a {}'.format(cont, soma))


"""for c in range (1, 501, 2)
    if c % 3 == 0:
        soma = coma + c
print(soma)

"""