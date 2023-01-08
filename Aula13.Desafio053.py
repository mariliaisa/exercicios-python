frase = str(input('Digite uma frase: ')).strip().upper().split()
frase = ''.join(frase)
esq = -1
dir = 0
resultado = 0
for i in range(0, len(frase)//2):
    if frase[dir] != frase[esq]:
        resultado = resultado + 1
    esq = esq - 1
    dir = dir + 1
if resultado > 0:
    print('\nA frase não é um palíndromo!')
else:
    print('\nA frase é um palíndromo!')
