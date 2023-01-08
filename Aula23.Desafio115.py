from time import sleep
import Dicionários as d
from utilidadesCEV import dados


while True:
    sleep(0.51
    )
    dados.menu(['Ver Cadastro', 'Adicionar pessoas ao cadastro', 'Sair do sistema' ])
    while True:
        opcao = dados.leiaInt()
        if opcao != 1 and opcao !=2 and opcao != 3:
            sleep(0.5)
            print(f'{d.cor["vermelho"]}Digite uma opção válida!{d.cor["limpa"]}')
        else:
            break
    if opcao == 1:
        sleep(0.5)
        dados.lerArquivo()
    if opcao == 2:
        sleep(0.5)
        dados.escreverArquivo()
    if opcao == 3:
        sleep(0.5)
        d.rodape()
        break

 
    



