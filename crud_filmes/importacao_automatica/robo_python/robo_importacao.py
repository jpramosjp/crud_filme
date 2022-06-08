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



filmeRepo = FilmeRepo()
categoriaRepo = CategoriaRepo()
funcoesRepo = FuncoesRepo()
pessoasRepo = PessoasRepo()
caminho = "C:/xampp/htdocs/crud_filmes/crud_filme/crud_filmes/imagens/"

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
    return pessoasRepo.inserirPessoa(nome, idade, nacionalidade,str(retornoFuncoes[0][0]))

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)



def criarPasta(caminho): 
    try:  
        os.mkdir(caminho)   
    except Exception as e: 
        print(e) 
        criarPasta() 
  
    


def pegarImagem(nomeFilme):
    
    parametross = {
    "q": unidecode(nomeFilme.replace(':','')) + " capa de filme",
    "sourceid": "chrome",
    }
    #url = 'https://www.google.com/search?q=' + unidecode(nomeFilme.replace(':','').replace(" ","+")) + '+capa+filme&sxsrf=ALiCzsZUw68Dmrp331rvSttffHQ-IBgbGg:1654652259123&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjq3oaB3Jz4AhWWJrkGHRaXAI4Q_AUoAXoECAEQAw&biw=1536&bih=694&dpr=1.25'
    html =  requests.get("https://www.google.com/search",params = parametross, headers=headers)
 
    
    soupImagem = BeautifulSoup(html.text,'lxml')

    for result in soupImagem.select('div[jsname=dTDiAc]'):
        link = f"https://www.google.com{result.a['href']}"
        being_used_on = result['data-lpage']
        print(f'Link: {link}\nBeing used on: {being_used_on}\n')
    #imagem = soupImagem.find('div',{'class':'bRMDJf islir'}).find('img')
    script_img_tags = soupImagem.find_all('script')
    img_matches = re.findall(r"s='data:image/jpeg;base64,(.*?)';", str(script_img_tags))
    for index, image in enumerate(img_matches):
        try:
            # https://stackoverflow.com/a/6966225/15164646
            final_image = Image.open(BytesIO(base64.b64decode(str(image))))

            # https://www.educative.io/edpresso/absolute-vs-relative-path
            # https://stackoverflow.com/a/31434485/15164646
            final_image.save(f'{caminho}inline_image.jpg', 'JPEG')
        except:
            pass
    # try: 
    #     imagemLink = imagem["src"] 
    #     #imagemLink = "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""" 
    #     #imagemLink = imagemLink.encode('utf-8')
        
    #     imagemBas64 = requests.get(imagemLink).content 
    #     str(imagemBas64, 'utf-8')
    #     print(str(imagemBas64, 'utf-8'))
    # except Exception as e: 
    #    print(e)
    # try: 
    #         pasta = os.path.join(caminho, str(nomeFilme.replace(":","").replace(" ","-")))
    #         criarPasta(pasta) 
    #         with open(pasta + "/" + nomeFilme.replace(" ","-")+".jpg", "wb+") as f: 
    #             f.write( base64.decodebytes(imagemLink)) 
    # except Exception as e:
    #     print(e) 

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
                        tipoFilme = categoriaRepo.inserirCategoria(categoriaFilme.upper())
                    direcao = lista.find('div', {'class' : 'meta-body-item meta-body-direction'}).find('a')
                    diretor = verificarPessoaExiste(direcao.text.upper())
                    if(diretor == False):
                        diretor = rasparDadosPessoas(direcao['href']) 
                    elenco = lista.find('div',{'class' : 'meta-body-item meta-body-actor'}).find('a')
                    ator = verificarPessoaExiste(elenco.text.upper())
                    if(ator == False) :
                        ator = rasparDadosPessoas(elenco['href'])
                    detalhes = lista.find('div',{'class' : 'content-txt'}).text.replace('\n','').upper()         
                    imagemLink = pegarImagem(filme.strip().lower())
                        


except HTTPError as e:
    print(e.status,e.reason)
except URLError as e:
    print(e.reason)    