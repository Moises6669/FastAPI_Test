from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:moises@localhost:3306/prueba")

meta = MetaData()

connection_database = engine.connect()
