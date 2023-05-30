from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker

# Defina a URL de conexão com o banco de dados
db_url = 'postgresql://postgres:admin@localhost/equipebd'

# Crie o engine do SQLAlchemy
engine = create_engine(db_url)

# Crie uma fábrica de sessões
Session = sessionmaker(bind=engine)
session = Session()

def connect():
    try:
        # Obtenha a versão do servidor PostgreSQL
        db_version = session.execute(text('SELECT version()')).scalar()
        print('Versão do PostgreSQL:')
        print(db_version)

        # Consulta para listar as atividades de um projeto
        projeto_id = 1  # ID do projeto desejado
        atividades = session.execute(
            text('SELECT a.descricao FROM atividade AS a JOIN atividade_projeto AS ap ON a.codigo = ap.codAtividade WHERE ap.codProjeto = :projeto_id'),{'projeto_id': projeto_id}
        ).fetchall()

        # Imprima os resultados
        print("Número total de linhas:", len(atividades))
        for row in atividades:
            print(row[0])
    except Exception as error:
        print(error)
    finally:
        # Feche a sessão
        session.close()
        print('Conexão com o banco de dados fechada.')


if __name__ == '__main__':
    connect()