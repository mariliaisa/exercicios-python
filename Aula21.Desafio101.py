from time import sleep
def voto(ano=1900):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return (f'Você tem {idade} anos, O VOTO É PROIBIDO!')
    elif 16 <= idade < 18 or idade > 65:
        return (f'Você tem {idade} anos, O VOTO OPCIONAL!')
    else:
        return (f'Você tem {idade} anos, O VOTO É OBRIGATÓRIO')
    return opcao

#PROGRAMA PRINCIPAL
ano = int(input('Em qual ano você nasceu? '))
print('Analisando...')
sleep(0.6)
print(voto(ano))
print('-='* 20)