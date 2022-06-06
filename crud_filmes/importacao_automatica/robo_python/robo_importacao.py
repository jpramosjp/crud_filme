from classes.Repositorios.FilmeRepo import FilmeRepo
from classes.Repositorios.CategoriaRepo import CategoriaRepo
from cgitb import html
from urllib import response
from urllib.request import Request, urlopen
from urllib.error import URLError,HTTPError
from bs4 import BeautifulSoup

filmeRepo = FilmeRepo()
categoriaRepo = CategoriaRepo()

def verificaFilmeExiste(nomeFilme):
    retornoBuscaFilme = filmeRepo.buscarFilme(nomeFilme)
    if len(retornoBuscaFilme) == 0:
        return False
    return True

def verificarCategoriaExiste(categoria):
    retornoBuscaCategoria = categoriaRepo.buscarCategoria(categoria)
    if len(retornoBuscaCategoria) == 0:
        return False
    return retornoBuscaCategoria

def verificarPessoaExiste(nomePessoa):
    retornoBuscaCategoria = categoriaRepo.buscarCategoria(nomePessoa)
    if len(retornoBuscaCategoria) == 0:
        return False
    return retornoBuscaCategoria

def rasparDadosPessoas():
    print("teste")


def trataHTML(html):
    return " ".join(html.split()).replace('> <','><')




looping = 0
pagina = 1
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'
}
try:
    while(looping < 10):
        url = f'https://www.adorocinema.com/filmes-todos/?page={pagina}'    
        req  = Request(url, headers=headers)
        responses = urlopen(req)
        htmls = responses.read().decode('utf-8')
        soup = BeautifulSoup(htmls,'html.parser')
        filme={}
        
        anuncio = soup.find('div',{'class': 'card entity-card entity-card-list cf'})
        listaFilmes = soup.findAll('li',{'class':'mdl'})
        ultimoFilme = listaFilmes[-1].find('a',{'class': 'meta-title-link'}).get_text()
        if(verificaFilmeExiste(ultimoFilme)):
            pagina += 1
            continue

        for lista in listaFilmes:
            filme = lista.find('a',{'class': 'meta-title-link'}).get_text()
            if(verificaFilmeExiste(filme) == False):
                if lista.find('span',{'class': 'date'}):
                    dataLancamento = lista.find('span',{'class': 'date'}).get_text()
                    categoriaFilme = lista.find('div',{'class': 'meta-body-item meta-body-info'}).find_all('span')[2].findNext('span').get_text()
                    tipoFilme = verificarCategoriaExiste(categoriaFilme)
                    if(tipoFilme == False):
                        tipoFilme = categoriaRepo.inserirCategoria(categoriaFilme)
                    direcao = lista.find('div', {'class' : 'meta-body-item meta-body-direction'}).find('a')
                    if(verificaFilmeExiste(direcao.text) == False):


                        


except HTTPError as e:
    print(e.status,e.reason)
except URLError as e:
    print(e.reason)    