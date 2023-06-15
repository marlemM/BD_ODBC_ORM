import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String
from sqlalchemy.orm import declarative_base


# Definição de conexão para o banco de dados
db_url = 'postgresql://postgres:admin@localhost/equipebd'



# Crie o engine do SQLAlchemy e a base do modelo:
engine = create_engine(db_url)
Base = declarative_base()


# Crie uma classe para a tabela de log:
class Log(Base):
    __tablename__ = 'log'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    query = Column(String)
    duration = Column(Integer)  # Em segundos

# Crie a tabela de log no banco de dados:
Base.metadata.create_all(bind=engine)


# Crie uma função para realizar a consulta e gravar o log:
def executar_consulta_e_gravar_log():
    # Inicie o cronômetro
    inicio = datetime.datetime.now()

    # Execute a consulta
    Session = sessionmaker(bind=engine)
    session = Session()
    # Aqui você deve inserir a sua consulta específica
    # por exemplo: resultados = session.query(Tabela).all()

    # Encerre o cronômetro
    fim = datetime.datetime.now()
    duracao = (fim - inicio).seconds

    # Grave o log no banco de dados
    log = Log(query="SELECT * FROM Tabela", duration=duracao)
    session.add(log)
    session.commit()

    # Exiba a duração no console
    print("Duração da consulta:", duracao, "segundos")

executar_consulta_e_gravar_log()