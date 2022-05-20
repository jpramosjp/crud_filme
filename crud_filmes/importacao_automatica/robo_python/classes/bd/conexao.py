import pymysql

class Conexao:
   conexao = ''

   def __init__(self):
      self.conectar()
     
   def conectar(self):
      try:
         self.conexao = pymysql.connect(host="localhost",user="root",passwd="",database="crud_filmes" ).cursor()
      except Exception as e:
         print("Não foi possível conecatar com o banco: ", e )

   def requisitar(self,sql):
      try:
         self.conexao.execute(sql)
         teste = self.conexao.fetchall()
         return teste
      except Exception as e:
         print("Não foi possível fazer a requesicao: ", e)






#database connection
# connection = pymysql.connect(host="localhost",user="root",passwd="",database="crud_filmes" )
# cursor = connection.cursor()

# teste = "select * from pessoas"

# cursor.execute(teste)
# rows = cursor.fetchall()
# for row in rows:
#    print(row)
# # some other statements  with the help of cursor
# connection.close()