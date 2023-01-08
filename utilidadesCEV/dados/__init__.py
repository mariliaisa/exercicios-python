import Dicionários as d
from time import sleep
def leiadinheiro():
    while True:
        num = str(input('Digite o valor: R$')).replace(',', '.').strip()
        if num.isnumeric():
            return float(num)    
        else:
            print(f'\033[1;31mERRO! Digite novamente\033[0m')



def leiaInteiro(texto=''):
    while True:
        texto = str(input('Digite um número: ')).strip()
        if texto.isnumeric():
            texto = int(texto)
            return texto
        else:
            print(f'\033[1;31mTente novamente.\033[0m')


def leiaInt():
    while True:
        try:
            numero = int(input(f'{d.cor["verde"]}Sua opção:{d.cor["limpa"]} '))
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
def linha(tam=42):
    print('-='*tam)



def menu(lista):
    d.cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{d.cor["amarelo"]}{c}{d.cor["limpa"]} - {d.cor["azulclaro"]}{item}{d.cor["limpa"]}')
        c += 1
    linha(20)

def lerArquivo():
    d.cabecalho("Pessoas Cadastradas")
    sleep(0.5)
    try:
        cadastro = open("dados.txt", "r")
    except:
        print(f'Ainda não há pessoas cadastradas.')
    else:
        if cadastro.read() == '':
            print(f'Ainda não há pessoas cadastradas.')
            cadastro.close()
        else:
            cadastro = open('dados.txt', 'r')
            for linha in cadastro:
                listinha = linha.split(';')
                listinha[1] = listinha[1].replace('\n', '')
                print(f'{d.cor["lilás"]}{listinha[0]:<30}{d.cor["limpa"]}{d.cor["azulpiscina"]}{listinha[1]:<3} anos{d.cor["limpa"]}')
            cadastro.close()



def escreverArquivo():
    cadastro = open("dados.txt", "a")
    nome = str(input('Nome: ').strip().title())
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print(f'Digite um número válido!')
        else:
            idade = str(idade)
            break
    cadastro.write(f'{nome};{idade}\n')
    cadastro.close()
   

