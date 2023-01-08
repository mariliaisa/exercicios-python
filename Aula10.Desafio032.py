# divisel por 4 e não por 100. Caso seja também 100, tem que ser por 400
import datetime
ano = int(input('Digite um ano ou  0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('\033[1;4;34;40mO ano é bissexto!\033[m')
else:
    print('\033[1;7;30mO ano não é bissexto!\033[m')

"""div1 = ano % 4
div2 = ano % 100
div3 = ano % 400
if div1 != 0 :
    print(emoji.emojize('O ano não é bissexto! :thumbsdown:'.format(ano), language='alias'))
    if div1 == 0 and div2 != 0:
        print(emoji.emojize('O ano {} é bissexto! :thumbsup:'.format(ano), language='alias'))
else:
    if div3 == 0:
        print(emoji.emojize('O ano {} é bissexto! :thumbsup:'.format(ano), language='alias'))
    else:
        print(emoji.emojize('O ano {} não é bissexto! :thumbsdown:'.format(ano), language='alias'))"""
