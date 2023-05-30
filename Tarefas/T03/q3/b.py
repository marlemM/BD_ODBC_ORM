from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
db_url = 'postgresql://postgres:admin@localhost/equipebd'

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

def connect():
    try:
        # Get the version of the PostgreSQL server
        db_version = session.execute('SELECT version()').scalar()
        print('Versão do PostgreSQL:')
        print(db_version)

        # Query to list the activities of a project
        projeto_id = 1  # ID do projeto desejado
        atividades = session.execute(
            'SELECT a.descricao FROM atividade AS a JOIN atividade_projeto AS ap ON a.codigo = ap.codAtividade WHERE ap.codProjeto = :projeto_id',{'projeto_id': projeto_id}
        ).fetchall()

        # Print the results
        print("Número total de linhas:", len(atividades))
        for row in atividades:
            print(row[0])
    except Exception as error:
        print(error)
    finally:
        # Close the session
        session.close()
        print('Conexão com o banco de dados fechada.')


if __name__ == '__main__':
    connect()
