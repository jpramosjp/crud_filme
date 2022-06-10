from sqlite3 import Cursor
from tkinter import EXCEPTION
from matplotlib import interactive
import pymysql

class Conexao:
   conexao = ''

   def __init__(self):
      self.conectar()
     
   def conectar(self):
      try:
         self.conexao = pymysql.connect(host="localhost",user="root",passwd="",database="crud_filmes")
      except Exception as e:
         print("Não foi possível conecatar com o banco: ", e )

   def requisitar(self,sql):
      try:
         while True:
            try:
               with self.conexao.cursor() as cursor:
                  cursor.execute(sql)
                  retorno =  cursor.fetchall()
                  break
            except pymysql.OperationalError:
               self.conexao.ping(True)   
         return retorno
      except Exception as e:
         print("Não foi possível fazer a requesicao: ", e)
   
   def inserir(self,sql):
      try:
         while True:
            try:
               with self.conexao.cursor() as cursor:
                  cursor.execute(sql)
                  self.conexao.commit()
                  break
            except pymysql.OperationalError:
               self.conexao(True)
         return True
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