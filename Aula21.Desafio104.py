import Dicionários as d
def leiaInt(texto=''):
    while True:
        texto = str(input('Digite um número: ')).strip()
        if texto.isnumeric():
            texto = int(texto)
            return f'Você acabou de digitar o número {texto}'
        else:
            print(f'{d.cor["vermelho"]}Tente novamente.{d.cor["limpa"]}')



#Programa principal
n = leiaInt()
print(f'{d.cor["verde"]}{n}{d.cor["limpa"]}')
