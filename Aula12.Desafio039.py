from datetime import date
from time import sleep
sexo = int(input("""Qual o seu sexo?
\033[1;31m1 - Feminino\033[m
\033[1;34m2 - Masculino\033[m\n"""))
if sexo == 1:
    print('Seu alistamento não é obrigatório!!!')
else:
    ano_nasc = int(input('Digite o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    print('Você possui {} anos!'.format(idade))
    print('Analisando...')
    sleep(0.95)
    if idade < 18:
        saldo = 18 - idade
        print('Você é menor de idade. Ainda faltam {} anos para você se alistar!'.format(saldo))
        ano = ano_atual - saldo
        print('O ano do seu alistamento será {}'.format(ano))
    elif idade == 18:
        print('A hora é agora! vamos pintar muro e cortar grama, recruta!')
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos! Ainda está no exército ou foi dispensado?'.format(saldo))
        ano = ano_atual - saldo
        print('O ano do seu alistamento foi em {}'.format(ano))