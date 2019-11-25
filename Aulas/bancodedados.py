# ################# POSTGRESQL ####################
# # import psycopg2

# # try:
# #     con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")

# #     cur = con.cursor()
    
# #     # cur.execute("insert into scripts(nome, conteudo) values ('devops','Projeto de python')")
# #     # cur.execute("update scripts set nome = 'DEVOPS NOVO' where nome = 'devops'")
# #     cur.execute("select * from scripts order by id desc")
# #     print(cur.fetchone())
# #     con.commit()
# #     print('Registro criado com sucesso')
# # except Exception as e:
# #     print(f'Erro:{e}')
# #     print('Fazendo rollback')
# #     con.rollback()
# # finally:
# #     print('Finalizando conexao com o banco de dados')
# #     cur.close()
# #     con.close()


# ################# MYSQL ####################

# # import MySQLdb

# # try:      
# #     con = MySQLdb.connect(host="localhost", user="developer", passwd="4linux",db="projetos")

# #     cur = con.cursor()

# #     # cur.execute("insert into clientes(nome,endereco) values('Joaquim','Rua das Flores')")
# #     # cur.execute("select * from clientes")
# #     print(cur.fetchall())
# #     con.commit()
# #     print('Inserido com sucesso')
# # except Exception as e:
# #     con.rollback()
# #     print(f'Erro : {e}')
# # finally:
# #     print('Finalizando conexao com o banco de dados')
# #     cur.close()
# #     con.close()


# ################### MONGO ######################

# from pymongo import MongoClient

# cliente = MongoClient('localhost')

# db = cliente['ronaldo']

# def inserirDados(x,y):

#     try:
#         db.fila.insert({"_id":11,
#                         "empresa":"4Linux",
#                         "cursos":[
#                                     {"nomecurso":x,
#                                     "valor":1000},
#                                     {"nomecurso":y,
#                                     "valor":1100}
#                                 ],
#                         "servico":"Intranet",
#                         "status":0})

#     except Exception as e:
#         print(f'Erro{e}')


# # inserirDados("Postgres","Mysql")

# def buscarDados():

#     for r in db.fila.find():
#         print(f'Empresa {r["empresa"]}')
#         for c in r["cursos"]:
#             print("============")
#             print(f'Nome {c["nome"]} Valor: {c["valor"]}')

# buscarDados()