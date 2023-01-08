lista = ('PATRONO', 'ESTUPEFAÇA', 'WINGUARDIUM LEVIOSA', 'AVADA KEDAVRA', 'LUMUS', 'ALO HOMORA', 'CRUCIUS', 'ACCIO', 'IMPERIUS', 'REPARO')
for feitiço in (lista):
    print('\nA palavra \033[1;36m{}\033[m possui as vogais: '.format(feitiço), end='')
    for letra in (feitiço):
        if letra in 'AEIOU':
            print(letra, end=' ')

