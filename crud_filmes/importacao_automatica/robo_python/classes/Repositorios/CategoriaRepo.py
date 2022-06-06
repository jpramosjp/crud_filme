from classes.bd.Conexao import Conexao

class CategoriaRepo:
    xsql = ''

    def __init__(self):
        self.xsql = Conexao()
    
    def buscarCategoria(self,nomeCategoria):
        try:
            sql = "SELECT codigo FROM tipo_filme WHERE descricao = '" + nomeCategoria + "'"
            retorno = self.xsql.requisitar(sql)
            return retorno 
        except Exception as e:
            print(e)
            return False
    
    def inserirCategoria(self,nomeCategoria):
        try:
            sql = "INSERT INTO tipo_filme(descricao) VALUES ('" + nomeCategoria + "')"
            self.xsql.inserir(sql)
            sql = "SELECT LAST_INSERT_ID() as codigo;"
            retorno = self.xsql.requisitar(sql)
            return retorno
        except Exception as e:
            print(e)
            return False