from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: ')).strip().capitalize()
anoNasc = int(input('Ano de nascimento: '))
atual = date.today().year
cadastro['idade'] = (atual - anoNasc)
cadastro['CTPS'] = int(input('Nº da CTPS:(Digite 0 se não tiver)  '))
if cadastro['CTPS'] != 0 :
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    aposentadoria = cadastro['Ano de contratação'] + 35
    cadastro['Aposentadoria'] = aposentadoria - atual + cadastro['idade']
    print('-='* 30)
    print("""
Nome: {}
Idade: {} anos
CTPS: {}
Ano de contratação: {}
Salário: {}
Se aposentará com {} anos no ano de {}.""".format(cadastro['nome'], cadastro['idade'], cadastro['CTPS'], cadastro['Ano de contratação'], cadastro['Salário'], cadastro['Aposentadoria'], aposentadoria))
else:
    print('-='* 30)
    print("""
Nome: {}
Idade: {} anos
CTPS: {}""".format(cadastro['nome'], cadastro['idade'], cadastro['CTPS']))