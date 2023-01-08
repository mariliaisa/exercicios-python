import emoji
from time import sleep
print('\033[35m=+' *5, 'CONTAGEM REGRESSIVA', '=+'*5,'\033[m') 
for contagem in range(10,-1,-1):
    print(contagem)
    sleep(1)
print(emoji.emojize('\033[1;34mUHUUUUUUUUUUUUUUUUUU!!!!!\033[m :sparkles:',language='alias'))
