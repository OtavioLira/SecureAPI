from pony.orm import Database, Required, PrimaryKey, Optional
import datetime

db = Database()

class LogEventos(db.Entity):
    id = PrimaryKey(int, auto=True)
    descricao = Optional(str)
    tipo = Optional(str)
    data_cricao = Optional(datetime.datetime, default=datetime.datetime.now)
    usuario = Optional(str)

class usuario(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique=True)
    hashed_password = Required(str)

# Não sobe essa poha no Github / deixe fora do repositorio
db.bind(provider='sqlite',filename="database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)