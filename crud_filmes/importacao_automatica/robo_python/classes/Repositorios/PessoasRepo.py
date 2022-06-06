from classes.bd.Conexao import Conexao

class PessoasRepo:
    xsql = ''

    def __init__(self):
        self.xsql = Conexao()
    
    def buscarPesoa(self,nomePessoa):
        try:
            sql = "SELECT codigo,funcao_principal FROM pessoas WHERE nome = '" + nomePessoa + "'"
            retorno = self.xsql.requisitar(sql)
            return retorno 
        except Exception as e:
            print(e)
            return False
    
    def inserirPessoa(self,nomePessoa,idade,nacionalidade,funcao_principal):
        try:
            sql = "INSERT INTO pessoas(nome,idade,nacionalidade,funcao_principal) VALUES ('" + nomePessoa + "'," + idade +", '"+ nacionalidade + "," + funcao_principal + ")"
            self.xsql.inserir(sql)
            sql = "SELECT LAST_INSERT_ID() as codigo;"
            retorno = self.xsql.requisitar(sql)
            return retorno
        except Exception as e:
            print(e)
            return False