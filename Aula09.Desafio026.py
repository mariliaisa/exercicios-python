frase = str(input('Digite uma frase: ')).strip().upper()
print("""Há {} letra(s) "a"
A 1º letra "a" aparece na posição {}
A última letra "a" aparece na posição: {}""".format(frase.count('A'), frase.find('A'), frase.rfind('A')))
