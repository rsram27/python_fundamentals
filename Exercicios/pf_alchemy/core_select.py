from sqlalchemy import select
from core import user_table

selecione = select([user_table])
selecione_01 = select([user_table]).where(user_table.c.nome == 'teste')

print([x for x in selecione_01.execute()])
print([x for x in selecione.execute()])


