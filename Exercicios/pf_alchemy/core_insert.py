from core import user_table , engine

con = engine.connect()
ins = user_table.insert()

# insert pessoa
new = ins.values(idade=24, nome='Lock dog', senha='testando')
con.execute(new)

# insert pessoas
con.execute(user_table.insert(),[
    {'nome':'Abraham', 'idade':60, 'senha':'sem senha'},
    {'nome':'Bolsonaro', 'idade':64, 'senha':'3*8*'},
    {'nome':'Queiroz', 'idade':22, 'senha':'_portas'},
    {'nome':'Lula', 'idade':70, 'senha':'preso'},
    {'nome':'Cid', 'idade':60, 'senha':'babaca'},
])
