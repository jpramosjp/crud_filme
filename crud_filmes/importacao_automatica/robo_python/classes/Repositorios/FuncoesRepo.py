from classes.bd.Conexao import Conexao

class FuncoesRepo:
    xsql = ''

    def __init__(self):
        self.xsql = Conexao()
    
    def buscarFuncao(self,funcao):
        try:
            sql = "SELECT codigo FROM funcoes WHERE descricao = '" + funcao + "'"
            retorno = self.xsql.requisitar(sql)
            return retorno 
        except Exception as e:
            print(e)
            return False
    
    def inserirFuncao(self,funcao):
        try:
            sql = "INSERT INTO funcoes(descricao) VALUES ('" + funcao + "')"
            self.xsql.inserir(sql)
            sql = "SELECT LAST_INSERT_ID() as codigo;"
            retorno = self.xsql.requisitar(sql)
            return retorno
        except Exception as e:
            print(e)
            return False