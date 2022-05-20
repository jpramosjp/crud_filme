from operator import concat
from classes.bd.Conexao import Conexao

class FilmeRepo:
    xsql = ''

    def __init__(self):
        self.xsql = Conexao()
    
    def buscarFilme(self,nomeFilme):
        try:
            sql = "SELECT * FROM filmes WHERE nome = '" + nomeFilme + "'"
            retorno = self.xsql.requisitar(sql)
            return retorno 
        except Exception as e:
            print(e)
            return False