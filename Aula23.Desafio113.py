import Dicionários as d
def leiaInt():
    while True:
        try:
            numero = int(input('Digite um número: '))
        except(ValueError, TypeError):
            print(f'{d.cor["vermelho"]}Valor inválido. Tente novamente.{d.cor["limpa"]}')
        else:
            return numero



def leiaFloat():
    while True:
        try:
            numero = float(input('Digite um número: '))
        except(ValueError, TypeError):
            print(f'{d.cor["vermelho"]}Valor inválido. Tente novamente.{d.cor["limpa"]}')
        else:
            return numero


#Programa principal
n1 = leiaInt()
n2 = leiaFloat()
print(f'Você digitou o número {d.cor["verde"]}{n1}{d.cor["limpa"]}')
print(f'Você digitpu o número {d.cor["lilás"]}{n2}{d.cor["limpa"]}')