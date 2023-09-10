import urllib
import urllib.request

'''Verifica se o computador está conseguindo acessar o site http://www.pudim.com.br'''
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro!')
else:
    print('Deu certo')