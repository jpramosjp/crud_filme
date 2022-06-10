from ntpath import join
from classes.Repositorios.FilmeRepo import FilmeRepo
from classes.Repositorios.CategoriaRepo import CategoriaRepo
from classes.Repositorios.FuncoesRepo import FuncoesRepo
from classes.Repositorios.PessoasRepo import PessoasRepo
from cgitb import html
from urllib import response
from urllib.request import Request, urlopen
from urllib.error import URLError,HTTPError
from bs4 import BeautifulSoup
import os
import requests
from unidecode import unidecode 
import base64
import re
import lxml
from PIL import Image
from io import BytesIO
import json
from serpapi import GoogleSearch
import urllib.request as fe
import urllib.request


filmeRepo = FilmeRepo()
categoriaRepo = CategoriaRepo()
funcoesRepo = FuncoesRepo()
pessoasRepo = PessoasRepo()

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
    retornoBuscaPessoa = pessoasRepo.buscarPesoa(nomePessoa)
    if len(retornoBuscaPessoa) == 0:
        return False
    return retornoBuscaPessoa

def rasparDadosPessoas(html):
    url = f'https://www.adorocinema.com{html}'
    reqPessoa =  Request(url, headers=headers)
    responses = urlopen(reqPessoa)
    htmlss = responses.read().decode('utf-8')
    soupPessoa = BeautifulSoup(htmlss,'html.parser')
    nome = ''
    idade = ''
    nacionalidade = ''
    retornoFuncoes = ''
    try:
        ativadade = soupPessoa.find_all('div',{'class' : 'meta-body-item'})[0].find('strong').text.replace('\n','').strip().upper()
        retornoFuncoes = funcoesRepo.buscarFuncao(ativadade)
        if (len(retornoFuncoes) == 0):
            print("teste")
            retornoFuncoes = funcoesRepo.inserirFuncao(ativadade)
        nome = soupPessoa.find('div',{'class' : 'titlebar-title titlebar-title-lg'}).text.strip().upper()
        idade = soupPessoa.find('div',{'class' : 'meta-body'}).find_all('div',{'class' : 'meta-body-item'})[-1].find('strong').text
        posicaoNacionalidade = soupPessoa.find('div',{'class' : 'meta-body'}).find_all('div',{'class' : 'meta-body-item'})
        nacionalidade = ''
        if(posicaoNacionalidade[1].find('span').text.strip() == 'Nacionalidade'):
            nacionalidade = posicaoNacionalidade[1].contents[2].replace('\n','').upper()
        if(posicaoNacionalidade[2].find('span').text.strip() == 'Nacionalidade'):
            nacionalidade = posicaoNacionalidade[2].contents[2].replace('\n','').upper()
    except:
        pass    
    return pessoasRepo.inserirPessoa(nome, idade, nacionalidade,str(retornoFuncoes[0][0]))





def pegarImagem(nomeFilme):
    


    params = {
      "api_key": 'c3e50e2347792ac18a0930a8d8f760fafc7c54457931a63ea7fa8ea765fb545c',
      "engine": "google",
      "q": unidecode(nomeFilme.replace(':',''))+" capa de filme",
      "tbm": "isch"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
    urllib.request.install_opener(opener)
    fe.urlretrieve(results['images_results'][0]['original'], unidecode(nomeFilme.replace(':','')) + ".jpg")
    with open(unidecode(nomeFilme.replace(':','')) + ".jpg", "rb") as arquivoImagem:
        imagemBase64 = base64.b64encode(arquivoImagem.read())
    os.remove(unidecode(nomeFilme.replace(':','')) + ".jpg")
  

    return imagemBase64
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
                    dataLancamento = lista.find('span',{'class': 'date'}).get_text().upper()
                    categoriaFilme = lista.find('div',{'class': 'meta-body-item meta-body-info'}).find_all('span')[2].findNext('span').get_text()
                    tipoFilme = verificarCategoriaExiste(categoriaFilme)
                    if(tipoFilme == False):
                        tipoFilme = categoriaRepo.inserirCategoria(categoriaFilme.upper())
                    try:
                        direcao = lista.find('div', {'class' : 'meta-body-item meta-body-direction'}).find('a')
                        diretor = verificarPessoaExiste(direcao.text.upper())
                        if(diretor == False):
                            diretor = rasparDadosPessoas(direcao['href'])
                    except:
                        pass 
                    elenco = lista.find('div',{'class' : 'meta-body-item meta-body-actor'}).find('a')
                    if (elenco == None):
                        continue
                    ator = verificarPessoaExiste(elenco.text.upper())                   
                    if(ator == False) :
                        ator = rasparDadosPessoas(elenco['href'])
                    detalhes = lista.find('div',{'class' : 'content-txt'}).text.replace('\n','').upper()         
                    imagemCriptografada = pegarImagem(filme.strip().lower())
                    parametrosFilme = [     filme.strip().upper(),
                                            dataLancamento,
                                            str(tipoFilme[0][0]),
                                            str(diretor[0][0]),
                                            str(ator[0][0]),
                                            detalhes,
                                            str(imagemCriptografada.decode('utf-8'))
                                      ]
                    textoConvertido =[]
                    for _ in parametrosFilme :
                        textoConvertido.append("'".join(["", _ ,""]))
                    retornoInserirFilme = filmeRepo.inserirFilme("," . join(textoConvertido))
        looping += 1

                        


except HTTPError as e:
    print(e.status,e.reason)
except URLError as e:
    print(e.reason)    