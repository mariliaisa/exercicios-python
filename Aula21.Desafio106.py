def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4 
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)


#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA')
    comando =str(input('Função ou biblioteca --> ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')
