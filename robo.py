from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Carregando e lendo o txt onde estao as informaçoes
listaSites = open("ListaSites.txt", "r")
listaSitesSaida = open("ListaSitesSaida.txt", "w")

#Navegador a ser aberto ex: Opera
#deixado em branco justamente para abrir o navegador padrao que utiliza no windows
#driver = webdriver.Opera('C:\Users\rafae\Desktop\pythonRobos\operadriver.exe')
driver = webdriver.Opera()
time.sleep(2)

#site que vai abrir
driver.get('http://registro.br')
time.sleep(1)

for dominio in listaSites:
    pesquisa = driver.find_element_by_id("is-avail-field")#pesquisa o conteudo da imput que vai ser colocado os dados
    pesquisa.clear()#limpa a imput caso haja alguma coisadigitada
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultados = driver.find_elements_by_tag_name("strong")#produta pelo strong onde esta escrito se esta ou nao disponivel
    listaSitesSaida.write(dominio +" - "+ resultados[4].text+"\n")#vai salvando no txt de saida


listaSites.close()
listaSitesSaida.close()
driver.close()