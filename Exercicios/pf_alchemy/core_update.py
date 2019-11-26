from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atualizar = update(user_table).where(user_table.c.nome == 'teste')

atualizar = atualizar.values(nome='Daniel')

resultado = con.execute(atualizar)

print(resultado.rowcount)

atualizar = update(user_table).where(user_table.c.nome == 'Daniel')
atualizar = atualizar.values(idade=(user_table.c.idade -1 ))
resultado = con.execute(atualizar)

print(resultado.rowcount)