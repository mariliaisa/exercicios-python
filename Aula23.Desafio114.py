#ABRINDO SITES COM PYTHON
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.python.org/')
except:
    print('O site não está acessível.')
else:
    print('Consegui acessar o site!')
