from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

# Conecte ao banco de dados
engine = create_engine('postgresql://postgres:admin@localhost:5432/equipebd')

# Crie uma sessão 
Session = sessionmaker(bind=engine)
session = Session()

# Declare uma base para mapeamento
Base = declarative_base()

# Classe que representa a tabela Atividade
class Atividade(Base):
   __tablename__ = 'atividade'
   codigo = Column(Integer, primary_key=True)
   descricao = Column(String)
   
# Classe que representa a relação entre Atividade e Projeto   
class AtividadeProjeto(Base):
   __tablename__ = 'atividade_projeto' 
   codAtividade = Column(Integer, ForeignKey('atividade.codigo'), primary_key=True)
   codProjeto = Column(Integer, primary_key=True)

# Escalar as mudanças para o banco de dados   
Base.metadata.create_all(engine)

# Selecione o ID do projeto
projeto_id = 1

# Obtenha atividades para esse projeto  
atividades = session.query(Atividade).\
       join(AtividadeProjeto).\
       filter(AtividadeProjeto.codProjeto == projeto_id).\
       all()

# Imprima as descrições das atividades       
for atividade in atividades:
    print(atividade.descricao)

# Feche a sessão         
session.close()