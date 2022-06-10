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
    def inserirFilme(self,parametros):
        try:
            sql = "INSERT INTO filmes(nome, data_lancamento, tipo_filme, diretor, ator_principal, detalhes, imagem_b64) Values (" + parametros + ");"
            retorno = self.xsql.inserir(sql)
            return True
        except Exception as e:
            print(e)
            return False