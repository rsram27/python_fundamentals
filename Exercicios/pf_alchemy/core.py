from sqlalchemy import(create_engine, MetaData, Column,
                        Table, Integer, String, DateTime)

from datetime import datetime

engine = create_engine('sqlite:///teste.db', echo=True)
metadata = MetaData(bind=engine)

user_table = Table('usuarios',
                        metadata,
                            Column('id', Integer, primary_key=True),
                            Column('nome', String(40), index=True),
                            Column('idade', Integer, nullable=False),
                            Column('senha', String),
                            Column('CriadoEm', DateTime, default=datetime.now),
                            Column('AtualizadaEm', DateTime, default=datetime.now, onupdate=datetime.now)
                            )

metadata.create_all(engine)
