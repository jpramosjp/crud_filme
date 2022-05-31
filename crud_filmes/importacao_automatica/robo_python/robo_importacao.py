
from tkinter.tix import Tree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from classes.Repositorios.FilmeRepo import FilmeRepo
import time

from selenium.webdriver.firefox.options import Options

profile = webdriver.FirefoxProfile()
adblockfile = r'\Users\joao.joao\Downloads\adblock_plus-3.13.xpi'
#profile.add_extension(adblockfile)

filmeRepo = FilmeRepo()

def verificaFilmeExiste(nomeFilme):
    retornoBuscaFilme = filmeRepo.buscarFilme(nomeFilme)
    if len(retornoBuscaFilme) == 0:
        return False
    return True

# def verificarAds():
#     all_iframes = driver.find_elements_by_tag_name("iframe")
#     if len(all_iframes) > 0:
#         print("Ad Found\n")
#         driver.execute_script("""
#             var elems = document.getElementsByTagName("iframe"); 
#             for(var i = 0, max = elems.length; i < max; i++)
#              {
#                  elems[i].hidden=true;
#              }
#                           """)
#         print('Total Ads: ' + str(len(all_iframes)))
#     return True

driver = webdriver.Firefox()
#driver.install_addon('C:/Users/joao.joao/Downloads/adblock_plus-3.13.xpii')
time.sleep(10)
driver.get('https://www.adorocinema.com/filmes-todos/')
contador = 1
try:
    for i in range(1,10):

        tabelaFilmes =WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content-layout"]/section[3]/div[2]/ul')))
        listasFilmes = WebDriverWait(tabelaFilmes,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'mdl')))

        nomeUltimoFilme = WebDriverWait(listasFilmes[-1],10).until(EC.presence_of_element_located((By.CLASS_NAME,'meta-title-link'))).get_attribute('text')

        if verificaFilmeExiste(nomeUltimoFilme) == True:
            contador += 1
            driver.get('https://www.adorocinema.com/filmes-todos/?page='+ str(contador))
            continue
        for linha in range(len(listasFilmes)):
            nomeFilme = WebDriverWait(listasFilmes[linha],10).until(EC.presence_of_element_located((By.CLASS_NAME,'meta-title-link'))).get_attribute('text')
            if verificaFilmeExiste(nomeFilme):
                continue
            tipoFilme = WebDriverWait(listasFilmes[linha],10).until(EC.presence_of_element_located((By.CLASS_NAME,'meta-body-item meta-body-info'))).find_element((By.TAG_NAME,'a')).get_attribute('text')
            diretor = WebDriverWait(listasFilmes[i],10).until(EC.presence_of_element_located((By.CLASS_NAME, 'meta-body-item meta-body-direction'))).get_attribute('text')
            ator = WebDriverWait(listasFilmes[i],10).until(EC.presence_of_element_located((By.CLASS_NAME('meta-body-item meta-body-actor')))).get_attribute('text')
            detalhes = WebDriverWait(listasFilmes[i],10).until(EC.presence_of_element_located((By.CLASS_NAME,'content-txt')))
except Exception as e:
    print(e)




# #
# from cgitb import html
# from urllib import response
# from urllib.request import Request, urlopen
# from urllib.error import URLError,HTTPError
# from bs4 import BeautifulSoup

# def trataHTML(html):
#     return " ".join(html.split()).replace('> <','><')


# url = 'https://www.adorocinema.com/filmes-todos/'


# headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'
# }
# try:
#     req  = Request(url, headers=headers)
#     responses = urlopen(req)
#     htmls = responses.read().decode('utf-8')
#     #htmls = trataHTML(htmls)
#     soup = BeautifulSoup(htmls,'html.parser')

#     filme={}
    
#     anuncio = soup.find('div',{'class': 'card entity-card entity-card-list cf'})
#     listaFilmes = soup.findAll('li',{'class':'mdl'})
#     for lista in listaFilmes:
#         print(lista.find('a',{'class': 'meta-title-link'}).get_text())
#         if lista.find('span',{'class': 'date'}):
#             print(lista.find('span',{'class': 'date'}).get_text())
#         print(lista.find('div',{'class': 'meta-body-item meta-body-info'}).find_all('span')[2].findNext('span').get_text())

# except HTTPError as e:
#     print(e.status,e.reason)
# except URLError as e:
#     print(e.reason)    