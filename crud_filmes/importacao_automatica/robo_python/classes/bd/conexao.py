import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="crud_filmes" )
cursor = connection.cursor()

teste = "select * from pessoas"

cursor.execute(teste)
rows = cursor.fetchall()
for row in rows:
   print(row)
# # some other statements  with the help of cursor
# connection.close()