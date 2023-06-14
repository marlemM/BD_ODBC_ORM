import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base


# Defina a URL de conexão com o banco de dados
db_url = 'postgresql://postgres:admin@localhost/equipebd'

# Crie o engine do SQLAlchemy
engine = create_engine(db_url)

#Base = declarative_base(bind=engine)
Base = declarative_base()


# Definindo as classes para as tabelas projeto, equipe, membro e atividade

class Projeto(Base):
    __tablename__ = 'projeto'

    codigo = Column(Integer, primary_key=True)
    descricao = Column(String(45))
    depto = Column(Integer, ForeignKey('departamento.codigo'))
    responsavel = Column(Integer, ForeignKey('funcionario.codigo'))
    dataInicio = Column(Date)
    dataFim = Column(Date)
    situacao = Column(String(45))
    dataConclusao = Column(Date)

    equipe = relationship('Equipe', back_populates='projeto')
    atividades = relationship('Atividade', back_populates='projeto')


class Equipe(Base):
    __tablename__ = 'equipe'

    codigo = Column(Integer, primary_key=True)
    nomeEquipe = Column(String(45))

    projeto = relationship('Projeto', back_populates='equipe')
    membros = relationship('Membro', back_populates='equipe')


class Membro(Base):
    __tablename__ = 'membro'

    codigo = Column(Integer, primary_key=True)
    codEquipe = Column(Integer, ForeignKey('equipe.codigo'))
    codFuncionario = Column(Integer, ForeignKey('funcionario.codigo'))

    equipe = relationship('Equipe', back_populates='membros')


class Atividade(Base):
    __tablename__ = 'atividade'

    codigo = Column(Integer, primary_key=True)
    descricao = Column(String(45))
    dataInicio = Column(Date)
    dataFim = Column(Date)
    situacao = Column(String(45))
    dataConclusao = Column(Date)
    codProjeto = Column(Integer, ForeignKey('projeto.codigo'))

    projeto = relationship('Projeto', back_populates='atividades')

# Funções auxiliares para os cálculos necessários:

def calcular_qtd_membros_equipe(projeto):
    return len(projeto.equipe.membros)

def calcular_numero_dias_atraso_projeto(projeto):
    data_hoje = datetime.date.today()
    if projeto.dataFim and projeto.dataFim < data_hoje:
        return (data_hoje - projeto.dataFim).days
    return 0

def calcular_qtd_atividades_projeto(projeto):
    return len(projeto.atividades)

def calcular_qtd_atividades_atrasadas_projeto(projeto):
    return projeto.atividades.filter(Atividade.situacao != 'Concluído(a)').count()

def calcular_soma_dias_atraso_atividades_atrasadas(projeto):
    data_hoje = datetime.date.today()
    return projeto.atividades.filter(Atividade.situacao != 'Concluído(a)') \
        .filter(Atividade.dataFim < data_hoje) \
        .with_entities(func.sum(func.datediff('day', Atividade.dataFim, data_hoje))).scalar() or 0


# Criando o procedimento para exibir o relatório analítico dos projetos:

def relatorio_projetos():
    Session = sessionmaker(bind=engine)
    session = Session()

    projetos = session.query(Projeto).all()

    for projeto in projetos:
        gerente = session.query(Funcionario).get(projeto.responsavel)
        qtd_membros_equipe = calcular_qtd_membros_equipe(projeto)
        dias_atraso_projeto = calcular_numero_dias_atraso_projeto(projeto)
        qtd_atividades_projeto = calcular_qtd_atividades_projeto(projeto)
        qtd_atividades_atrasadas_projeto = calcular_qtd_atividades_atrasadas_projeto(projeto)
        soma_dias_atraso_atividades_atrasadas = calcular_soma_dias_atraso_atividades_atrasadas(projeto)

        print("Código do Projeto:", projeto.codigo)
        print("Nome do Projeto:", projeto.descricao)
        print("Nome do Gerente:", gerente.nome)
        print("Quantidade de Membros da Equipe:", qtd_membros_equipe)
        print("Número de Dias de Atraso do Projeto:", dias_atraso_projeto)
        print("Quantidade de Atividades do Projeto:", qtd_atividades_projeto)
        print("Quantidade de Atividades Atrasadas do Projeto:", qtd_atividades_atrasadas_projeto)
        print("Soma dos Dias de Atraso das Atividades Atrasadas:", soma_dias_atraso_atividades_atrasadas)
        print("")

    session.close()

