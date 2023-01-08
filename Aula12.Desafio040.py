import emoji
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua média foi: {:.2f}'.format(media))
if media < 5:
    print(emoji.emojize('\033[1;31mVocê foi reprovado!\033[m :sob:', language='alias'))
elif 5 <= media < 7:
    print(emoji.emojize('\033[1;33mVocê está de recuperação!\033[m :scream:', language='alias'))
else:
    print(emoji.emojize('\033[1;34mVocê foi aprovado!\033[m :sparkles:', language='alias'))
