#FUNÇÃO PARA MENSAGEM COM TAMANHO ADAPTÁVEL
def escreva(texto):
    print('=' * (len(texto) + 2))
    print('{:^10}'.format(texto ))
    print('=' * (len(texto) + 2))


#PROGRAMA PRINCIPAL
frase = str(input('Digite uma frase: ')).strip()
escreva(frase)