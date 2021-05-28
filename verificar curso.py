from bs4 import BeautifulSoup as bs
import urllib.request
from time import sleep

x = urllib.request.urlopen('https://acessograduacao.ufrj.br/')

resultado = bs(x,'lxml')
resultado = str(resultado.text)


#f = open("mudancacurso.txt", "w")
#f.write(resultado)
#f.close()

f = open("mudancacurso.txt", "r")

if resultado == f.read():
    print("mesma coisa - pagina inicial mudanca curso")
else:
    print("DIFERENTES!!! - pagina inicial mudanca curso")
    
f.close()




x = urllib.request.urlopen('http://www.intercambio.poli.ufrj.br/pt/editais')

resultado = bs(x,'lxml')
resultado = str(resultado.text)


#f = open("intercambio.txt", "w")
#f.write(resultado)
#f.close()

f = open("intercambio.txt", "r")

if resultado == f.read():
    print("mesma coisa - pagina inicial intercambio")
else:
    print("DIFERENTES!!! - pagina inicial intercambio")
    
f.close()

sleep(3)