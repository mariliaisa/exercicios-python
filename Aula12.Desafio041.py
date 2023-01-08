from datetime import date
import emoji
ano_nasc = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano_nasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print(emoji.emojize('Sua categoria é MIRIM :baby:', language='alias'))
elif idade <= 14:
    print(emoji.emojize('Sua categoria é INFANTIL :girl: :boy:', language='alias'))
elif idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade <= 25:
    print('Sua categoria é SÊNIOR!')
else:
    print(emoji.emojize('Sua categoria é MASTER! :older_woman: :older_man:', language='alias'))
